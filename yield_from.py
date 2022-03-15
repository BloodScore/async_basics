from inspect import getgeneratorstate


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
    message = yield from g
    print(message)
