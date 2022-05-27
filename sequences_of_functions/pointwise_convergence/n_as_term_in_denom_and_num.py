import matplotlib.pyplot as plt
import numpy as np
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s'
    ' - %(message)s')
logging.getLogger('matplotlib.font_manager').disabled = True

logging.debug('Start of program' + f'\n')


def nx_over_one_plus_nx_squared():
    """This function plots each function $f_{n}(x)$, from a sequence of
functions \{f_{n}\}_{n=1}^{\infty}, each with a doman and codmain of real
numbers, from n=1 up to whatever value of n is required for the if conditional
to evaluate True. Once the if conditional evaluates True, the function stores
the number of natural numbers, n=K, for such an evaluation to be reached.
This sequence of functions converges pointwise to f=0, on (-\infty, \infty).
However, we observe convergence on the positive portion of the graph."""
    
    # We consider those scenarios when user input is not what we desire
    flag = True
    while flag:
        # We take care of those scenarios when user input is the return key
        x_input = input('Choose a real number x between 50 and 300,'
            ' or press the return key to quit: ')
        if not x_input:
            return 'Okay. Goodbye'
        
        # We take care of those scenarios when user input is non-numerical
        try:
            x = float(x_input)
            flag = False
        except ValueError:
            logging.debug('Really must type in a numerical value.' + f'\n')
            continue 
    
    # We consider those scenarios when user input is not what we desire
    flag = True
    while flag:
        # We take care of those scenarios when user input is the return key
        epsilon_input = input('Choose a small number epsilon, between 1/100000'
            ' and 1/100, or press the return key to quit: ')
        if not epsilon_input:
            return 'Okay. Goodbye'
        
        # We take care of those scenarios when user input is non-numerical
        try:
            epsilon = float(epsilon_input)
            flag = False
        except ValueError:
            logging.debug('Really must type in a numerical value.' + f'\n')
            continue
    
    
    # We take care of those scenarios when user input is out of specified range
    if x < 50 or x > 300:
        logging.debug(f'Your value x={x} is not in the requested'
            ' range' + f'\n')
        return 'Goodbye'
    
    # We take care of those scenarios when user input is out of specified range
    if epsilon < 1/100000 or epsilon > 1/100:
        logging.debug(f'Your value epsilon={epsilon} is not in the' 
            ' requested range' + f'\n')
        return 'Goodbye'
    
    # The statement below begins to assemble our figure
    fig, ax = plt.subplots(figsize=(15, 10))
    
    # Vector u is what defines our restricted domain of each function
    # with respect to x
    u = np.linspace(0, 300, 1000)
    
    # We initiate the index n with a value of 1 to simulate a
    # mathematical sequence
    n = 1
    
    # Vector v will serve as the range of our restricted domain defined by
    # vector u
    v = (n*u)/(1+(n*u)**2)
    
    # We plot this first vector pair u and v.
    ax.plot(u, v)
    
    flag = True
    while flag:
        if abs((n*x)/(1+(n*x)**2)) < epsilon:
            
            # Completing the plot
            ax.axvline(x=0, c='k')
            ax.axhline(y=0, c='k')
            ax.axhline(y=epsilon, c='k', label='epsilon')
            ax.axvline(x=x, c='c', label='x')
            plt.xlabel('Restricted Domain with respect to x', fontsize=20)
            plt.xticks(fontsize=10)
            plt.ylabel('Range of Restricted Domain',
                fontsize=20)
            plt.yticks(fontsize=10)
            plt.ylim(0, 0.02)
            plt.xlim(0, 300 + epsilon)
            fig.suptitle(r'$f_{n}(x) = \dfrac{nx}{1+(nx)^2}$', fontsize=20)
            plt.legend(prop={'size':20})
            plt.show()
            
            flag = False
        else:
            
            # We increase our index by 1
            n += 1
            
            # We keep the same restricted domain with vector u, but our
            # range with this new vector v will change, since n has changed
            v = (n*u)/(1+(n*u)**2)
            
            # We plot the next vector pair u and v in the same plot as the
            # preceding vector pairs
            ax.plot(u, v)
            
    return f'\nThe number of functions on the graph: {n}'
            

print(nx_over_one_plus_nx_squared())