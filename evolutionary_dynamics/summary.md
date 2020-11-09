---
title: TEK9010 - Evolutionary Dynamics
author: Sebastian G. Winther-Larsen
date: \today
mainfont: DejaVuSerif.ttf
geometry: margin=2cm
fontsize: 16pt
...

# Quasispecies Theory

You need to incorporate three basic principles in order to model evolution;
*reproduction*, *selection* and *mutation*. In the world of mathematical 
biology, we normally assume some sort of asexual reproduction.
$$
    \dot{x} = \frac{\partial x}{\partial t} = rx
$$
The solution of this equation is exponential growth,
$$
    x(t) = x_0 = e^{rt},
$$
but may be checked by resource limitation.
Selection arises when different types of individuals reproduce at different rates.
$$
    \dot{x} = x(a - \phi),
$$
$$
    \dot{y} = y(b - \phi), 
$$
such that $a \neq b$. The term $\phi$ ensures that $x + y = 1$, which is only possible if 
$\phi = ax + by$. We may echange the values $a$ and $b$ with fitness values 
$f_i$, in the general case of $n$ types of individuals,
$$
    \dot{x}_i = x_i(f_i - \phi).
$$
Mutation arisis when reproduction is not perfectly accurat, such that 
an individual of type $i$ can transition to an individual of type $j$
in reproduction. This is is modelled by the mutation matrix $Q = [q_{ij}]$,
which is a stochastic $n\times n$ matrix.

The quasispecies equation incorporates all of these concepts 
of reproduction, selection and mutation,
$$
    \dot{x}_i = \sum_{j=1}^n x_i f_i Q_{ij} - \phi (\mathbf{x}) x_j.
$$
This equation gives the rate of change over time $\dot{x}_i$, i.e.
the time derivative of the frequency of an individual of species $i$.
The first term on the right-hand side contains the sum of product of 
all other individual frequencies $x_j$, the fitness $f_j$ and the
mutation rate $Q_{ij}$ from species $i$ to $j$. The fitness is also 
called the reproductive rate of the organism, which is determined 
by phenotype of the organism. The average fitness is given by 
$\phi(\mathbf{x}) = \sum_i f_i x_i$.

The quasispecies equation describes deterministic evolutionary dynamics
in terms of mutation and constant selection acting on an infinitely large
population. Generally, the quasipsecies equation has one global equilibrium,
consisting of a distribution of genomes in a mutation-selection balance.

# Evolutionary Game Dynamics

In game theory, games can be formulated in 
terms of a payoff matrix, which specifies the payoff for one strategy when interacting
with another. 

--- --- ---
     A   B 
 A   a   b 
 B   c   d 
--- --- ---

:Pay-off matrix with interacting strategies $A$ and $B$, with different 
payoffs $a$, $b$, $c$ and $d$, dependent on choice.

In evolutionary games we interpret the payoffs as fitness - a better 
strategy would lead to faster reproduction.

In game theory it is absolutely necessary to define the Nash equlibirium. 
If each player has a chosen strategy, and no player can increase its own expected payoff
by changing its strategy while other players keep their unchanged,
then the current set of strategy choices consitutes a Nash equilibrium.
The Nash equilibrium is related to the evolutionary stable stratgy (ESS).
In general, for games with more than two strategies, we can define the 
two concepts in the following way. If $E(S_i, S_j)$ is the expected payoff 
for strategy $S_i$ versus $S_j$, then;

- Strategy $S_k$ is a strict Nash 
equilibrium if $E(S_k, S_k) > E(S_i, S_k)$ for all $i \neq k$,
- Strategy $S_k$ is a (non-strict) Nash eqmuilibrium if
$S(S_k, S_k) \geq S(S_i, S_k)$ for all $i$, 
- Strategy S_k is ESS, if for all $i \neq k$ we have either
$E(S_k, S_k) > E(S_i, S_k)$ or 
$E(S_k, S_k) = E(S_i, S_k)$ and $E(S_k, S_i) > E(S_i, S_i)$.
- Strategy $S_k$ is stable against invasion by selection ("weak ESS")
if for all $i \neq k$ we have either
$E(S_k, S_k) > E(S_i, S_k)$ or 
$E(S_k, S_k) = E(S_i, S_k)$ and $E(S_k, S_i) \geq E(S_i, S_i)$.

Note; strict Nash implies ESS implies weak ESS implies Nash.


The replicator equation is the cornerstone of evolutionary game dynamics,
$$
    \dot{x}_i = x_i[f_j(\mathbf{x}) - \phi(\mathbf{x})].
$$
It describes deterministic evolutionary game dynamics. For $n=2$ strategies,
there can be dominance, coexistence, bistability or neutrality. For $n\geq 3$
strategies, there can be heteroclinic cycles. For $n\geq 4$, there can be 
limit cycles and chaos. The replicator equation with $n$ strategies
$$
    \dot{x}_i = x_i[\sum_{j=1}^n a_{ij}x_j - \phi(\mathbf{x})].
$$
is equivalent to the Lotka-Volterra equation from ecology,
$$
    \dot{y}_i = y_i\left(r_i + \sum_{j=1}^{n-1} b_{ij}y_j  \right),
$$
with the parameters $r_i = a_{in} - a_{nn} and $b_{ij} = a_{ij} - a_{nj}$.


# Prisoner's Dilemma and Cooperation

--- --- ---
     C   D 
 C   R   S  
 D   T   P 
--- --- ---

:A payoff matrix is a prisoner's dilemma game if $T>R>P>S$.

In a prisoner's dilemma game you can either cooperate (C) or defect (D).
Defection is "rational", because it maximises the payoff. But, if 
my opponent analyses the game the same way that I do, the we both
choose defection which leads to a suboptimal payoff. The social 

Reactive strategies on the unit square.

TFT vs ALLD $\rightarrow$ GTFT $\rightarrow$ WSLS.

# Stochastic Description of Finite Populations

The Moran process: Pick one individual for reproduction and one for death. 
The offspring of the first individual replaces the second. The individual can 
be the same. We typically have two types of individuals, A and B.

An interesting process to model is the one where the initial state is one A 
individual and N - 1 B individuals. The probability that A takes over the 
whole population is called the fixation probability. We are interesting in 
studying if a mutation can take over the whole population.

Introducing fitnes to this kind of model would make things more interesting,
as we could model a situation where the mutation is favoured.

One may also introduce random mutations, introducting the molecular clock of 
neutral evolution.

# Games in Finite Populations

Computing fixation probabilities can determine if a selection one strategy 
over another.

There is surprising $\frac{1}{3}$ law.

There are ESS that hold for finite population size $N$, i.e. ESS$_N$.

Geme dynamics of TFT and ALLD changes for finite populations.

# Evolutionary Graph Theory

A graph can represent the spatial configuration of a population, the 
differentiation hierarchy of cells in a multicellular organism, or 
a social network. Individuals are placed on the vertices of the graph and
the edges of a graph determine competitive interaction. All invividuals of 
the population are labelled $i\ in [0,N]$, at each time step, an individual 
is chosen for reproduction. The probability that the offspring of $i$ replaces 
$j$ is $w_{ij}$, i.e. the process is determinded by an $N \times N$ matrix $W$,
where all entries are probabilities. The Moran process is given by the 
_complete graph_ with identical weights.

Other simple ones:

- The (directed) cycle,
- The line and the burst,

The temperature of a vertex is given by,
$$
    T_j = \sum_{i=1}^N w_{ij}.
$$
If all vertices have the same temperature, then the fixation probability is 
equivalent to the Moran process. This is called the isothermal theorem.

The cycle and directed cycles are isothermal. All symmeric graphcs 
$w_{ij} = w_{ji}$ are isothermal.

## Suppressing and Ampllifying Selection

There are graphs that can do both these things. One-rooted 
vs multiple-rooted graphs. (Super) star,funnnel

## Games on Graphs

Games on graphs can be studied by assuming that individuals interact with their 
nearest neighbors an thereby acumulate payoff. Some games are the birth-death, 
death-birth and imitation process games.

# Spatial Games

This is just pretty pictures.