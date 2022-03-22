import time

from inspect import getgeneratorstate


""" sub_generator and delegating generator (not coroutine) """
# def sub_generator(string):
#     for i in string:
#         yield i
#
#
# def delegator(g):
#     for i in g('Dzmitry'):
#         yield i


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


# @coroutine
def sub_generator():
    while True:
        try:
            message = yield
        except StopIteration:
            print('Raised exception in sub_generator')
            break
        else:
            print(message)

    return 'sub_generator finished'


# @coroutine
# def delegator(g):
#     while True:
#         try:
#             print('iteration of delegator')
#             data = yield
#             g.send(data)
#         except StopIteration:
#             try:
#                 g.throw(StopIteration)
#             except StopIteration as e:
#                 print('AHAHAHAHHA', e)
#         else:
#             print('Data passed')


""" The same with previous thanks to 'yield from' """
""" Functionality of eternal cycle and g.send/throw """
@coroutine
def delegator(g):
    try:
        print('iteration of delegator')  # не печатается
        message = yield from g
        # print('HAHAHAHHA')
        print('Message:', message)
    except StopIteration:
        print('Handled StopIteration in delegator')


""" yield from can yield from any iterable object """
def gen(string):
    yield from string
