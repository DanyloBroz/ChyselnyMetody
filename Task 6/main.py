from pprint import pprint
import math
import matplotlib.pyplot as plt
import numpy as np

pi = math.pi


def function(x):
    return math.exp(math.sin(x) + math.cos(x))
    #return 3 * math.cos(15 * x)


def creat_interpolation_nodes_equidistant(n, period):
    res = []
    for j in range(2 * n):
        x = period[0] + (period[1] - period[0]) * j / (2 * n)
        function_value = function(x)
        info = {
            "x": x,
            "y": function_value
        }
        res.append(info)
    return res


def interpolation_function_value(x, n, interpolation_nodes):

    q_t = 0
    for k in range(n + 1):
        sum_b_k = 0
        sum_a_k = 0
        for j in range(2 * n):

            sum_a_k += interpolation_nodes[j]["y"] * math.cos(pi * k * j / n)
            sum_b_k += interpolation_nodes[j]["y"] * math.sin(pi * k * j / n)
        a_k = sum_a_k / n
        b_k = sum_b_k / n
        if k == 0:
            q_t += a_k / 2
        elif k == n:
            q_t += a_k * math.cos(n * x) / 2
        else:
            q_t += a_k * math.cos(k * x) + b_k * math.sin(k * x)
    return q_t


if __name__ == '__main__':

    m = 10
    construction_interval = [-2 * pi, 2 * pi]
    period = 2 * pi/15
    fig, ax = plt.subplots()
    x = np.linspace(construction_interval[0], construction_interval[1], m)
    function2 = np.vectorize(function)
    y = function2(x)
    ax.plot(x, y, color="black")
    plt.show()
    for n in [2, 4, 8, 100]:
        fig_n, ax_n = plt.subplots()
        x1 = []
        y1 = []
        left = construction_interval[0]
        while True:
            right = left + period
            interpolation_nodes_equidistant = creat_interpolation_nodes_equidistant(n, [left, right])
            # print(interpolation_nodes_equidistant)
            flag=False
            for i in creat_interpolation_nodes_equidistant(m, [left, right]):
                if i["x"] <= construction_interval[1]:
                    t_i = (i["x"] - left) * (2 * pi) / (
                                right - left)

                    y_i = interpolation_function_value(t_i, n, interpolation_nodes_equidistant)
                    x1.append(i["x"])
                    y1.append(y_i)
                else:
                    flag=True
                    break
            if flag:
                break
            left+=period

        ax_n.plot(x1, y1)
        plt.show()
        break
