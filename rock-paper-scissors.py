"""
Rock Paper Scissors game

calculates the Nash equilibrium for the 2-player zero sum game, since there is equal probablity
that either player is going to choose any of the 3 options each player is incentivized to use a
mixed strategy to obtain the optimal reward (i.e. number of wins)

=====
dependencies
=====
CVXOPT => `pip install cvxopt`

=====
example
=====
__________|_rock_|_paper_|_scissors_|__
___rock___|___0__|___1___|____-1____|__
__paper___|__-1__|___0___|_____1____|__
_scissors_|___1__|__-1___|_____0____|__
          |      |       |          |
NASH
  rock     => 0.333
  paper    => 0.333
  scissors => 0.333
"""

from cvxopt import matrix, solvers

# trying to minimize value for 3 variables of equal weight
c = matrix([1.,1.,1.])
# translated from the given reward matrix for Player A
G = matrix([
	[0., 1., -1.],
	[-1., 0., 1.],
	[1., -1., 0.]])
# zero sum game, Player B's reward matrix is opposite given Player A's reward matrix
h = matrix([0.,0.,0.])

# added restriction that sum of all variables must sum to 1
## 1*rock + 1*paper + 1*scissors = 1
A = matrix([[1.],[1.],[1.]])
b = matrix(1.)

# pass into optimized linear programming solver
solution = solvers.lp(c,G,h,A,b)
print(solution['x'])
