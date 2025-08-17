from datetime import date, datetime


def days_difference(start_date=date.today(), end_date=None):
    """
    Calculate absolute day difference between two dates.
    """
    if end_date is None:
        end_date = date.today()
    return abs((end_date - start_date).days)

class ProjectDeadline:
    def __init__(self, deadline_str):
        self.deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()

    def remaining_days(self, current=None):
        """
        Returns the number of days left until the project deadline.
        """
        if current is None:
            current = date.today()
        return days_difference(start_date=current, self.deadline)

def main():
    """Main function to show example usage of ProjectDeadline."""
    project = ProjectDeadline("2025-12-20")
    print("Days until deadline:", project.remaining_days())


if __name__ == "__main__":
    main()