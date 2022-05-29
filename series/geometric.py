import matplotlib.pyplot as plt
import numpy as np
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s'
    ' - %(message)s')
logging.getLogger('matplotlib.font_manager').disabled = True

logging.debug('Start of program' + f'\n')

def geo_series():
    """This geometric series follows the definition
    seen in the legend, where a and r are constants and abs(r) < 1.
    Choose your epsilon small enough to ensure accuracy of the sum of the 
    series"""
    
    # Taking in and checking user input for the scalar a.
    flag = True
    while flag:
        a_input = input('Choose a real number, or press return to exit'
            ' program: ')
        
        # If user wishes to exit program
        if not a_input:
            return 'No Problem, Goodbye'
        
        # We check if input is a numerical 
        try:
            a = float(a_input)
            flag = False
        except ValueError:
            logging.debug('Need a numerical input here' + f'\n')
            continue
    
    # Taking in and checking user input for the base r.
    flag = True
    while flag:
        r_input = input('Choose a base with an absolute value less than one,'
            ' or press return to exit program: ')
        
        # If user wishes to exit program
        if not r_input:
            return 'No Problem, Goodbye'
        
        # We check if input is a numerical holding under specified conditions
        try:
            r = float(r_input)
            if abs(r) >= 1:
                logging.debug('We need a base with an absolute value less'
                    ' than 1')
            else:
                flag = False
        except ValueError:
            logging.debug('Really must provide a numerical response' + f'\n')
            continue
    
    # Taking in and checking user input for the epsilon.
    flag = True
    while flag:
        epsilon_input = input('Choose an epsilon greater than 0, or press'
            ' return to exit program: ')
        
        # If user wishes to exit program
        if not epsilon_input:
            return 'No Problem. Goodbye'
        
        # We check if input is a numerical holding under specified conditions
        try:
            epsilon = float(epsilon_input)
            if epsilon <= 0:
                logging.debug('We need an epsilon with value greater'
                    ' than 0')
            else:
                flag = False
        except ValueError:
            logging.debug('Really must provide a numerical response' + f'\n')
            continue
    
    # Taking in and checking user input for the m.
    flag = True
    while flag:
        m_input = input('Choose a positive integer as m, or press'
            ' return to exit program: ')
        
        # If user wishes to exit program
        if not m_input:
            return 'No Problem. Goodbye'
        
        # We check if input is a numerical holding under specified conditions
        try:
            m = int(m_input)
            if m <= 0:
                logging.debug('We need a m with value greater'
                    ' than 0')
            else:
                flag = False
        except ValueError:
            logging.debug('Really must provide a numerical response' + f'\n')
            continue
    
    # We will plot the powers list as our domain, and we will plot the results
    # list as our range
    results = []
    powers = []
    
    # We initiate the power variable at 0
    power = 0
    powers.append(power)
    
    # We initiate the result variable at 0, for the purposes of initiating
    # the absolute value of difference of two adjacent result terms, as
    # seen below in the while loop
    prev_result = 0
    
    # Since we do not wish to plot a value of 0, we omit this entry from
    # our graph
    results.append(np.nan)
    
    # This loop will fill our powers and results lists until the if conditional
    # within evaluates to True
    flag = True
    while flag:
        curr_result = a*r**(power)
        if power!=0 and power%m==0:
            if abs(sum(results[power-m:power-1])) < epsilon:
                flag = False
                continue
        results.append(curr_result)
        prev_result = curr_result
        power += 1
        powers.append(power)
        
    # The statements below will plot the powers and results list that we have
    # from the above while loop, completing the graph of our function
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.scatter(powers, results, label=r'$af(r)=\sum_{i=0}^{\infty}ar^i$')
    plt.xlabel('Integer Powers', fontsize=20)
    plt.ylabel('Sequence Value', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    fig.suptitle('Geometric Series', fontsize=20)
    plt.legend(prop={'size': 20})
    plt.show()
    
    return f'Nice work. Your program require n = {power} before reaching'\
        ' convergence for the epsilon you specified.'

print(geo_series())