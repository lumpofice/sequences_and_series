import numpy as np
import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt


x = np.linspace(0,0.49,5000)
y = np.sin(x)
u = np.linspace(0.51, 1, 5000)
v = np.sin(u)


fig, ax = plt.subplots(figsize=(15,10))
ax.plot(x, y, c='b')
ax.plot(u, v, c='b')
circle = plt.Circle((0.5, np.sin(0.5)), 0.01, fill=False)
ax.set_aspect(1)
ax.add_artist(circle)
plt.xlabel('Domain', fontsize=20)
plt.ylabel('Range', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlim(0, 1)
plt.ylim(0,1)
fig.suptitle('$f(x)=\sin(x)$, ' + ' ' + ' $x \in [0,0.5)\cup(0.5,1]$', fontsize=20)
plt.savefig('sine_nondomain_limit.pgf', format='pgf')
