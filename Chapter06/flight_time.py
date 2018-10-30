import numpy as np
from scipy.linalg import lstsq

distance = np.array([365,1462,1285,1096,517,1686,932,1160])
time = np.array([1.167,2.333,2.250,2.083,2.250,2.833,1.917,2.167])

M = distance[:, np.newaxis]**[0, 1]
model, _, _, _ = lstsq(M,time)
print "Intercept =", model[0]
print "distance coefficient =", model[1]
