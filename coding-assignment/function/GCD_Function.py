#Write a Function to Find the Greatest Common Divisor (GCD) : You need to find the GCD of two numbers.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(60, 48))  
