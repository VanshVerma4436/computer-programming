# An application needs to find all prime numbers within a given range.
start = 10
end = 50
primes = []
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
print(primes)

