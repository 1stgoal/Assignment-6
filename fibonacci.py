class Fibonacci:
    def __init__(self, n):
        if not isinstance(n, int) or n < 0:  # checks if the entered values are integer and not negative
            raise ValueError("only integer values to be entered")

