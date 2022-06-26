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
            logging.debug('Need a numerical input here')
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
            logging.debug('Really must provide a numerical response')
            continue
        
    
    # Taking in and checking user input for the epsilon.
    flag = True
    while flag:
        epsilon_input = input('Choose an epsilon greater than 1/1000000,'\
            ' in decimal form, or press'
            ' return to exit program: ')
        
        
        # If user wishes to exit program
        if not epsilon_input:
            return 'No Problem. Goodbye'
        
        
        # We check if input is a numerical holding under specified conditions
        try:
            epsilon = float(epsilon_input)
            if epsilon < 1/1000000:
                logging.debug('The epsilon you chose is not in the specified'\
                ' range')
            else:
                flag = False
        except ValueError:
            logging.debug('Really must provide a numerical response')
            continue
    
    
    # Taking in and checking user input for the m, which is the number of terms
    # the user wishes to sum together, comparing this sum to the chosen epsilon.
    flag = True
    while flag:
        m_input = input('Choose a positive integer, no greater than 30000,'\
            ' of terms whose sum you wish'\
            ' to compare with the epsilon you have chosen, or press'
            ' return to exit program: ')
        
        
        # If user wishes to exit program
        if not m_input:
            return 'No Problem. Goodbye'
        
        
        # We check if input is a numerical holding under specified conditions
        try:
            m = int(m_input)
            if m <= 0 or m > 30000:
                logging.debug('The m you chose is not in the specified range')
            else:
                flag = False
        except ValueError:
            logging.debug('Really must provide a numerical response')
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
    # within evaluates to True.
    # The conditions in the first if statement below are not
    # a set of conditions necessary for the mathematical function,
    # but rather a set of conditions necessary to accomodate the author's
    # inability to produce an alternative for comparing a sum of the function's
    # terms with the chosen epsilon.
    # --------------------------------------------------------------------------
    # Example to motivate the first if statement:
    # if power!=0 and power-m!=0 and 'power%m==0'
    # Let m=10 and power=20.
    # if 20 is not 0 (check)
    # and if 20 minus 10 is not 0 (check)
    # and if 20 in base 10 is 0 (check)
    # --------------------------------------------------------------------------
    flag = True
    while flag:
        curr_result = a*r**(power)
        if power!=0 and power-m!=0 and power%m==0:
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
    
    
    return f'Nice work. Your program requires n = {power} before reaching'\
        f' convergence to the sum {sum(results[1:])} for the epsilon'\
        ' you specified.'


geo_series()