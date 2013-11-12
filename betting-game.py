import math
from sys import argv

heads = float(argv[1])
tails = float(argv[2])
lower_range = float(argv[3])
upper_range = float(argv[4])
count_step = .00001

fac = math.factorial(heads + tails + 1) / ((math.factorial(heads)*math.factorial(tails)))

p_density = 0
moving_point = lower_range
while moving_point < upper_range:
	p_density = count_step * (moving_point**heads * (1.0-moving_point)**tails * fac) + p_density
	moving_point = moving_point + count_step

print p_density