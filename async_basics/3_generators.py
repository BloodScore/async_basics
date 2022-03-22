def name_generator(name):
    for ch in name:
        yield ch


def num_generator(i):
    while True:
        yield i
        i += 1


def gen(n):
    for i in range(n):
        yield i


name_gen = name_generator('Dzmitry')
num_gen = num_generator(0)
gen = gen(4)


tasks = [name_gen, gen]

while tasks:
    task = tasks.pop(0)

    try:
        print(next(task))
        tasks.append(task)
    except StopIteration:
        pass
