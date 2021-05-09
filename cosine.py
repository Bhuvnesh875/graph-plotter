import matplotlib.pyplot as plt
import numpy as np

def cos():
 print('Enter the value of n. Graph will be plotted from 0 to n*pie')
 n=int(input())
 x=np.arange(0,n*np.pi,0.1)
 y=np.cos(x)
 plt.plot(x,y)
 plt.xlabel('x values from 0 to n*pi')
 plt.ylabel('cos(x)')
 plt.title('Plot of cosine graph')
 plt.show()