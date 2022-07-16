import numpy as np

f = lambda u: np.sin(u)
s1 = lambda w1:\
    ((6*np.sqrt(3)-6*np.sqrt(2))/(5*np.pi))*w1 +\
    ((8*np.sqrt(2)-3*np.sqrt(3))/10)
s2 = lambda w2:\
    ((4-(2*np.sqrt(2)))/(np.pi))*w2 + (np.sqrt(2)-1)
t = lambda v: (np.sqrt(2)/2)*v + (np.sqrt(2)/2)*((4-np.pi)/4)

f_s1_t_xs = [
    np.arange(0, np.pi, 0.01)
    ]

for i, j in enumerate(f_s1_t_xs):
    with open('sin_0_pi.table', 'w') as file:
        for u in j:
            if f(u) >= 0 and f(u) <= 1:
                file.write('{:f} {:f}\n'.format(u, f(u)))
    with open('secant1_0_pi.table', 'w') as file:
        for w1 in j:
            if s1(w1) >= 0 and s1(w1) <=1:
                file.write('{:f} {:f}\n'.format(w1, s1(w1)))
    with open('secant2_0_pi.table', 'w') as file:
        for w2 in j:
            if s2(w2) >= 0 and s2(w2) <= 2:
                file.write('{:f} {:f}\n'.format(w2, s2(w2)))
    with open('tangent_0_pi.table', 'w') as file:
        for v in j:
            if t(v) >= 0 and\
                t(v) <= (np.sqrt(2)/2)*(np.pi) + (np.sqrt(2)/2)*((4-np.pi)/4):
                file.write('{:f} {:f}\n'.format(v, t(v)))
                
