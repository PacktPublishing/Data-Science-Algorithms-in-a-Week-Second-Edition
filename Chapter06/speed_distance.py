import numpy as np
from scipy.linalg import lstsq

distance = np.array([38098, 85692, 152220])
squared_speed = np.array([160000,360000,640000])

M = distance[:, np.newaxis]**[0, 1]
model, _, _, _ = lstsq(M,squared_speed)
print "Intercept =", model[0]
print "distance coefficient =", model[1]
