#Write a Function to Generate Fibonacci Series : You need to generate the first n terms of the Fibonacci series
def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

print(fibonacci(10)) 
