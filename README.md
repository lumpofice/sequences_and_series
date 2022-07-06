# Sequences and Series

## This is a repository for anyone who wishes to student calculus concepts.


## Following is a breakdown of the different directories and their contents. Relevant python scripts, jupyter files, python-generated tables, etc. can be located within separate directories within each section. Functions within the series and sequences sections are broken down by function calls, in correspondance with the function's mathematical structure, to the python files within this repository.

### Note: Names for all python functions that are pointwise convergent on their larger domains and uniformly convergent on appropriately attenuated domains have their uniformly convergent counterparts prefaced by a 'u', while the pointwise convergent definition is not prefaced by any character. For example: ```nx_over_one_plus_nx()``` is the python function for the pointwise convergent counterpart, while ```u_nx_over_one_plus_nx()``` is the python function for the uniformly convergent counterpart. All python files containing pointwise convergent functions are prefaced with a 'p', and all python files containing uniformly convergent functions are prefaced with a 'u'. Of course, uniformly convergent functions are pointwise convergent, but name-wise, we try to keep the two separated.

<b> series </b>
1. ```geo_series()``` &nbsp;&nbsp; $af(r)=\sum ar^i$ &nbsp;&nbsp; in &nbsp;&nbsp; geometric.py

<br/> 

<b> sequences_of_functions </b>
1. <b> pointwise_convergence </b>
	1. ```x_over_x_plus_n()``` &nbsp;&nbsp; $f_{n}(x) = \dfrac{x}{x+n}$ &nbsp;&nbsp; in &nbsp;&nbsp; p_n_as_term_in_denom.py 
	2. ```nx_over_one_plus_nx_squared()``` &nbsp;&nbsp; $f_{n}(x) = \dfrac{nx}{1+(nx)^2}$ &nbsp;&nbsp; in &nbsp;&nbsp; p_n_as_term_in_denom_num.py
	3. ```nx_over_one_plus_nx()``` &nbsp;&nbsp; $f_{n}(x) = \dfrac{nx}{1+(nx)}$ &nbsp;&nbsp; in &nbsp;&nbsp; p_n_as_term_in_denom_num.py

<br/>

2. <b> uniform_convergence </b>
	1. ```x_plus_one_over_n()``` &nbsp;&nbsp; $f_{n}(x) = x + \dfrac{1}{n}$ &nbsp;&nbsp; in &nbsp;&nbsp; u_n_as_term_in_denom_num.py
	2. ```u_nx_over_one_plus_nx()``` &nbsp;&nbsp; $f_{n}(x) = \dfrac{nx}{1+nx}$ &nbsp;&nbsp; in &nbsp;&nbsp; u_n_as_term_in_denom_num.py
	3. ```u_x_over_x_plus_n()``` &nbsp;&nbsp; $f_{n}(x) = \dfrac{x}{x+n}$ &nbsp;&nbsp; in &nbsp;&nbsp; u_n_as_term_in_denom.py
	4. ```u_nx_over_one_plus_nx_squared()``` &nbsp;&nbsp; $f_{n}(x) = \dfrac{nx}{1+(nx)^2}$ &nbsp;&nbsp; in &nbsp;&nbsp; u_n_as_term_in_denom_num.py

