def series(a, r, epsilon):
    """This geometric series follows the definition
    f(n) = sum_{i=0}^{\infty}(a*r**i), where a, r are constants and abs(r) < 1
    Choose your epsilon small enough to ensure accuracy of the value of the 
    series"""
    results = []
    power = 0
    prev_result = 0
    flag = True
    while flag:
        curr_result = a*r**(power)
        if abs(prev_result - curr_result) < epsilon:
            flag = False
        results.append(curr_result)
        prev_result = curr_result
        power += 1
    return sum(results)