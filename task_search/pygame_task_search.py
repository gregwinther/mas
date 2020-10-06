import pygame, sys
import numpy as np
import math
from datetime import datetime

# Problem description
# Search area is square b/w (0,0) and (1000,1000)

# Some task T is randomly distributed over area,
# when task is completed another is added.
# Tc is the task capacity, indicating how many agents
# are needed to solve the task.

# An agent R move randomly around the area at
# speed

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
PASTEL_RED = (245, 130, 120)
MINT = (160, 250, 160)
FOREST_GREEN = (30, 140, 30)
RED = (255, 0, 0)

BACKGROUND = WHITE

FRAME_RATE = 12


class Task(pygame.sprite.Sprite):
    def __init__(self, x, y, Tc=1, Tr=50):
        super().__init__()
        radius = 5  # Size of task
        self.image = pygame.Surface([radius * 2] * 2)
        self.image.fill(BACKGROUND)
        pygame.draw.circle(self.image, RED, (radius, radius), radius)

        self.pos = np.array([x, y])
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = x, y

        # Task capacity
        self.Tc = Tc
        self.tasked_agents = pygame.sprite.Group()

        # Task radius
        self.Tr = Tr

    def update(self):

        # Task completion
        if len(self.tasked_agents) >= self.Tc:
            self.kill()


class Agent(pygame.sprite.Sprite):
    def __init__(self, x, y, Rv=25, boundary=1000):
        super().__init__()
        radius = 5
        self.image = pygame.Surface([radius * 2] * 2)
        self.image.fill(BACKGROUND)
        pygame.draw.circle(self.image, FOREST_GREEN, (radius, radius), radius)

        self.pos = np.array([x, y], dtype=np.float64)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

        self.Rv = Rv  # / FRAME_RATE
        self.Rd = 250

        self.vel = np.random.rand(2) * 2 - 1
        self.trend = (np.random.rand(2) * 2 - 1) / 2

        self.boundary = boundary

        self.tasked = False
        self.called = False
        self.call_dir = np.array([0, 0])

    def update(self):
        if self.tasked:
            # Stand still
            return

        if self.called:
            # print(self.call_dir)
            self.pos += self.call_dir
            self.rect.centerx, self.rect.centery = self.pos
            return

        self.pos += self.normalize(self.vel + self.trend, self.Rv)
        self.rect.centerx, self.rect.centery = self.pos

        # Boundary conditions
        if self.pos[0] > self.boundary or self.pos[0] < 0:
            self.vel[0] = -self.vel[0]
            self.trend[0] = -self.trend[0]
            if self.pos[0] > self.boundary:
                self.pos[0] -= 20
            if self.pos[0] > self.boundary:
                self.pos[0] += 20
        elif self.pos[1] > self.boundary or self.pos[1] < 0:
            self.vel[1] = -self.vel[1]
            self.trend[1] = -self.trend[1]
            if self.pos[1] > self.boundary:
                self.pos[1] -= 20
            if self.pos[1] > self.boundary:
                self.pos[1] += 20
        else:
            self.vel = np.random.rand(2) * 2 - 1

    def dist_to_sprite(self, other_sprite):
        return math.hypot(
            self.pos[0] - other_sprite.pos[0], self.pos[1] - other_sprite.pos[1]
        )

    def direction_to_sprite(self, other_sprite):
        direction = other_sprite.pos - self.pos
        return self.normalize(direction, self.Rv)

    def normalize(self, vector, renorm=1):
        vector /= np.linalg.norm(vector)
        return vector * renorm


class Simulation:
    def __init__(self, width=1000):
        self.WIDTH = width  # Square

        self.tasks = pygame.sprite.Group()
        self.agents = pygame.sprite.Group()
        self.tasked_agents = pygame.sprite.Group()

        self.cycles = 1000

        self.n_T = 5
        self.Tc = 1
        self.Tr = 50
        self.n_R = 1

        self.replace_tasks = True
        self.communicate = False

        self.write = False
        self.save_interval = 10

        self.total_tasks_solved = 0

    def start(self):

        if self.write == True:
            f = open(
                f"sta_T{self.n_T}_Tc{self.Tc}_Tr{self.Tr}_R{self.n_R}.txt", "w"
            )

        pygame.init()

        area = pygame.display.set_mode([self.WIDTH, self.WIDTH])

        # Assigning initial Tasks
        # Random positions of initial tasks (n, dim)
        T_pos = np.random.randint(0, self.WIDTH, size=(self.n_T, 2))

        for x, y in T_pos:

            T = Task(x, y, Tc=self.Tc, Tr=self.Tr)
            self.tasks.add(T)

        # Assigning initial Agents
        R_pos = np.random.randint(0, self.WIDTH, size=(self.n_R, 2))

        for x, y in R_pos:

            R = Agent(x, y)
            self.agents.add(R)

        clock = pygame.time.Clock()

        # Game loop
        for i in range(self.cycles):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if self.write:
                        f.close()
                    sys.exit()

            if (self.write == True) and (i % self.save_interval == 0):
                f.write(f"{i:3} {self.total_tasks_solved:3}\n")

            self.tasks.update()
            self.agents.update()

            # Any tasks completed? Create new tasks.
            n_new_tasks = self.n_T - len(self.tasks)
            self.total_tasks_solved += n_new_tasks
            if n_new_tasks > 0:
                print("Solved!")
                R_pos = np.random.randint(0, self.WIDTH, size=(n_new_tasks, 2))
                for x, y in R_pos:
                    T = Task(x, y, Tc=self.Tc, Tr=50)
                    self.tasks.add(T)
                for agent in self.agents:
                    agent.tasked = False
                    agent.called = False
                # self.tasked_agents.empty()

            # Checking if a task is found
            for agent in self.agents:
                for task in self.tasks:
                    distance = agent.dist_to_sprite(task)
                    if abs(distance) < task.Tr and not agent.tasked:
                        print(f"Aha! A task at {task.pos}")
                        agent.tasked = True
                        task.tasked_agents.add(agent)

            # Call out (and off)
            if self.communicate:
                for agent in self.tasked_agents:
                    # Make sure to not call oneself.
                    other_sprites = self.agents.copy()
                    other_sprites.remove(agent)
                    for agent2 in other_sprites:
                        distance = agent.dist_to_sprite(agent2)
                        if abs(distance) < agent2.Rd:
                            agent2.called = True
                            agent2.call_dir = agent2.direction_to_sprite(agent)

            area.fill(BACKGROUND)
            self.tasks.draw(area)
            self.agents.draw(area)
            pygame.display.flip()

            clock.tick(FRAME_RATE)

        if self.write:
            f.close()
        pygame.quit()


if __name__ == "__main__":

    simulation = Simulation(1000)
    simulation.cycles = 1000
    simulation.communicate = True
    simulation.write = True
    simulation.n_T = 2
    simulation.Tr = 50
    simulation.n_R = 7
    simulation.Tc = 3
    simulation.start()

