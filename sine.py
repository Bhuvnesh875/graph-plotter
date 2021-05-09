import matplotlib.pyplot as plt
import numpy as np

def sin():
 print('Enter the value of n. Graph will be plotted from 0 to n*pie')
 n=int(input())
 x=np.arange(0,n*np.pi,0.1)
 y=np.sin(x)
 plt.plot(x,y)
 plt.xlabel('x values from 0 to 10pi')
 plt.ylabel('sin(x)')
 plt.title('Plot of sine graph')
 plt.show()