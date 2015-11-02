from concurrent.futures import ProcessPoolExecutor as Pool


def bar(n):
    yield from range(7)

b = bar(5)
