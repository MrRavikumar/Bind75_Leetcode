# Sum of first N Numbers using Parameterized Recursion
print('Sum of first N Numbers using Parameterized Recursion')
def sumOfFirstNNumbers(n, sum):
    if n < 1:
        print(sum)
        return
    sumOfFirstNNumbers(n-1, sum+n)

sumOfFirstNNumbers(5, 0)

# Sum of first N Numbers using Functional Recursion
print('\nSum of first N Numbers using Functional Recursion')
def sumOfFirstNNumbersFunctionalRecursion(n):
    if n == 0:
        return 0
    return n + sumOfFirstNNumbersFunctionalRecursion(n-1)

print(sumOfFirstNNumbersFunctionalRecursion(5))

# Factorial of a Number using Parameterized Recursion
print('\nFactorial of a Number using Parameterized Recursion')
def factorialParameterizedRecursion(n, fact):
    if n < 1:
        print(fact)
        return
    factorialParameterizedRecursion(n-1, fact*n)

factorialParameterizedRecursion(5, 1)

# Factorial of a Number using Functional Recursion
print('\nFactorial of a Number using Functional Recursion')
def factorialFunctionalRecursion(n):
    if n == 1:
        return 1
    return n * factorialFunctionalRecursion(n-1)

print(factorialFunctionalRecursion(5))
