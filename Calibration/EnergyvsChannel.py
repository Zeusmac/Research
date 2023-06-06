

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b):
    return a*x + b
    
def linfit (x, y):
    popt, pvoc = curve_fit(func, x, y)
    return popt

energy1 = np.array([344.2,778.9,1112,1408])

energy = np.array([121.8,344.2,778.9,1112,1408])

""" ID0
"""
mean0 = np.array([164.343,466.747,1051.732,1501.997,1901.775])

# ID 1
mean1 = np.array([402.204,1137.329,2572.897,3674.496,4652.698])

""" ID 2
"""
#mean2 = np.array([406.633,1150.845,2603.560,3719.468,4709.464])

""" ID 3 
"""
mean3 = np.array([409.971,1159.814,2625.496,3748.819,4746.339])


# Cl2

"""ID 5"""
#mean5 = np.array([392.771,1110.776,2513.657,3590.830,4546.498])

"""ID 6"""
mean6 = np.array([1093.765,2475.334,3535.818,4476.719])

"""ID 7"""
mean7 = np.array([1139.715,2579.194,3684.04,4664.402])

"""ID 8"""

mean8 = np.array([391.208,1105.791,2502.206,3573.028,4523.994])



#cl3

#ID 10

mean10 = np.array([1134.250,2566.546,3665.894,4641.711])

#ID 11

mean11 = np.array([1124.176,2543.188,3632.286,4599.016])

#ID 12gg

mean12 = np.array([1050.393,2556.765,3650.675,4622.421])

#ID 13

mean13 = np.array([391.970,1109.343,2511.266,3586.091,4540.488])


#cl4


#ID 16

mean16 = np.array([463.763,1049.923,1499.090,1898.103])

#ID 17

mean17 = np.array([465.427,1054.0428,1505.553,1906.471])

#ID 18

mean18 = np.array([])

#ID 19 

mean19 = np.array([935.034,2116.056,3022.360,3826.429])

#cl5

#21

mean21 = np.array([])

#22

mean22 = np.array([])

#23

mean23 = np.array([])


#24
mean24 = np.array([])



#cl7

#35

mean35 = np.array([400.109,1130.165,2556.566,3652.590,4624.946])

#cl8

#ID 37

mean37 = np.array([672.652,1901.644,4304.567,6145.789,7782.294])

#Cl9

#45
mean45 = np.array([1153.994,2610.752,3728.846,4721.820])


#cl 11

""" ID 53 
"""
mean53 = np.array([403.930,1142.716,2586.1482,3693.897,4676.903])

""" ID 54
"""
mean54 = np.array([409.965,1160.10,2625.746,3749.599,4747.673])

""" ID 55
"""
mean55 = np.array([393.407,1113.128,2518.4721,3597.395,4554.825])
#mean55 = np.array([385.772,1090.630,2468.213,3525.464,4463.935])

""" ID 56
"""
mean56 = np.array([760.295,2149.977,4866.009,6947.732])


slope = []
intercept = []
ran = [16,35,37,45]

def plot (mean,energy):
    popt = linfit(mean, energy)
    plt.plot(mean, func(mean, *popt))
    plt.scatter(mean,energy)
    plt.xlabel("Channel")
    plt.ylabel("Energy")
    plt.show()
    return popt

def list(mean, energy):
    S, t = plot(mean, energy)
    slope.append(S)
    intercept.append(t)

list(mean16,energy1)
list(mean35,energy)
list(mean37,energy)
list(mean45,energy1)

#for i in range(4):
print(ran[0],"\t%2.5f\t%.5f\t\n" % (intercept[0],slope[0]))
