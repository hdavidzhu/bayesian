# Imports.
from math import *

# Definitions.
prob = {}
prob[4] = 1.0/4.0
prob[6] = 1.0/4.0
prob[8] = 1.0/4.0
prob[20] = 1.0/4.0

rolls = [6,6,8,7,7,5,4]
normalize = 1

# Calculations.
print prob
for roll in rolls:
	for die in prob:
		if roll <= die:
			prob[die] = prob[die] * 1.0/(die)
		else:
			prob[die] = 0.0
		# Normalize.
		normalize = sum(prob.values())
		prob[die] = prob[die]/normalize
	print roll, prob