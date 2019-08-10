'''
 Simulating the sum of two independent random variables X and Y
 say we have the random variables X and Y defined as dictionaries
'''

import matplotlib.pyplot as plt
import numpy as np

def sumXY(X,Y,z_axis):
    pZ = []
    for z in z_axis:
        r = 0
        for x in X['x']:
            index_x = X['x'].index(x)
            diff = z-x
            if diff in Y['y']:
                index_y = Y['y'].index(diff)
                r += X['pX'][index_x]*Y['pY'][index_y]
        pZ.append(r)
    
    return {'z':z_axis, 'pZ':pZ}


X = {'x':[1,2,3],'pX':[1/6,3/6,2/6]}
Y = {'y':[2,3,4],'pY':[2/6,3/6,1/6]}   
z_axis = np.linspace(1,10,10)
Z = sumXY(X,Y,z_axis)

plt.figure()
plt.stem(Z['z'], Z['pZ']), plt.xlabel(r'$z$'), plt.ylabel(r'$p_Z$')
plt.savefig('pdf.png', dpi = 300)


