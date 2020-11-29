from pprint import pprint
import math
import matplotlib.pyplot as plt
import numpy as np



def function(x):
    return 1 / (1 + 25 * x ** 2)


def function1(x):
    return math.log(x + 2)


def creat_interpolation_nodes_equidistant(n, period):
    res = []
    i = period[0]
    step = (period[1] - period[0]) / n
    while i <= period[1]:
        function_value = function(i)
        info = {
            "x": i,
            "y": function_value
        }
        res.append(info)
        i += step
    return res


def creat_interpolation_nodes_cheb(n, period):
    res = []
    for g in range(n):
        k=g+1
        x = 1 / 2 * (period[0] + period[1]) + 1 / 2 * (period[1] - period[0]) * math.cos(
            (2 * k - 1) * math.pi / (2 * n))
        function_value = function(x)
        info = {
            "x": x,
            "y": function_value
        }
        res.append(info)

    return res


def interpolation_function_value(x,interpolation_nodes):
    res = 0.0
    k = len(interpolation_nodes)
    for i in range(k):
        res_i = interpolation_nodes[i]["y"]
        L_i = 1.0
        for m in range(k):
            try:
                L_i *= (x - interpolation_nodes[m]["x"]) / (interpolation_nodes[i]["x"] - interpolation_nodes[m]["x"])
            except:
                r = "dil/0"
        res_i *= L_i
        res += res_i
    return res

def interpolation_function_value_f(interpolation_nodes,xall):
    res=[]
    for x in xall:
        res_x = 0.0
        k = len(interpolation_nodes)
        for i in range(k):
            res_i = interpolation_nodes[i]["y"]
            L_i = 1.0
            for m in range(k):
                try:
                    L_i *= (x - interpolation_nodes[m]["x"]) / (interpolation_nodes[i]["x"] - interpolation_nodes[m]["x"])
                except:
                    r = "dil/0"
            res_i *= L_i
            res_x += res_i
        res.append(res_x)
    return res


if __name__ == '__main__':

    n = 10

    period = [-1, 1]


    point = 0.1


    fig, ax = plt.subplots()
    x = np.linspace(period[0], period[1], 1000)
    function2 = np.vectorize(function)
    y = function2(x)
    ax.plot(x, y)


    interpolation_nodes_equidistant = creat_interpolation_nodes_equidistant(n, period)
    f_point_equidistant = interpolation_function_value(point,interpolation_nodes_equidistant)
    #ax.scatter(point, f_point_equidistant, c='red')
    print(period)
    x1 = []
    for i in creat_interpolation_nodes_equidistant(1000,period):
        x1.append(i["x"])
    print(x1)
    y1=interpolation_function_value_f(interpolation_nodes_equidistant,x1)
    ax.plot(x1, y1,color="green")

    print("Equidistant "+str(f_point_equidistant-function2(point)))

    interpolation_nodes_cheb= creat_interpolation_nodes_cheb(n, period)
    f_point_cheb = interpolation_function_value(point,interpolation_nodes_cheb)
    #ax.scatter(point, f_point_cheb, c='black')

    x2 = []
    for i in creat_interpolation_nodes_cheb(1000,period):
        x2.append(i["x"])
    print(x2)
    y2 = interpolation_function_value_f(interpolation_nodes_cheb,x2)
    ax.plot(x2, y2,color="black")

    print("cheb  " + str(f_point_cheb - function2(point)))

    plt.show()
    # print(-0.94+0.02)