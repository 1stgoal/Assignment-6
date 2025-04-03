class Fibonacci:
    def __init__(self, n):
        if not isinstance(n, int) or n < 0:  # checks if the entered values are integer and not negative
            raise ValueError("only integer values to be entered")

        """Creating variables"""
        self.n = n
        self.a = 0
        self.b = 1
        self.count = 0

    """Returns iterable object"""

    def __iter__(self):
        return self

    """Generates the next Fibonacci number and raises StopIteration when the sequence ends."""

    def __next__(self):
        if self.count > self.n:
            raise StopIteration

        fib_number = self.a
        c = self.a + self.b
        self.a = self.b
        self.b = c
        self.count += 1
        return fib_number
