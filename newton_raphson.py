import matplotlib.pyplot as plt
import numpy as np
from sympy import *

def Newton_Raphson(function,function_deriv,x_0):
    x = symbols('x')
    def newton_Raphson(f,df,x_i):
        x_sig = x_i -f(x_i) / df(x_i)

        while abs(x_sig - x_i) != 0:
            x_i =  x_sig
            x_sig = x_i - f(x_i) / df(x_i)
            print(x_i)
            print(x_sig)

        return 'Raiz de x: {0:.5f} '.format(x_sig)

    def f(_):
        return function.subs(x,_)
    def df(_):
        return function_deriv.subs(x,_)
    return newton_Raphson(f,df,x_0)


def graph_function(function,x):
    eje_x = np.array(range(-100, 100))*0.1
    eje_y = np.zeros(len(eje_x))
    for i in range(len(eje_x)):
        eje_y[i] = sympify(function).subs(x, eje_x[i])
    plt.plot(eje_x, eje_y, label='Funcion ', linewidth=3, color = 'blue')
    plt.title('Metodo Newton Raphson')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    x = symbols('x')
    function = sympify(input('f(x) = '))
    function_deriv = sympify(diff(function, x, 1))
    print('Derivada: ', function_deriv)
    while True:
        try:
            x_0 = float(input('X_0 : '))
            break
        except ValueError:
            print('Hubo un error, intente de nuevo')

    print(Newton_Raphson(function,function_deriv, x_0))
    graph_function(function, x)

