import numpy as np
import matplotlib.pyplot as plt
import math
from sympy import *

taylor_terms = list()
taylor_expansion = float()
taylor_polinomios = list()
x = symbols('x')
function = sympify('2*x**2')
a = 8
orden = 4
h = 10 - a
list_colors = ['red', 'green', 'blue', 'yellow','m','c']

def polinomioDeTaylor():
    global taylor_expansion, taylor_terms, x, function, a, orden, h
    counter = 0
    polinomio = 0
    for i in range(0, orden+1):
        function_deriv = diff(function, x, i)
        polinomio += ((function_deriv*(h)**i)/math.factorial(i))
        term = ((function_deriv.subs(x, a)*(h)**i)/math.factorial(i))
        taylor_expansion += term
        if term != 0:
            taylor_terms.append(term)
            taylor_polinomios.append(polinomio)


def nameLabel():
    list = []
    i = 0
    polinomio = 0
    for item in taylor_polinomios:
        polinomio+=item
        if i==0:
            list.append('Funcion original: ' + str(nsimplify(polinomio)))
        else:
             list.append('Polinomio de orden {}: '.format(i) + str(nsimplify(item)))
        i+=1
    return list


if __name__ == "__main__":
    polinomioDeTaylor()
    print('Funcion a evaluar: ' + str(nsimplify(function)))
    print('Valor aproximado: P(x) = {0:.9f} '.format(taylor_expansion))
    eje_x = np.array(range(-200, 400))*0.1
    eje_y = np.zeros(len(eje_x))
    j = 0
    list = nameLabel()
    for polinomio in taylor_polinomios:
        for i in range(len(eje_x)):
            eje_y[i] = sympify(polinomio).subs(x, eje_x[i])
        plt.plot(eje_x,eje_y, label=list[j], linewidth=2, color=list_colors[j])
        j+=1
    plt.title('Serie de Taylor sin(x)-x')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.legend()
    plt.grid()
    plt.show()












