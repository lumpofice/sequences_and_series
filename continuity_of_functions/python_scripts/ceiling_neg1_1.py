import numpy as np

"""We will construct f(x) = ceiling(x), piecewise, on
[-1, -0.01] and [0.01, 1]. Then, we will output the domain and range
data to .table files that LaTeX will use to graph f."""


# Here is our function
f = lambda u: np.ceil(u)


# Here is the domain of our function
xs = [
    np.arange(-1, -0.01, 0.01),
    np.arange(0.01, 1, 0.01)
    ]


# Here is how we use the domain and the function definition to generate our
# .table files for LaTeX
for i, j in enumerate(xs):
    with open('ceiling_neg1_1_piece_{}.table'.format(i), 'w') as file:
        for u in j:
            if f(u) >= 0 and f(u) <= 1:
                file.write('{:f} {:f}\n'.format(u, f(u)))