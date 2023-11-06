def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        a, b = 0, 1  # Initialize a and b to the first two Fibonacci numbers
        for i in range(2, n):
            next_fib = a + b
            fib_sequence.append(next_fib)
            a, b = b, next_fib  # Update a and b for the next iteration
        return fib_sequence
    

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence


def fibonacci_step_count(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        steps = 2  # We start with 2 because the first two numbers are known (0 and 1).
        a, b = 0, 1
        for i in range(2, n):
            next_fib = a + b
            a, b = b, next_fib
            steps += 1
        return steps

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = fibonacci(n)
rec_fib_sequence = fibonacci_recursive(n)
step_count = fibonacci_step_count(n)



print("Fibonacci Sequence:")
print(fib_sequence)
print("\n")
print(rec_fib_sequence)
print("Step Count:", step_count)

# TIME COMPLEXITY FOR ITERATIVE = O(n)
# SPACE COMPLEXITY FOR ITERATIVE = O(1)


# TIME COMPLEXITY FOR ITERATIVE = O(2^n)
# SPACE COMPLEXITY FOR RECURSIVE = O(n) (due to the recursion stack)

