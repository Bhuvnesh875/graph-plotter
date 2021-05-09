import matplotlib.pyplot as plt
import numpy as np
x, y = list(), list()


def BarGraph():
    print("enter title of graph")
    t = input()
    n = int(input("Enter no of coordinates: "))
    print("Enter X label")
    xl = input()
    print("Enter quantities on x")
    for i in range(0, n):
        ele = input()
        x.append(ele)
        xpoints = np.array(x)
    print("Enter Y label")
    yl = input()
    print("Enter heights")
    for i in range(0, n):
        ele1 = input()
        y.append(int(ele1))
        ypoints = np.array(y)

    plt.bar(xpoints, ypoints)
    plt.title(t)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.show()
