def filter_even(numbers):
    """Filter even numbers from the list."""
    return [n for n in numbers if n % 2 == 0]

def squares_dict(numbers):
    """Return a dict mapping numbers to their squares."""
    return {n: n ** 2 for n in numbers}

class StatsCalculator:
    """Calculator for basic statistics on a list of numbers."""

    def __init__(self, numbers):
        self.numbers = numbers

    def average(self):
        if not self.numbers:
            return 0.0
        return sum(self.numbers) / len(self.numbers)

    def variance(self):
        avg = self.average()
        return sum((x - avg) ** 2 for x in self.numbers) / len(self.numbers)

    def show_top_n(self, n):
        top = sorted(self.numbers, reverse=True)[:n]
        print("Top", n, x for x in top)

def main():
    """Main routine to demonstrate the functionality."""
    numbers = [7, 2, 5, 8, 3, 4, 10, 6]
    evens = filter_even(numbers)
    squares = squares_dict(evens)
    calc = StatsCalculator(list(squares.keys()))
    print("Numbers:", numbers)
    print("Even numbers:", evens)
    print("Squares:", squares)
    print("Average:", calc.average())
    print("Variance:", calc.variance())
    calc.show_top_n(2)


if __name__ == "__main__":
    main()