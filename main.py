from fibonacci import *
from factorial import *

n=20
assert fibonacci(n)==fibonacci_stack(n)

'''
print(f'Fib recursion of {n}: {fibonacci(n)}') 
print(f'Fib stack of {n}: {fibonacci_stack(n)}' )
'''

assert factorial(10) == factorial_stack(10)

