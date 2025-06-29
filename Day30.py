# Recursion in Python 

# As we know how to calculate the factorial of a number 

# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(3) = 3*2*1
# factorial(2) = 2*1
# factorial(1) = 1
# factorial(0) = 1


# Recursion is defining something in term of itself


def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

# print(factorial(5))



# fibonacci sequence 

# f0 = 0
# f1 = 1
# f2 = f0 + f1
# fn = f(n-1) + f(n-2)



def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(3))