# Sequences and Series

Starting with the basics of calculus/analysis, the content within walks users through material, starting from sequences of real numbers. Precalculus concepts are assumed.


Following is a breakdown of the different directories and their contents. Relevant python scripts, jupyter files, python-generated tables, etc. can be located within separate directories within each section. Functions within the series and sequences_of_functions directories are broken down by function calls, in correspondance with the function's mathematical structure, contained within python files located in their respective directories.

## sequences_of_numbers
<b> sequences_of_numbers </b>
1. sequences_of_numbers.tex

## limits_of_functions
<b> limits_of_functions </b>
1. limits_of_functions.tex
2. python_scripts
    1. floor_0_2.py
    2. rational_neg1half_2.py
    3. sine_0_1_discontinuity.py
3. python_generated_tables
    1. floor_0_2_piece_0.table
    2. floor_0_2_piece_1.table
    3. rational_neg1half_2_piece_0.table
    4. rational_neg1half_2_piece_1.table
    5. sine_0_1_piece_0.table
    6. sine_0_1_piece_1.table
    
## continuity_of_functions
<b> continuity_of_functions </b>
1. continuity_of_functions.tex
2. python_scripts
    1. ceiling_neg1_1.py
    2. arctan_neg1_1_id_1_2.py
3. python_generated_tables
    1. arctan_neg1_1_piece_0.table
    2. arctan_neg1_1_piece_1.table
    3. ceiling_neg1_1_piece_0.table
    4. ceiling_neg1_1_piece_1.table
    5. id_1_2.table
    
## derivatives_of_functions
<b> derivatives_of_functions </b>
1. derivatives_of_functions.tex
2. python_scripts
    1. sin_0_pi_secants_tangent_0_pi.py
3. python_generated_tables
    1. sin_0_pi.table
    2. sin_0_pi_line_1.table
    3. sin_0_pi_line_2.table
    4. sin_0_pi_line_3.table
    5. sin_0_pi_line_4.table
    6. sin_0_pi_line_5.table
    7. sin_0_pi_line_6.table
    8. sin_0_pi_tangent.table

## series AND sequences_of_functions 
Note: Names for all <b><span style='color:#E63BD4'>python functions</span></b> that are pointwise convergent on their larger domains and uniformly convergent on appropriately attenuated domains have their uniformly convergent counterparts prefaced by a 'u', while the pointwise convergent definition is not prefaced by any character. For example: ```nx_over_one_plus_nx()``` is the python function for the pointwise convergent counterpart, while ```u_nx_over_one_plus_nx()``` is the python function for the uniformly convergent counterpart. All <b><span style='color:#E63BD4'>python files</span></b> containing pointwise convergent functions are prefaced with a 'p', and all python files containing uniformly convergent functions are prefaced with a 'u'. Of course, uniformly convergent functions are pointwise convergent, but name-wise, we try to keep the two separated.

<b> series </b>
1. series.tex
2. python_scripts
    1. ```geo_series()``` &nbsp;&nbsp; $af(r)=\sum ar^i$ &nbsp;&nbsp; in &nbsp;&nbsp; geometric.py
3. jupyter_files
    1. geometric.ipynb


<b> sequences_of_functions </b>
1. sequences_of_functions.tex
2. pointwise_convergence 
    1. python_scripts
        1. ```x_over_x_plus_n()``` &nbsp;&nbsp; $f_{n}(x) = \dfrac{x}{x+n}$ &nbsp;&nbsp; in &nbsp;&nbsp; p_n_as_term_in_denom.py 
        2. ```nx_over_one_plus_nx_squared()``` &nbsp;&nbsp; $f_{n}(x) = \dfrac{nx}{1+(nx)^2}$ &nbsp;&nbsp; in &nbsp;&nbsp; p_n_as_term_in_denom_num.py
        3. ```nx_over_one_plus_nx()``` &nbsp;&nbsp; $f_{n}(x) = \dfrac{nx}{1+(nx)}$ &nbsp;&nbsp; in &nbsp;&nbsp; p_n_as_term_in_denom_num.py
    2. jupyter_files
        1. p_n_as_term_in_denom.ipynb
        2. p_n_as_term_in_denom_num.ipynb
3. uniform_convergence
    1. python_scripts
        1. ```x_plus_one_over_n()``` &nbsp;&nbsp; $f_{n}(x) = x + \dfrac{1}{n}$ &nbsp;&nbsp; in &nbsp;&nbsp; u_n_as_term_in_denom_num.py
        2. ```u_nx_over_one_plus_nx()``` &nbsp;&nbsp; $f_{n}(x) = \dfrac{nx}{1+nx}$ &nbsp;&nbsp; in &nbsp;&nbsp; u_n_as_term_in_denom_num.py
        3. ```u_x_over_x_plus_n()``` &nbsp;&nbsp; $f_{n}(x) = \dfrac{x}{x+n}$ &nbsp;&nbsp; in &nbsp;&nbsp; u_n_as_term_in_denom.py
        4. ```u_nx_over_one_plus_nx_squared()``` &nbsp;&nbsp; $f_{n}(x) = \dfrac{nx}{1+(nx)^2}$ &nbsp;&nbsp; in &nbsp;&nbsp; u_n_as_term_in_denom_num.py
    2. jupyter_files
        1. u_n_as_term_in_denom.ipynb
        2. u_n_as_term_in_denom_num.ipynb

