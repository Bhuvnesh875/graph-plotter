import matplotlib.pyplot as plt
import numpy as np

def log1():
 x = list()
 print('Enter ending point')
 n = int(input())
 for i in range(1, n):
    x.append(int(i))
    y = np.log10(x)
 plt.plot(y, color='blue')
 plt.plot(x, color='red')
 plt.xlabel('Natural logs')
 plt.ylabel('Entered numbers')
 plt.title('Graph of natural log()')
 plt.legend(['log10(x)','entered number x'])
 plt.show()
