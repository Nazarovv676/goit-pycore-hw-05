def caching_fibonacci():
    """Caching decorator function for Fibonacci sequence.

    Returns a function that computes the nth Fibonacci number using memoization
    to optimize repeated calculations.
    """
    cache = dict()  # Dictionary to store previously computed Fibonacci numbers

    def fibonacci(n):
        """Compute the nth Fibonacci number.

        Args:
            n (int): The position in the Fibonacci sequence.

        Returns:
            int: The nth Fibonacci number.

        Uses memoization to avoid redundant calculations.
        """
        nonlocal cache  # Access the cache from the outer function

        # Base cases
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # Return cached result if available
        if n in cache:
            return cache[n]

        # Compute the value and store it in the cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci  # Return the inner function


# Create a cached Fibonacci function
fibonacci = caching_fibonacci()

# Test the function
print(fibonacci(10))  # Output: 55
print(fibonacci(15))  # Output: 610
