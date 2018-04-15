import Quad


def info(quad):
    print(quad)
    print('Vertex: {}'.format(quad.vertex()))
    print('X Intercepts: {}'.format(quad.x_intercepts()))
    print('Y Intercept: {}'.format(quad.y_int))
    print('Factored Form: {}'.format(quad.factored_form()))
    print('Vertex Form: {}'.format(quad.vertex_form()))


def graph(quad):
    x_start = int(raw_input('Input range start:\n> '))
    x_stop = int(raw_input('Input range stop:\n> '))
    vector = raw_input('Do you want a vector image (Y,N) ?\n> ')
    vector = True if vector.lower() == 'y' else False
    quad.graph(x_range=[x_start, x_stop], vector=vector)


def evaluation(quad):
    while True:
        x = raw_input('Input x (q to Quit):\n> ')
        if x.lower() == 'q':
            break
        print('f({}) = {}'.format(x, quad.evaluate(float(x))))


def main():
    print('Welcome to PyQuad. Please enter the coefficients of your equation.')
    print(u'f(x)=ax\u00b2+bx+c')
    a = raw_input('Input a: ')
    b = raw_input('Input b: ')
    c = raw_input('Input c: ')
    q = Quad.Quadratic(a, b, c)
    while True:
        choice = raw_input('Do you want info(I), graph(G) or evaluation(E) ?\n> ')
        while True:
            if choice.lower() == 'i':
                info(q)
                break
            elif choice.lower() == 'g':
                graph(q)
                break
            elif choice.lower() == 'e':
                evaluation(q)
                break
            else:
                print('Input i, g or e')
                break
        choice = raw_input('Quit or Main Menu (Q, M)?\n> ')
        if choice.lower() == 'q':
            break


if __name__ == '__main__':
    main()
