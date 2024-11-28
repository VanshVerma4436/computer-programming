#Write a Function to Calculate the Factorial of a Number : You need to find the factorial of a given number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) 
