import numpy as np


"""We will construct f(x) = sin(x), piecewise, on
[0, 0.49] and [0.51, 1]. Then, we will output the domain and range
data to .table files that LaTeX will use to graph f."""
            

# Here is our function
f = lambda u: np.sin(u)


# Here is the domain of our function
xs = [
    np.arange(0, 0.49, 0.01),
    np.arange(0.51, 1, 0.01)
    ]


# Here is how we use the domain and the function definition to generate our
# .table files for LaTeX
for i, v in enumerate(xs):
    with open('sine_0_1_piece_{}.table'.format(i), 'w') as file:
        for u in v:
            if f(u) >= 0 and f(u) <= 1:
                file.write('{:f} {:f}\n'.format(u, f(u)))
                
                
