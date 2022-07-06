import numpy as np

"""We will construct f(x) = (x-1)/(x**2 - 1), piecewise, on
[-0.5, 0.99] and [1.01, 2]. Then, we will output the domain and range
data to .table files that LaTeX will use to graph f."""


# Here is our function
f = lambda u: (u - 1)/(u**2 - 1)


# Here is the domain of our function
xs = [
    np.arange(-1/2, 0.99, 0.01),
    np.arange(1.01, 2, 0.01)
    ]


# Here is how we use the domain and the function definition to generate our
# .table files for LaTeX
for i, j in enumerate(xs):
    with open('rational_neg1half_2_piece_{}.table'.format(i), 'w') as file:
        for u in j:
            if f(u) >= 1/3 and f(u) <= 2:
                file.write('{:f} {:f}\n'.format(u, f(u)))