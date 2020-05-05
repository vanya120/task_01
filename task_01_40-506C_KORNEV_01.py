import numpy as np
import matplotlib.pyplot as plt
import os

if __name__ == '__main__':
    try: os.mkdir('results')
    except: pass
    x = np.arange(-5.12,5.13,0.01)
    A = 10
    y = A + x**2 - A * np.cos(2 * np.pi * x)

    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.show()
    
    with open('results/task_01_40-506C_KORNEV_01.txt', 'w') as ouf:
        ouf.write('x\ty(x)\n')
        for i in range(0,len(x)):
            ouf.write(str('{0:.2f}\t{1:.2f}\n'.format(x[i],y[i])))           
        
    
