#Predicting profit based on the year
import numpy as np
from scipy.linalg import lstsq

year = np.array([2011,2012,2013,2014,2015,2016,2017])
profit = np.array([40,43,45,50,54,57,59])

M = year[:, np.newaxis]**[0, 1]
model, _, _, _ = lstsq(M,profit)
print "Intercept =", model[0]
print "year coefficient =", model[1]
