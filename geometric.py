import matplotlib.pyplot as plt
import numpy as np

def series(a, r, epsilon):
    """This geometric series follows the definition
    seen in the legend, where a and r are constants and abs(r) < 1.
    Choose your epsilon small enough to ensure accuracy of the sum of the 
    series"""
    results = []
    powers = []
    power = 0
    powers.append(power)
    prev_result = 0
    results.append(np.nan)
    flag = True
    while flag:
        curr_result = a*r**(power)
        if abs(prev_result - curr_result) < epsilon:
            flag = False
        results.append(curr_result)
        prev_result = curr_result
        power += 1
        powers.append(power)
    return powers, results

powers, terms = series(float(input('Choose a scalar: ')), 
                       float(input('Choose a base: ')), 
                       float(input('Choose an epsilon: ')))
fig, ax = plt.subplots(figsize=(15, 10))
ax.plot(powers, terms, label=r'$af(r)=\sum_{i=0}^{\infty}ar^i$')
plt.xlabel('Integer Powers', fontsize=20)
plt.ylabel('Sequence Value', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
fig.suptitle('Geometric Series', fontsize=20)
plt.legend(prop={'size': 20})
plt.show()