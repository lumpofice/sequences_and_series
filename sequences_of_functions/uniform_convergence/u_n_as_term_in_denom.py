import matplotlib.pyplot as plt
import numpy as np
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s'
    ' - %(message)s')
logging.getLogger('matplotlib.font_manager').disabled = True


logging.debug('Start of program' + f'\n')


def u_x_over_x_plus_n():
    """This function plots each function $f_{n}(x)$, from a sequence of
functions \{f_{n}\}_{n=1}^{\infty}, each with a doman and codmain of real
numbers, from n=1 up to whatever value of n is required for the if conditional
to evaluate True. Once the if conditional evaluates True, the function stores
the number of natural numbers, n=K, for such an evaluation to be reached.
This sequence of functions converges uniformly to f=0, on [0, a],
where a>0"""
    
    
    # We kick off the program
    starter = True
    while starter:
        
        
        # We give users a choice of whether or not they wish to explore this
        # function with a natural number or an epsilon
        choose_k = input('We choose an arbitrarily'\
                ' small number based on natural number k.'\
                ' Press k for natural number k,'\
                ' or press return to escape the program: \n')
        
        
        if not choose_k:
            starter = False
            return 'Okay. Goodbye'
        
            
        if choose_k == 'k':
            starter = False
            
            
            # User input for a
            flag = True
            while flag:
                
                
                a_input = input('Choose a real number "a" between 1'\
                    ' and 100, or press the return key to quit: ')
                
                
                # We take care of those scenarios when user input is the return
                # key
                if not a_input:
                    return 'Okay. Goodbye'
                
                
                # We take care of those scenarios when user input is
                # non-numerical
                try:
                    a = float(a_input)
                    # When user input for a is out of specified range
                    if a < 1 or a > 100:
                        logging.debug(f'Your value a={a} is not in the'\
                            ' requested range' + f'\n')
                        continue
                    else:
                        flag = False
                except ValueError:
                    logging.debug('Really must type in a numerical value.'\
                        + f'\n')
                    continue
                
                
            # User input for x
            flag = True
            while flag:
                
                
                x_input = input('Choose a real number x between 0 and'\
                    ' "a", or press the return key to quit: ')
                
                
                # We take care of those scenarios when user input is the return
                # key
                if not x_input:
                    return 'Okay. Goodbye'
                
                
                # We take care of those scenarios when user input is
                # non-numerical
                try:
                    x = float(x_input)
                    # When user input for x is out of specified range
                    if x > a or x < 0:
                        logging.debug(f'Your value x={x} is not in the'\
                            ' requested range' + f'\n')
                        continue
                    else:
                        flag = False
                except ValueError:
                    logging.debug('Really must type in a numerical value.'\
                        + f'\n')
                    continue 
            
            
            # User input for k
            flag = True
            while flag:
                
                
                k_input = input('Choose a large natural number k, between 100' 
                    ' and 1000, or press the return key to quit: ')
                
                
                # We take care of those scenarios when user input is the return
                # key
                if not k_input:
                    return 'Okay. Goodbye'
                
                
                # We take care of those scenarios when user input is
                # non-numerical
                try:
                    k = float(k_input)
                    # When user input for k is out of specified range
                    if k < 100 or k > 1000:
                        logging.debug(f'Your value k={k} is not in the' 
                            ' requested range' + f'\n')
                        continue
                    else:
                        flag = False
                except ValueError:
                    logging.debug('Really must type in a numerical value.'\
                        + f'\n')
                    continue
            
            
            # The statement below begins to assemble our figure
            fig, ax = plt.subplots(figsize=(15, 10))
            
            
            # Vector u is what defines our restricted domain of each function
            # with respect to x
            u = np.linspace(0, 101, 1000)
            
            
            # We initiate the index n with a value of 1 to simulate a
            # mathematical sequence
            n = 1
            
            
            # Vector v will serve as the range of our restricted domain defined
            # by vector u
            v = u/(n+u)
            
            
            # We plot this first vector pair u and v, as well as the 
            # absolute value of the difference of f_n(x)-f(x), where f_n(x) is 
            # the function from our sequence at n=1 and f(x) is the function to 
            # which the sequence of functions uniformly converges.
            ax.plot(u, v)
            ax.scatter(x, x/(n+x),\
                label=r'$| f_n(x) - f(x) |$')
            
            
            flag = True
            while flag:
                
                
                if abs(x/(n+x)) < a/k:
                    # Completing the plot
                    ax.axvline(x=0, c='k')
                    ax.axhline(y=0, c='k')
                    ax.axhline(y=a/k, c='k', label=r'$\dfrac{a}{k}$')
                    plt.xlabel('Restricted Domain with respect to x',\
                        fontsize=20)
                    plt.xticks(fontsize=10)
                    plt.ylabel('Range of Restricted Domain',\
                        fontsize=20)
                    plt.yticks(fontsize=10)
                    plt.ylim(0, 1.02)
                    plt.xlim(0, 101)
                    fig.suptitle(r'$f_{n}(x) = \dfrac{x}{n+x}$', fontsize=20)
                    plt.legend(prop={'size':20})
                    plt.show()
                    
                    
                    flag = False
                    
                    
                else:
                    # We increase our index by 1
                    n += 1


                    
                    # We keep the same restricted domain with vector u, but our
                    # range with this new vector v will change, since n has
                    # changed
                    v = u/(n+u)
                    
                    
                    # We plot the next vector pair u and v in the same plot as 
                    # the preceding vector pairs, as well as the absolute value 
                    # of the difference of f_n(x)-f(x), where f_n(x) is the
                    # function from our sequence at n=k and f(x) is the function 
                    # to which the sequence of functions uniformly converges.
                    ax.plot(u, v)
                    ax.scatter(x, x/(n+x))
                    
                    
            return f'The number of functions on the graph: {n}'
        
        
        else:
            continue
            

u_x_over_x_plus_n()