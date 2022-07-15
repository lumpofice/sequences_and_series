import numpy as np

f = lambda u: np.sin(u)
g = lambda v: 0.66*v + 0.2

f_g_xs = [
    np.arange(0, np.pi/2, 0.01)
    ]

for i, j in enumerate(f_g_xs):
    with open('sin_0_pi_by2.table', 'w') as file:
        for u in j:
            if f(u) >= 0 and f(u) <= 1:
                file.write('{:f} {:f}\n'.format(u, f(u)))
    with open('linear_0_pi_by2.table', 'w') as file:
        for v in j:
            if g(v) >= 0 and g(v) <= np.pi/2:
                file.write('{:f} {:f}\n'.format(v, g(v)))
                
