import math

import numpy as np


class SolutionMtrx:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n
        self.sm = np.diag(np.full(self.n + 1, 1.0))

    def lurozklad(self):
        det_a = 1
        for i in range(0, self.n + 1):
            self.sm[i][0] = self.a[i][0] / self.a[0][0]

        for i in range(1, self.n + 1):
            for j in range(1, self.n + 1):
                if i <= j:
                    self.a[i][j] = self.a[i][j] - self.get_sum(i, j, True)
                    det_a *= self.a[i][j]
                    # if det_a == 0:
                    #     raise RuntimeError("Det A equals zero")
                else:
                    self.sm[i][j] = 1 / self.a[j][j] * (self.a[i][j] - self.get_sum(i, j, False))

    def get_sum(self, i, j, b):
        res_sum = 0
        if b:
            side = i
        else:
            side = j
        for k in range(0, side):
            res_sum += self.sm[i][k] * self.a[k][j]
        return res_sum

    def update_a(self):
        for i in range(0, self.n + 1):
            for j in range(0, self.n + 1):
                if i > j:
                    self.a[i][j] = 0.0

    def get_res(self):
        res_y = self.get_y_vector()
        res_x = np.zeros(self.n + 1)
        for i in range(self.n, -1, -1):
            s = 0.0
            for k in range(i + 1, self.n + 1):
                s += self.a[i][k] * res_x[k]
            res_x[i] = float(1 / self.a[i][i] * (res_y[i] - s))
        return res_x

    def get_y_vector(self):
        res_y = []
        for i in range(0, self.n + 1):
            s = 0.0
            for k in range(0, i):
                s += self.sm[i][k] * res_y[k]
            res_y.append(self.b[i] - s)
        return res_y

    def get_miff(self, a_l: list, b_l: list, res_x: list):
        e_l = []
        for i in range(0, len(a_l)):
            e = 0.0
            for j in range(0, len(a_l[i])):
                e += res_x[j] * a_l[i][j]
            e -= b_l[i]
            e_l.append(math.fabs(e))
        return max(e_l)