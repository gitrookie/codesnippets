from collections import deque


def countdown(n):
    for i in range(n):
        yield n
        n -= 1

tasks = deque()
tasks.extend([countdown(10), countdown(5), countdown(7)])


def run():
    while tasks:
        task = tasks.popleft()
        try:
            x = next(task)
            print(x)
            tasks.append(task)
        except StopIteration:
            print("Task")
run()
print(tasks)
