def add(*args):
    sum = 0
    for x in args:
        sum += x
    return (sum)


def calculate(n, **kwargs):
    print(kwargs)

