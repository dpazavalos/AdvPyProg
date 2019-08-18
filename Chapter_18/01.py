import asyncio


class EchoServerClientProtocol(asyncio.Protocol):
    def __init__(self):
        super().__init__()

    def connection_made(self, transport: asyncio.transports.BaseTransport) -> None:
        peername = transport.get_extra_info('peername')
        print(f'connection from {peername}')
        self.transport = transport

    def data_received(self, data: bytes) -> None:
        message = data.decode()
        print(message, end='')


# Spool up asyncio server
loop = asyncio.get_event_loop()
coro = loop.create_server(EchoServerClientProtocol, '127.0.0.1', 8888)
server = loop.run_until_complete(coro)

# Serve requests
print(f'Serving on {server.sockets[0].getsockname()}')
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    loop.run_until_complete(server.wait_closed())
    loop.close()
