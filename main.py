from math import sqrt
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch


class Quadratic:

    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.y_int = (0, self.c)
        self.discriminant = self.b**2 - (4 * self.a * self.c)

    def __repr__(self):
        if self.a == 0:
            return u'f(x) = %+dx%+d'.encode('UTf-8') % (self.b, self.c)
        elif self.b == 0:
            return u'f(x) = %+dx\u00b2%+d'.encode('UTF-8') % (self.a, self.c)
        elif self.c == 0:
            return u'f(x) = %+d\u00b2%+dx'.encode('UTF-8') % (self.a, self.b)
        else:
            return u'f(x) = %+dx\u00b2%+dx%+d'.encode('UTF-8') % (self.a, self.b, self.c)

    def has_x_intercept(self):
        if self.discriminant > 0:
            return 2
        elif self.discriminant == 0:
            return 1
        else:
            return 0

    def x_intercepts(self):
        if self.has_x_intercept() == 0:
            return None
        elif self.has_x_intercept() == 1:
            return self.vertex()
        else:
            x1 = (-self.b + sqrt(self.discriminant)) / (2 * self.a)
            x2 = (-self.b - sqrt(self.discriminant)) / (2 * self.a)
            return x1, x2

    def is_square(self, num):
        root = sqrt(num)
        if int(root + 0.5) ** 2 == num:
            return True
        else:
            return False

    def is_factorable(self):
        if self.is_square(self.discriminant):
            return True
        else:
            return False

    def factored_form(self):
        x_ints = self.x_intercepts()
        vertex = self.vertex()
        a = -vertex[1] / ((max(x_ints) - vertex[0]) ** 2)
        return u'f(x) = %+d(x%+d)(x%+d)'.encode('UTF-8') % (a, -x_ints[0], -x_ints[1])

    def vertex(self):
        x = (self.b / self.a) / 2
        x = -x if not x == 0 else 0
        y = self.c - (x**2 * self.a)
        return round(x, 3), round(y, 3)

    def vertex_form(self):
        x = (self.b / self.a) / 2
        y = self.c - (x**2 * self.a)
        return u'f(x) = %+.2f(x%+.2f)\u00b2%+.2f'.encode('UTF-8') % (self.a, round(x, 3), round(y, 3))

    def graph(self, x_range=[-10, 11]):
        x = [i for i in range(x_range[0], x_range[1])]
        y = [((self.a * (i**2)) + (self.b * i) + self.c) for i in x]
        plt.plot(x, y,)
        vertex = self.vertex()
        x_ints = self.x_intercepts() if self.has_x_intercept() else None
        l = []
        l.append(mpatch.Patch(label="Vertex "+str(vertex)))
        l.append(mpatch.Patch(label="Y Intercept "+str(self.y_int)))
        if x_ints is not None:
            l.append(mpatch.Patch(label="X Intercepts "+str(x_ints)))
        plt.grid()
        plt.legend(handles=l)
        plt.savefig('graph.png', bbox_inches='tight')


if __name__ == '__main__':
    q = Quadratic(5, 25, 30)
    # print(q)
    # print(q.y_int)
    # print(q.has_x_intercept())
    # print(q.x_intercepts())
    # print(q.is_factorable())
    # print(q.factored_form())
    # print(q.vertex())
    # print(q.vertex_form())
    q.graph()
