# libs
import inspect
# libs for plotting
from bokeh.plotting import figure
from bokeh.io import output_notebook, show

output_notebook()
# libs for solving
import numpy as np
from numpy.polynomial.polynomial import Polynomial
from bokeh.palettes import all_palettes

a = -1
b = 1
n = 6
m = 1  # 1 - linear 2 - square power

h = (b - a) / (n)
# print(h)
xk = np.linspace(a - h, b + h, n + 3)
# print(xk
color_line = all_palettes['Viridis'][n]

xki = xk[0]


def B1(x):
    '''
    input: array
    '''
    y = []
    x_inside = np.abs((x - xki) / h)
    for xm in x_inside:
        if xm >= 1:
            y.append(0)
        else:
            y.append(1 - xm)
    return y


def B2(x):
    '''
    input: array
    '''
    y = []
    x_inside = np.abs((x - xki) / h)

    for xm in x_inside:
        if xm >= 1.5:
            y.append(0)
        elif xm <= 0.5:
            y.append(2 - (xm - 0.5) ** 2 - (xm + 0.5) ** 2)
        else:
            y.append((xm - 1.5) ** 2)
    return y


def B3(x):
    y = []
    x_inside = np.abs(x)

    for xm in x_inside:
        if xm >= 2:
            y.append(0)
        elif xm <= 1:
            y.append(((2 - xm) ** 3 - 4 * (1 - xm) ** 3) / 6)
        else:
            y.append(((2 - xm) ** 3) / 6)
    return np.array(y)


# s(x):
def s(x):
    '''
    input: array
    return: array
    '''
    s = np.array([0 for k in range(len(x))])
    for ki in range(len(xk)):
        s = s + alpha[ki] * B3((x - xk[ki]) / h)
    return s


# here has to be block of finding alpha:

'''
     -0.5alpha-1 + 0.5alpha1 = a1*h,
     1/6 alpha i-1 + 2/3 alpha i + 1/6 alpha i+1 = yi,   i = 0,n,
     -0.5alpha n-1 + 0.5alpha n+1 = b1*h;

     1/3 alpha-1 + 2/3 alpha0 = y0 - h*a1/3
     1/6 alpha i-1 + 2/3 alpha i + 1/6 alpha i+1 = yi,   i = 0,n,
     2/3 alpha n + 1/3 alpha n+1 = 

     from that we have:
     1/6 alpha i-1 + 2/3 alpha i + 1/6 alpha i+1 = yi,
     alpha-1 = -2alpha0 + 3y0 - h*a1, alpha n+1 = -2alpha n + 3yn + h*b1   [1.1, 1.2]

     so:

     alpha i = lambda i+1 *alpha i+1 + beta i+1 [1.3]

     to find lamda and beta we use:

     lambda i+1 = 1/(-4 - lambda i), // note i am not really sure about negative 4. Also here can be positive 4.
     beta i+1 = (6y i + beta i)/(-4 - lambda i), in both cases i = 0, ... n;

     to defind lambda0, beta0 we will use 1.1 and 1.3 with i=-1, thus:
     lambda0 = -2, beta0 = 3y0 - h*a1;
     As we have lambda0, beta0 we can easily find all lambda1, ... lambda n+1 and beta1, ... beta n+1;

     To find all alpha i, where i = -1, ... n. We need to determine alpha n+1, so we have:
     alpha n+1 = (3y n + h*b1 - 2beta n+1)/(1 + 2lambda n+1)
     alpha i = lambda i+1 *alpha i+1 + beta i+1
'''


def another_f(x):
    return (x ** 2) * 3 - 2 * x + 2


def cub_f_der(x):
    return 6 * (x ** 1) - 2


# we still have xk as x in range [a,b]
yk = []
for xki in xk:
    # print(xki)
    yk.append(another_f(xki))
yk = np.array(yk)

alpha = [0 for k in range(n + 3)]
lambd = [0 for k in range(n + 2)]
beta = [0 for k in range(n + 2)]

lambd[0] = -2
beta[0] = -h * cub_f_der(a) + 3 * yk[1]

for i in range(n + 1):
    lambd[i + 1] = 1 / (-4 - lambd[i])
    beta[i + 1] = (-6 * yk[i + 1] + beta[i]) / (-4 - lambd[i])

alpha[n + 2] = (h * cub_f_der(b) + 3 * yk[n + 1] - 2 * beta[n + 1]) / (1 + 2 * lambd[n + 1])
print(lambd)
for i in reversed(range(n + 2)):
    alpha[i] = lambd[i] * alpha[i + 1] + beta[i]

# plotting using bokeh

linspace_for_plot = np.linspace(a, b, 100)  # 100 points to plot s(x)
# p = figure(plot_width=900, plot_height=400 )
p2 = figure(plot_width=900, plot_height=400)

s_to_plot = s(linspace_for_plot)

p2.line(x=linspace_for_plot, y=another_f(linspace_for_plot), color=color_line[3], line_width=3)
p2.line(x=linspace_for_plot, y=s_to_plot, color=color_line[5], line_width=2)
# show(p)
show(p2)