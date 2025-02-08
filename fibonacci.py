def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# Test the function
if __name__ == "__main__":
    print(fib(5))  # This will print the Fibonacci number for 5
