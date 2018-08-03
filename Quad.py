from math import sqrt
from numpy import linspace as ls

import matplotlib.pyplot as plt
import matplotlib.patches as mpatch


class Quadratic(object):
    """
    This is a Quadratic function class that takes a quadratic equation in standard form
    and returns anything that you might want.

    X and Y intercepts, vertex of graph, factored form of equation, vertex form of equation,
    graph of function as a vector or raster image (png, or pdf).

    USAGE EXAMPLES:
    >>> q = Quadratic(5, 25, 30)
    >>> print(q)
    f(x) = 5x^2 + 25x + 30
    >>> q.vertex()
    (-2.5, -1.25)
    >>> q.factored_form()
    f(x) = 5(x+2)(x+3)
    """

    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.y_int = (0, self.c)
        self.discriminant = self.b ** 2 - (4 * self.a * self.c)

    def __repr__(self, encode=True):
        """
        Python2 doesn't have default unicode support so I
        have added the encode method but matplotlib doesn't need the encode method
        so I made a default parameter and enter False when I'm using this for matplotlib
        """
        if self.b == 0 and self.c == 0:
            if encode:
                return u'f(x) = %dx\u00b2'.encode('UTF-8') % self.a
            else:
                return u'f(x) = %dx\u00b2' % self.a
        elif self.a == 0:
            if encode:
                return u'f(x) = %dx%+d'.encode('UTF-8') % (self.b, self.c)
            else:
                return u'f(x) = %dx%+d' % (self.b, self.c)
        elif self.b == 0:
            if encode:
                return u'f(x) = %dx\u00b2%+d'.encode('UTF-8') % (self.a, self.c)
            else:
                return u'f(x) = %dx\u00b2%+d' % (self.a, self.c)
        elif self.c == 0:
            if encode:
                return u'f(x) = %dx\u00b2%+dx'.encode('UTF-8') % (self.a, self.b)
            else:
                return u'f(x) = %dx\u00b2%+dx' % (self.a, self.b)
        else:
            if encode:
                return u'f(x) = %dx\u00b2%+dx%+d'.encode('UTF-8') % (self.a, self.b, self.c)
            else:
                return u'f(x) = %dx\u00b2%+dx%+d' % (self.a, self.b, self.c)

    @staticmethod
    def __is_square(num):
        """
        Checks if number is a perfect square.
        I'm adding 0.5 to root because you can never rely on exact comparisons
        when dealing with float numbers.
        Maybe sqrt(49) evaluates to 6.99999 or 7.00001
        so taking the square of the int right off isn't going to work.
        we add 0.5 and then take int() to ensure we have what we want.
        """
        root = sqrt(num)
        if int(root + 0.5) ** 2 == num:
            return True
        else:
            return False

    def has_x_intercept(self):
        """
        According to a mathematical rule:
        1. If the discriminant of a quadratic function is greater than 0,
        the vertex is below x axis, therefore the graph has 2 x-intercepts.
        2. If the discriminant of a quadratic function is equal to 0,
        the vertex is on x axis, therefore the graph has 1 x-intercept.
        3. If the discriminant of a quadratic function is less than 0,
        the vertex is above x axis, therefore the graph doesn't have x-intercepts.
        """
        if self.discriminant > 0:
            return 2
        elif self.discriminant == 0:
            return 1
        else:
            return 0

    def x_intercepts(self):
        """
        If graph has 0 x-intercepts, return None.
        If graph has 1 x-intercept, return vertex.
        If graph has 2 x-intercepts, use quadratic formula to get x-intercepts.
        """
        if self.has_x_intercept() == 0:
            return None
        elif self.has_x_intercept() == 1:
            return self.vertex()
        else:
            x1 = (-self.b + sqrt(self.discriminant)) / (2 * self.a)
            x2 = (-self.b - sqrt(self.discriminant)) / (2 * self.a)
            return round(x1, 3), round(x2, 3)

    def is_factorable(self):
        """
        According to a mathematical rule:
        If the discriminant of a quadratic function is a perfect square,
        the equation is factorable.
        """
        if self.b == 0 and self.c == 0:
            return False
        elif self.discriminant < 0:
            return False
        elif self.__is_square(self.discriminant):
            return True
        else:
            return False

    def factored_form(self):
        """
        In order to find the factored form, we need the a value
        which is obtained by looking at one of the x-intercepts.
        getting the distance from the x of the vertex and checking
        where it normally would end up with a value of a (by squaring it).
        Then we divide that by the y of the vertex and get the a value.
        The other two factors are easily obtained from the x-intercepts.
        """
        if self.is_factorable():
            x_ints = self.x_intercepts()
            vertex = self.vertex()
            a = -vertex[1] / ((max(x_ints) - vertex[0]) ** 2)
            return u'f(x) = %d(x%+d)(x%+d)'.encode('UTF-8') % (a, -x_ints[0], -x_ints[1])
        else:
            return None

    def vertex(self):
        """
        Using a shortened method of completing the square, I get the x and y of the vertex
        for any given graph f(x) = ax^2 + bx + c
        the vertex form is f(x) = a(x - h)^2 + k
        we can convert using this method:
        EXAMPLE. f(x) = -4x^2 - 32x + 6
        1. factor the coefficients
            f(x) = -4(x^2 + 8x) + 6

        2. create a perfect square trinomial
            f(x) = -4(x^2 + 8x + 16 - 16) + 6

        in the second step we are taking half of the second coefficient in the bracket and squaring it.
        but since we can't change the value of our graph we also subtract the same value.

        3. take the subtracted value out of the bracket (multiply by a).
            f(x) = -4(x^2 + 8x + 16) + 6 + 64

        4. now we can factor the bracket into a binomial.
            f(x) = -4(x + 4)^2 + 70

        From this final equation we can get the vertex which is (-4, 70)
        To only get the vertex, we don't need to go through all of the steps.
        We only need half of the second coefficient for the x of the vertex.
        The y of the vertex is half of the second coefficient squared times a, subtracted from c.
        """
        x = (self.b / self.a) / 2
        x = -x if not x == 0 else 0
        y = self.c - (x ** 2 * self.a)
        return round(x, 3), round(y, 3)

    def vertex_form(self):
        """
        This function gets the vertex and goes the extra step of printing
        the function in proper vertex form.
        """
        if self.b == 0 and self.c == 0:
            return u'f(x) = %dx\u00b2'.encode('UTF-8') % self.a
        x = (self.b / self.a) / 2
        y = self.c - (x ** 2 * self.a)
        return u'f(x) = %.2f(x%+.2f)\u00b2%+.2f'.encode('UTF-8') % (self.a, round(x, 3), round(y, 3))

    def evaluate(self, x):
        """
        Returns y value for any given x
        """
        return self.a * (x**2) + self.b * x + self.c

    def graph(self, x_range=None, vector=False):
        """
        This function uses matplotlib to graph the function.
        If no range is given, it takes the x of the vertex and
        graphs in a range of 5 on both sides.

        I'm using numpy linspace to create 1000 evenly spaced points within the range.
        So the graph is always smooth no matter how small the range.

        The function loops through the array of x and simply plugs it into the function
        and plots each point.

        It also adds the equation, the x and y intercepts and the vertex as labels.

        It saves the graph as "graph.png" into the same directory by default.
        If the vector option is on, it saves as a vector image "graph.pdf".
        """
        vertex = self.vertex()
        if x_range:
            x = ls(x_range[0], x_range[1], 1000)
        else:
            x = ls(vertex[0] - 5, vertex[0] + 5)
        y = [((self.a * (i ** 2)) + (self.b * i) + self.c) for i in x]
        plt.plot(x, y)
        x_ints = self.x_intercepts() if self.has_x_intercept() else None

        patches = [mpatch.Patch(color='black', label=self.__repr__(False)),
                   mpatch.Patch(color='red', label="Vertex " + str(vertex)),
                   mpatch.Patch(color='blue', label="Y Intercept " + str(self.y_int))]
        if x_ints is not None:
            patches.append(mpatch.Patch(color='orange', label="X Intercept(s) " + str(x_ints)))

        plt.grid()
        plt.legend(handles=patches)
        if vector:
            plt.savefig('graph.pdf', bbox_inches='tight')
        else:
            plt.savefig('graph.png', bbox_inches='tight')
