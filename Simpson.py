import matplotlib.pyplot as plt
import numpy as np
from sympy import *

x = symbols('x')
function=''
def graph_function():
    global x,function
    eje_x = np.array(range(-100, 100)) * 0.1
    eje_y = np.zeros(len(eje_x))
    for i in range(len(eje_x)):
        eje_y[i] = sympify(function).subs(x, eje_x[i])
    plt.plot(eje_x, eje_y, label='Funcion ', linewidth=3, color='blue')
    plt.title('Funcion Graficada')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.legend()
    plt.grid()
    plt.show()


def Simpson(x_0,x_2):
    global x

    x_1 = (x_0 + x_2)/2

    h =  (x_2 - x_0)/2

    return (h/3)* (f(x_0) + 4*f(x_1) + f(x_2))

def f(_):
    return sympify(function.subs(x,_))


if __name__ == "__main__":
    print('\tIntegrales Definidas : ')
    function = sympify(input('f(x) : '))
    x_0 = int(input('Valor de a : '))
    x_2 = int(input('Valor de b : '))
    print(Simpson(x_0,x_2))
    graph_function()
