"""
Matching Pennies game

simple 2-player zero sum game where each player chooses a side of their penny to display and
both players reveal choices at same time
- matching pennies gives player Even the pennies with a reward of +1
- differing pennies gives player Odd the pennies also with a reward of +1
zero sum indicates reward of -1 for other player in both scenarios

=====
dependencies
=====
CVXOPT => `pip install cvxopt`

=====
example
=====
_______|_heads_|_tails_|_
_heads_|___+1__|__-1___|_
_tails_|___-1__|__+1___|_
       |       |       |
NASH
   heads => 0.5
   tails => 0.5
"""

from cvxopt import matrix, solvers

# zero sum game using player Even's reward matrix
c = matrix([1.,1.])
G = matrix([
	[1., -1.],
	[-1., 1.]])
h = matrix([0.,0.])

# restrict sum of final probabilities to 1
A = matrix([[1.],[1.]])
b = matrix(1.)

solution = solvers.lp(c,G,h,A,b)
print(solution['x'])
