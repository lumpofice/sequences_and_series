import numpy as np


"""We will construct f(x) = cos(x) on [0, pi].
Then, we will output the domain and range
data to .table files that LaTeX will use to graph f."""


# Here is our function
f = lambda x: np.cos(x)


# Here is the domain of our function
xs = [
    np.arange(0, np.pi, 0.01)
    ]


# Here is how we use the domain and the function definition to generate our
# .table files for LaTeX
for i, j in enumerate(xs):
    with open('cos_0_pi_riemann_sum.table', 'w') as file:
        for x in j:
            if f(x) >= -1 and f(x) <= 1:
                file.write('{:f} {:f}\n'.format(x, f(x)))