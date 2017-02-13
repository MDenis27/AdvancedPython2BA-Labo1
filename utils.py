# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016
import math

def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    factorielle=1
    for x in range(n):
        factorielle*=n
        n-=1
    return factorielle

def roots(a, b, c):
    delta= (b**2-4*a*c)
    if delta > 0:
        return ((-b+math.sqrt(delta))/(2*a),(-b-math.sqrt(delta))/(2*a))
    if delta == 0:
        return (-b/(2*a))
    if delta < 0:
        return ()
        

def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    if function == 1:
        return(1)



if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))

