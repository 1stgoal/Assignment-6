class Fibonacci:
    def __init__(self, n):
        if not isinstance(n, int):  # checks if the entered values are integer
            raise ValueError("only integer values to be entered")

        """Creating variables"""
        self.n = n
        self.a = 0
        self.b = 1
        self.count = 0

    """Returns iterable object"""

    def __iter__(self):
        return self

    """Generates the next Fibonacci number. Stops iteration when the 
        sequence ends or if initialized with a negative value."""

    def __next__(self):
        if self.count > self.n or self.n < 0:
            raise StopIteration

        fib_number = self.a
        c = self.a + self.b
        self.a = self.b
        self.b = c
        self.count += 1
        return fib_number
