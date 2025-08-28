def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Example usage
n = int(input("Enter number of terms: "))
print("Fibonacci series up to", n, "terms:")
fibonacci(n)
