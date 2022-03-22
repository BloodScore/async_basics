from inspect import getgeneratorstate


def message_generator(func):
    a = 'Hey ho'
    for _ in range(3):
        message = yield a
        print('Generator received message:', message)


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


@coroutine
def average_generator():
    count = 0
    sum_ = 0
    average = None

    while True:
        try:
            # x = yield average
            x = yield
        except StopIteration:
            print('Finished')
            break
        else:
            count += 1
            sum_ += x
            average = sum_ / count

    return average


# average_generator = coroutine(average_generator)
g = average_generator()
