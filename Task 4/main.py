import numpy
import matplotlib.pyplot as plt
from SolutionMtrx import SolutionMtrx
import math


def c_y(x_l, res):
    y_l = []
    for x in x_l:
        y = 0
        for i in range(0, len(res)):
            y += res[i] * math.pow(x, i)
        y_l.append(y)
    return y_l

def c_m(x_l, n):
    arr = []
    for i in range(0, n + 1):
        a = []
        for x in x_l:
            a.append(math.pow(x, i))
        arr.append(a)
    a_arr = numpy.array(arr).T
    return a_arr

def program3_1():

    x = [-3, -1, 0, 1, 3]
    y = [-4, -0.8, 1.6, 2.3, 1.5]
    for n in [1,2,3]:
        plt.plot(x, y, color="red")
        matr = c_m(x, n)
        a = numpy.dot(matr.T, matr)
        b = numpy.dot(matr.T, numpy.array(y))
        l = SolutionMtrx(a, b, n)
        l.lurozklad()
        r = l.get_res()
        x_new=[x[0]+(x[-1]-x[0])/100*i for i in range(100)]
        y_l = c_y(x_new, r)
        plt.plot(x_new, y_l)
        plt.show()




def program3_2():
    a = [[1.0, 3.0], [2.0, 4.0], [5.0, 6.0]]
    b = [1.0, 0.0, 1.0]
    print(a)
    print(b)
    a_dot = numpy.dot(numpy.array(a).T, a)
    b_dot = numpy.dot(numpy.array(a).T, b)
    help = SolutionMtrx(a_dot, b_dot, 1)
    help.lurozklad()
    res = help.get_res()
    e = help.get_miff(a, b, res)
    return res, e

if __name__ == '__main__':
    program3_1()
    print(program3_2())


