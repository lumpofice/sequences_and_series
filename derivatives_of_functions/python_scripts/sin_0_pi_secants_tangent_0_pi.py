import numpy as np

"""We will construct several functions, one of which will be the primative,
the rest of which will be secant and tangent lines to the primative at
a specific point."""

#-------------------------------------------------------------------------------
# The sine function g(x) = sin(x) from [0, pi]
# 1) function
g = lambda v: np.sin(v)
# 2) domain
g_xs = [
    np.arange(0, np.pi, 0.01)
    ]
# 3) generated data table
with open('sin_0_pi.table', 'w') as file:
    for v in g_xs[0]:
        if g(v) >= 0 and g(v) <= 1:
            file.write('{:f} {:f}\n'.format(v, g(v)))


#-------------------------------------------------------------------------------
# A set of secant lines at the point (pi/4, sqrt(2)/2).


# The following will generate four secant lines.
for n in range(1, 5):
    # 1) slope
    m = (np.sin((np.pi/4) + (1/n)) - np.sin(np.pi/4))/(1/n)
    # 2) intercept
    b = np.sin(np.pi/4) - m*(np.pi/4)
    # 3) function
    f = lambda u: m*u + b
    # 4) domain 
    f_xs = [
        np.arange(0, np.pi, 0.01)
        ]
    # 5) generated data table
    with open('sin_0_pi_line_{}.table'.format(n), 'w') as file:
        for u in f_xs[0]:
            if f(u) >= 0 and f(u) <= 3:
                file.write('{:f} {:f}\n'.format(u, f(u)))
        

#-------------------------------------------------------------------------------
# Another set of secant lines at the point (pi/4, sqrt(2)/2).


# First line
# 1) slope
m = (np.sin(2*np.pi/3) - np.sin(np.pi/4))/(5*np.pi/12)
# 2) intercept
b = np.sin(np.pi/4) - m*(np.pi/4) 
# 3) function
s = lambda x: m*x + b
# 4) domain
s_xs = [
    np.arange(0, np.pi, 0.01)
    ]
# 5) generated data table
with open('sin_0_pi_line_5.table', 'w') as file:
    for x in s_xs[0]:
        if s(x) >= 0 and s(x) <= 3:
            file.write('{:f} {:f}\n'.format(x, s(x)))
            
            
# Second line
# 1) slope
m = (np.sin(np.pi/2) - np.sin(np.pi/4))/(np.pi/4)
# 2) intercept
b = np.sin(np.pi/4) - m*(np.pi/4) 
# 3) function
w = lambda y: m*y + b
# 4) domain
w_xs = [
    np.arange(0, np.pi, 0.01)
    ]
# 5) generated data table
with open('sin_0_pi_line_6.table', 'w') as file:
    for y in w_xs[0]:
        if w(y) >= 0 and w(y) <= 3:
            file.write('{:f} {:f}\n'.format(y, w(y)))
            

#-------------------------------------------------------------------------------
# The tangent line at the point (pi/4, sqrt(2)/2).
# 1) slope
m = np.sin(np.pi/4)
# 2) intercept
b = np.sin(np.pi/4) - m*(np.pi/4) 
# 3) function
t = lambda z: m*z + b
# 4) domain
t_xs = [
    np.arange(0, np.pi, 0.01)
    ]
# 5) generated data table
with open('sin_0_pi_tangent.table', 'w') as file:
    for z in t_xs[0]:
        if t(z) >= 0 and t(z) <= 3:
            file.write('{:f} {:f}\n'.format(z, t(z)))