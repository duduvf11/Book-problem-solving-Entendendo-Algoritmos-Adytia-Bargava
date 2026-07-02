#Binary search formula: log2(n) == number of steps

import math

def binary_search_steps_counter(n):
    if n > 0:
        steps = math.ceil(math.log2(n))
        return steps
    else:
        return "List length have to be bigger than 0."
    
print(binary_search_steps_counter(128)) #resolves exercise 1.1
print(binary_search_steps_counter(256)) #resolves exercise 1.2