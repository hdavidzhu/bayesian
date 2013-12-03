import scipy.misc as misc
import numpy
import matplotlib.pyplot as plt

times = 20
x = 0
balance = 0.6
combination = [0] * (times+1)

while x <= times: 
	combination[x] = misc.comb(times,x) * balance**x * (1-balance)**(times-x)
	x = x + 1

plt.plot(combination)
plt.show()