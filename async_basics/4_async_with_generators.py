import socket

from select import select


tasks = []

to_read = {}
to_write = {}


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        # print('Server before yield')
        yield 'read', server_socket
        # print('Server before .accept()')
        client_socket, address = server_socket.accept()
        print('Established connection from', address)
        tasks.append(client(client_socket))


def client(client_socket):
    while True:
        # print('Client before yield')
        yield 'read', client_socket
        # print('Client before .recv()')
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'Hello, world\n'.encode()
            yield 'write', client_socket
            client_socket.send(response)

    client_socket.close()


def event_loop():

    while any([tasks, to_read, to_write]):
        while not tasks:
            # print('no tasks')
            # print(tasks)
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])
            # print('after select')

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

            # print(tasks)

        try:
            # print('in try block')
            task = tasks.pop(0)
            reason, sock = next(task)
            # print(reason, sock)

            if reason == 'read':
                to_read[sock] = task
            elif reason == 'write':
                to_write[sock] = task

            # print(to_read)
            # print(to_write)
        except StopIteration:
            print('Done!')


if __name__ == '__main__':
    tasks.append(server())
    event_loop()
