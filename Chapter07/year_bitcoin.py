#Determining a linear trend line for Bitcoin
import numpy as np
from scipy.linalg import lstsq

year = np.array([2010.91666666666, 2011.41666666666, 2011.91666666666,
             2012.41666666666, 2012.91666666666, 2013.41666666666,
             2013.91666666666, 2014.41666666666, 2014.91666666666,
             2015.41666666666, 2015.91666666666, 2016.41666666666,
             2016.91666666666, 2017.41666666666])
btc_price = np.array([0.23, 9.57, 3.06, 5.27, 12.56, 129.3, 946.92, 629.02,
	              378.64, 223.31, 362.73, 536.42, 753.25, 2452.18])

M = year[:, np.newaxis]**[0, 1]
model, _, _, _ = lstsq(M,btc_price)
print "Intercept =", model[0]
print "year coefficient =", model[1]
