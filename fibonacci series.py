def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Get input from the user
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Generate Fibonacci sequence
fib_sequence = fibonacci(n)
print(fib_sequence)
