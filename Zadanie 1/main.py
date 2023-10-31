import numpy as np

def f1(x):
    diff = 1
    n = Sn = g = 0
    calculation_counter = 52
    while diff >= 1e-10:
        g += np.sin(n * x * x * x * x) * np.sin(n * x * x * x * x) * np.exp(-n) + np.cos(
            n * x * x * x * x) * np.exp(-4 * n)
        diff = abs(Sn - g)
        n += 1
        Sn = g
        calculation_counter += 160
    text = f"Wynik f1 to {g:.10f} Dla N={n} przy ilości obliczeń={calculation_counter}"
    print(text)
    return Sn
f1(1)
