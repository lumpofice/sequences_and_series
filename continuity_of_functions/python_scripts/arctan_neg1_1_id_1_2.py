import numpy as np

"""We will construct f(x) = arctan(x), piecewise, on
[-1, -0.01) and (0.01, 1), and we will construct
g(x) = x on [1, 2].
Then, we will output the domain and range
data to .table files that LaTeX will use to graph f."""


# Here is our function
f = lambda u: np.arctan(u)
g = lambda v: v


# Here is the domain of our function
f_xs = [
    np.arange(-1, -0.01, 0.01),
    np.arange(0.01, 0.99, 0.01) 
    ]

g_xs = [
    np.arange(1, 2, 0.01)
    ]


# Here is how we use the domain and the function definition to generate our
# .table files for LaTeX
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