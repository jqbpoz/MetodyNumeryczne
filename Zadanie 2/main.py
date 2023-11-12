import numpy as np
import math
import matplotlib.pyplot as plt


def func(x):
    return math.sin(x)


def DerivativeA(f, x, h):
    df = (f(x + h) - f(x)) / h
    return df


def DerivativeB(f, x, h):
    df = (f(x + h) - f(x - h)) / (2 * h)
    return df


def DerivativeC(f, x, h):
    df = (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)
    return df


def find_minimum_error(x, real_value):
    h_values = np.logspace(-16, 0, num=100)
    derivatives_A = [abs((DerivativeA(func, x, h) - real_value)) for h in h_values]
    derivatives_B = [abs((DerivativeB(func, x, h) - real_value)) for h in h_values]
    derivatives_C = [abs((DerivativeC(func, x, h) - real_value)) for h in h_values]

    min_value_A = min(derivatives_A)
    min_value_B = min(derivatives_B)
    min_value_C = min(derivatives_C)

    index_A = derivatives_A.index(min(derivatives_A))
    index_B = derivatives_B.index(min(derivatives_B))
    index_C = derivatives_C.index(min(derivatives_C))

    best_h_A = h_values[index_A]
    best_h_B = h_values[index_B]
    best_h_C = h_values[index_C]

    plt.plot(h_values, derivatives_A, label='DerivativeA')
    plt.plot(h_values, derivatives_B, label='DerivativeB')
    plt.plot(h_values, derivatives_C, label='DerivativeC')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('h')
    plt.ylabel('Błąd')
    plt.title('Wartość błędu obliczeniowego w zależności od h (~x={:.2f})'.format(x))
    plt.legend()
    plt.grid()
    plt.show()

    print("Minimalny błąd dla A wynosi", min_value_A, "gdzie h wynosi ", best_h_A)
    print("Minimalny błąd dla B wynosi", min_value_B, "gdzie h wynosi ", best_h_B)
    print("Minimalny błąd dla C wynosi", min_value_C, "gdzie h wynosi ", best_h_C)


x_values = [1.0, math.pi / 2]
real_values = [math.cos(x) for x in x_values]

for x, real_value in zip(x_values, real_values):
    find_minimum_error(x, real_value)

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
