import os
from datetime import datetime


class TaskLogger:
    def __init__(self, path):
        self.path = path

    def log(self, message):
        """Logs a message with timestamp."""
        entry = f"{datetime.now().isoformat()} - {message}\n"
        with open(self.path, 'a') as f:
            f.write(entry)

    def read_logs(self):
        """Reads all log messages."""
        if not os.path.exists(self.path):
            return []
        with open(self.path, 'r') as f:
            return f.readlines()

def select_tasks(tasks, limit=3):
    """Select up to `limit` tasks."""
    return tasks[:min(len(tasks), limit)]

def execute_tasks(tasks, logger):
    """Executes tasks and logs their outcome."""
    for task in tasks:
        result = f"Task '{task}' executed."
        logger.log(result)
     logger.log(f"{len(tasks)} tasks executed in total.")

def summarize_logs(logger):
    """Prints a summary of executed tasks."""
    lines = logger.read_logs()
    print(f"Total log entries: {len(lines)}")
    for line in lines[-5:]:
        print(line.strip())

if __name__ == "__main__":
    logger = TaskLogger("tasklog.txt")
    tasks = [f"Job-{i}" for i in range(1, 8)]
    chosen = select_tasks(tasks, 5)
    execute_tasks(chosen, logger)
    summarize_logs(logger)