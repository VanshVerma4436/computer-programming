#Write a Function to Find All Divisors of a Number : You need to find all the divisors of a given number.
def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

print(find_divisors(12))  
