def fibonacci(n):
    # Initialize the first two terms of the series
    fib_series = [0, 1]
    
    # Generate subsequent terms of the series
    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    
    return fib_series

# Test the function
num_terms = int(input("Enter the number of terms for Fibonacci series: "))
if num_terms <= 0:
    print("Number of terms should be positive.")
else:
    fib_series = fibonacci(num_terms)
    print("Fibonacci series up to {} terms:".format(num_terms))
    print(fib_series)