import matplotlib.pyplot as plt
import numpy as np
x, y = list(), list()


def Pie():
  print("enter title of graph")
  t = input()
  n = int(input("Enter no of quantities: "))
  print("Enter quantities(out of 100)")
  for i in range(0, n):
      ele = input()
      x.append(int(ele))
      d = np.array(x)
  print("Enter Labels")
  for i in range(0, n):
      ele1 = input()
      y.append(ele1)
      label = np.array(y)

  plt.pie(d, labels=label)
  plt.title(t)
  plt.legend(loc='upper right')
  plt.show()
