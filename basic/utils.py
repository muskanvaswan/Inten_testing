#assignment 1 wih recursion

# function to find the power of a number
def power(number, exponent):
    if exponent==1:
        return number
    else:
        return (number * power(number, exponent-1))
# ends here ~ function to find the power of a number

# fucntion to solve mathematical expression
def calculate(x, n):
    if n == 1:
        return 1/x
    else:
        return ((1/power(x, n))+calculate(x, n-1))
# ends here ~ fucntion to solve mathematical expression
