import numpy
from pprint import pprint
def array_x(a, b, n):
    x = []
    for k in range(n+1):
        x.append(a + k * (b - a) / n)
    return x


def B1(x):
    if abs(x) <= 1:
        return 1 - abs(x)
    return 0


def B2(x):
    if abs(x) <= 0.5:
        return 0.5 * (2-(abs(x) - 0.5) ** 2 - (abs(x) + 0.5) ** 2)
    elif 0.5 < abs(x) and abs(x) <= 1.5:
        return 0.5 * ((abs(x) - 1.5) ** 2)
    return 0


def B3(x):
    if abs(x) <= 1:
        return (1/6) * ((2-abs(x)) ** 3 - 4*(1-abs(x)) ** 3)
    elif 1 < abs(x) and abs(x) <= 2:
        return (1/6) * ((2- abs(x) ) ** 3)
    return 0

if __name__ == '__main__':
    a ,b= -5,5
    n,m = 4, 100
    x=array_x(a,b,m)

    x_k=array_x(a,b,n)

    X=[]
    for i in x:
        r=[(j-i)/((a-b)/n) for j in x_k]
        X.append(r)
    pprint(X)
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()

    for i in range(len(x_k)):
        y = []
        P=[]
        for k in X:
            P.append(k[i])
        print(P)
        for j in P:
            y.append(B1(j))
        print(x)
        print(y)
        ax.plot(x, y)
    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/