import numpy as np
from scipy.linalg import lstsq

#temperature data
fahrenheit = np.array([5,14,23,32,41,50])
celsius = np.array([-15,-10,-5,0,5,10])

M = fahrenheit[:, np.newaxis]**[0, 1]
model, _, _, _ = lstsq(M,celsius)
print "Intercept =", model[0]
print "fahrenheit =", model[1]
