# Asyncio Communication Channels

##### What is a communication channel? What is its connection to async programming?
Logical connection between two or more network devices. Async is built primarily for swapping between tasks,
an optimal programming principle when handling networking

##### What are the two parts of the OSI model protocol layers? What purposes do each of them serve?
 - OS - Manages end user/server device, connections, etc. Can call to build and destroy connections, but 
 does not actually handle comm channels
 - Network - Responsible for actual data transfer. Physical cables, switches and MAC addresses, IP addresses,
 and Ports and protocols

##### What is the transport layer? why is it crucial to communciation channels?
Transport layer contains protocols for sending and receiving packets, consists primarily of TCP and UPD connections.
This layer is directly utilized by asyncio module

##### how does async facilitate the implementation of server side comm channels?
Server can asynchronously handle multiple clients simultaneously, switching between tasks to handle requests
as they arrive, even calling on lower level processes to handle part of the request (i.e. call slave server to compile
client requested data, move to another request, then return to orig request and send data to client)

##### How does async facilitate the implementation of client-side comm channels?
Similar to Server side, client can process HTTP connections as they return, parsing smaller responses while
awaiting the larger ones

##### What is aiofiles?


##Scripts
### 01.py
Simple Server. Receive connections, stdout received data. Tested with multiple telnet clients

### 02.py
