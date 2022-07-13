import numpy as np

f = lambda u: np.arctan(u)
g = lambda v: v

f_xs = [
    np.arange(-1, -0.01, 0.01),
    np.arange(0.01, 0.99, 0.01) 
    ]

g_xs = [
    np.arange(1, 2, 0.01)
    ]

for i, j in enumerate(f_xs):
    with open('arctan_neg1_1_piece_{}.table'.format(i), 'w') as file:
        for u in j:
            if f(u) >= -np.pi/4 and f(u) < np.pi/4:
                file.write('{:f} {:f}\n'.format(u, f(u)))

for s, t in enumerate(g_xs):
    with open('id_1_2.table', 'w') as file:
        for v in t:
            if g(v) >= 1 and g(v) <= 2:
                file.write('{:f} {:f}\n'.format(v, g(v)))