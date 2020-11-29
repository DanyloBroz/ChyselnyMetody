from math import pi, fabs
import matplotlib.pyplot as plt
import numpy as np
from math import sin, e, pi
from scipy.integrate import quad
import math


def f1(x):
    return sin(x) / x

def f2(x):
    return (1 / math.sqrt(2 * pi)) * (math.pow(math.e, (-1 * math.pow(x, 2) / 2)))

def f3(x):
    return (-1) * math.log(math.cos(x))

def rozbita(func, prom, k):
    x, y = [], []
    for i in np.linspace(prom[0], prom[1], k):
        try:
            y.append(quad(func, prom[0], i)[0])
            x.append(i)
        except:
            pass
    return x, y


def trapetion(func, a, b, n):
    sum_r = 0.0
    xk = np.linspace(a, b, n + 1)
    h = (b - a) / n
    for i in range(0, len(xk)):
        if i == 0 or i == len(xk) - 1:
            sum_r += 1 / 2 * func(xk[i])
        else:
            sum_r += func(xk[i])
    return h * sum_r


def rectangle(func, a, b, n):
    s_0 = 0.0
    xk = np.linspace(a, b, n + 1)
    h = (b - a) / n
    for i in range(0, len(xk)):
        s_0 += func(xk[i] + h / 2)
    return h * s_0


def simpsons(func, a, b, n):
    s_0 = 0.0
    xk = np.linspace(a, b, n + 1)
    h = (b - a) / n
    for i in range(0, len(xk)):
        if i == 0 or i == len(xk) - 1:
            s_0 += func(xk[i])
        elif i % 2 == 0:
            s_0 += 2 * func(xk[i])
        else:
            s_0 += 4 * func(xk[i])
    return h / 3 * s_0


if __name__ == '__main__':
    a, b = 0.0, pi / 3
    k = 100
    x, y = rozbita(f3, [a, b], k)
    plt.plot(x, y, color="black")

    eps = 0.001

    res_integral = []
    for i in range(0, len(x)):
        n = 1
        i_n = trapetion(f3, a, x[i], n)
        i_n1 = trapetion(f3, a, x[i], n * 2)
        while fabs(i_n - i_n1) > eps:
            n *= 2
            xk = np.linspace(a, x[i], n)
            i_n = trapetion(f3, a, x[i], n)
            i_n1 = trapetion(f3, a, x[i], n * 2)

        res_integral.append((i_n1 + i_n) / 2)

    plt.plot(x, res_integral, color="red")
    plt.show()
