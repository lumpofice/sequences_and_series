# Sequences and Series

## This is a respository with different sequences and series I have found useful or interesting through the years.


## Following are the function calls, in correspondance with the function's mathematical structure, to the python files within this repository:
### Note: All names for python functions that are pointwise convergent on larger domains and unformly convergent on attenuated domains have their uniformly convergent counterparts prefaced by a 'u_', while the pointwise convergent definition is not preface by any character. For example: ```nx_over_one_plus_nx()``` is the python function for the pointwise convergent counterpart, while ```u_nx_over_one_plus_nx()``` is the python function for the uniformly convergent counterpart. 

<b> Series
 - ```geo_series()``` &nbsp;&nbsp; $af(r)=\sum_{i=0}^{\infty}ar^i$ &nbsp;&nbsp; in &nbsp;&nbsp; geometric.py

<br/> 

<b> Sequences of Function
 - <b> Pointwise Convergence
 - ```x_over_x_plus_n()``` &nbsp;&nbsp; $f_{n}(x) = \dfrac{x}{x+n}$ &nbsp;&nbsp; in &nbsp;&nbsp; p_n_as_term_in_denom.py 

<br/>

 - ```nx_over_one_plus_nx_squared()``` &nbsp;&nbsp; $f_{n}(x) = \dfrac{nx}{1+(nx)^2}$ &nbsp;&nbsp; in &nbsp;&nbsp; p_n_as_term_in_denom_num.py

<br/>

 - ```nx_over_one_plus_nx()``` &nbsp;&nbsp; $f_{n}(x) = \dfrac{nx}{1+(nx)}$ &nbsp;&nbsp; in &nbsp;&nbsp; p_n_as_term_in_denom_num.py
 - <b> Uniform Convergence
 - ```x_plus_one_over_n()``` &nbsp;&nbsp; $f_{n}(x) = x + \dfrac{1}{n}$ &nbsp;&nbsp; in &nbsp;&nbsp; u_n_as_term_in_denom_num.py

<br/>

 - ```u_nx_over_one_plus_nx()``` &nbsp;&nbsp; $f_{n}(x) = \dfrac{nx}{1+nx}$ &nbsp;&nbsp; in &nbsp;&nbsp; u_n_as_term_in_denom_num.py

<br/>

 - ```u_x_over_x_plus_n()``` &nbsp;&nbsp; $f_{n}(x) = \dfrac{x}{x+n}$ &nbsp;&nbsp; in &nbsp;&nbsp; u_n_as_term_in_denom.py

<br/>

 - ```u_nx_over_one_plus_nx_squared()``` &nbsp;&nbsp; $f_{n}(x) = \dfrac{nx}{1+(nx)^2}$ &nbsp;&nbsp; in &nbsp;&nbsp; u_n_as_term_in_denom_num.py
