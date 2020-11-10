from matplotlib import pyplot as plt 
import numpy as np 
from tqdm import tqdm

"""
Every guy plays the gem.
Interaction:
    C  D
C   1  0 
D   b  0
Each guy has eight immeadiate neighbors.
A cooperator surrounded by 8 cooperators recies payoff 8
A defector surrounded by 8 cooperators receives payoff 8b
"""

class Board:

    def __init__(self, N=2, b=1.5):
        self.N = N
        self.b = b
        # self.lattice = np.empty((N, N), dtype=object)
        self.lattice = np.ones((N, N))
        self.payoff_lattice = np.zeros((N, N))

    def set_up_simple_square(self):
        self.lattice = np.zeros((self.N, self.N))
        self.lattice[self.N//2, self.N//2 - 1] = 1
        self.lattice[self.N//2 - 1, self.N//2] = 1
        self.lattice[self.N//2 - 1, self.N//2 - 1] = 1
        self.lattice[self.N//2, self.N//2] = 1

    def set_up_single_defector(self):
        self.lattice = np.ones((self.N, self.N))
        self.lattice[self.N//2, self.N//2] = 0

    def advance(self):
        old_strategies = self.lattice.copy()

        self.compute_payoffs()
        for i in range(self.N):
            for j in range(self.N):
                dir = self.dir_happiest_neighbor(i, j)
                coords = self.move(dir, i, j)
                # Change strategy if someone did better
                if self.payoff_lattice[coords] > self.payoff_lattice[i, j]:
                    self.lattice[i, j] = old_strategies[coords]

    def set_up_random(self):
        self.lattice = (np.random.rand(self.N, self.N) > 0.5).astype(int)

    def compute_site_payoff(self, i, j):
        
        # Am I cooperating?
        payoff_multiple = 1 if self.lattice[i, j] else self.b

        payoff = 0

        for dir in range(8):
            payoff += self.lattice[self.move(dir, i, j)]

        return payoff * payoff_multiple

    def compute_payoffs(self):
        for i in range(self.N):
            for j in range(self.N):
                self.payoff_lattice[i, j] = self.compute_site_payoff(i, j)

    def dir_happiest_neighbor(self, i, j):
        values = []

        for dir in range(8):
            values.append(self.payoff_lattice[self.move(dir, i, j)])

        best_dir = np.asarray(values).argmax()

        return best_dir

    def move(self, dir, i, j):

        # North
        if dir == 0:
            return ((i - 1) % self.N, j)
        # North East 
        if dir == 1:
            return ((i - 1) % self.N, (j + 1) % self.N)
        # East 
        if dir == 2:
            return (i, (j + 1) % self.N)
        # South East 
        if dir == 3:
            return ((i + 1) % self.N, (j + 1) % self.N)
        # South 
        if dir == 4:
            return ((i + 1) % self.N, j)
        # South West 
        if dir == 5:
            return ((i + 1) % self.N, (j - 1) % self.N)
        # West 
        if dir == 6:
            return (i, (j - 1) % self.N)
        # North West
        if dir == 7:
            return ((i - 1) % self.N, (j - 1) % self.N)

if __name__ == "__main__":
    N = 50 
    board = Board(N, 1.1)
    # board.set_up_simple_square()
    # board.set_up_single_defector()
    board.set_up_random()
    plt.figure() 
    plt.imshow(board.lattice)
    plt.title("1")
    for i in tqdm(range(8)):
        board.advance() 
        plt.figure()
        plt.imshow(board.lattice)
        plt.title(f"{i + 1}")
    plt.show()