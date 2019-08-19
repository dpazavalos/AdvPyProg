# Intro to Async Programming

## Chapter 16
##### what is the idea behind asynchronous programming?
Async resolves around task switching, especially in regards to scenarios where one task requires excessive wait time. Can also be used to do quickly finish short tasks 

##### how is Async programming different from synchronous programming?
Synchronous, or sequential, tackles tasks as they are written. Async can swap between
tasks

##### How is async different from threading and multiprocessing?
Threading and multiprocessing create multiple copies of running code, able to execute in 
a parallel and partitioned fashion. Async operates in one instance, sharing resources and data

## Chapter 17 
##### What is Async programming? What advantages?
Allows switching between tasks and functions, via event loops and 
dedicated async functions

##### What are the main elements in an asynchronous program? How do they interact?
- Event Loops - handles all tasks to be run asynchronously. Is responsible for task swap
- Coroutines - tasks handled by event loops. Basically async function wrappers
- Futures - placeholders for results returned by coroutines

##### What are async and await? What purpose do they serve?
- async - async def func(): creats an async function
- await - releases control to Event loop (allow loop to swap tasks)

##### What options does asyncio provide, in terms of implementing async programming?
- asyncio.get_event_loop() - provides a new AbstractEventLoop, to handle coroutines.
(Note that asyncio has a 'global' loop that can be used)
- AbstractEventLoop.create_task() - Inputs a coroutine to add to event loop task list
- AbstractEventLoop.run_until_complete() - Called by loop. Executes until future is returned. 
                        No other code can run until loop is complete and future returned
- AbstractEventLoop.run_forever - Like run_until_complete, but will only close loop on explicit .stop() Good for servers
- AbstractEventLoop.stop() - Safely stop event loop at next available await. 
- AbstractEventLoop.sleep() - a coroutine used to cause immediate task switch event
- AbstractEventLoop.wait() - Takes a list of futures and awaits their execution (sub-coroutines)
                        
##### what are the improvements in regards to asynchronous programming provided in 3.7?
- async/await are reserved keywords
- Asyncio now has a .run() to simplify boilerplate (rather than adding to an AbstractEventLoop obj, call .run() and add to Asyncio
Perf improvement

##### What are blocking functions? Why do they pose a problem for traditional async?
Tasks that prevent any Event Loop switching (read data, Stdin, large math, etc)
Async will usually offer worse performance when blocking functions exist. Consider concurrent.futures.ThreadPoolExecutor or .ProcessPoolExecutor

##### How does concurrent.futures provide solution to blocking functions for async? Options?
High level interface for async functions. Allows handling regular functions rather than coroutines, via multithreading or processing
If crunching numbers (high blocking) consider Executor

## Scripts
### 01.py
Asynchronous Prime finder, checking if numbers 9_637_529_763_296_797, 427_920_331, and 157 are prime via 
incrementation.

Typically 10 seconds execution. Minimal task swapping available, as all work is raw number crunching

### 02.py
Async stdout printer showing blocking effects (using time.sleep), and how to work around it via asyncio.sleep(0)

### 03.py
Asynchronous Prime finder. 
When crunching large numbers to find prime, incorporated asyncio.sleep(0) every 1_000_000 numbers, to
try and increase responsiveness (i.e. if task is taking a while, try swapping to another one)

Since 9_637_529_763_296_797 is so large, Event Loop switched to other tasks (The 400 mil and 157).
Since these are smaller, they displayed on screen quickly, HOWEVER: The .sleep() coroutine slowed
overall run time to TWENTY SECONDS

### 04.py
Reproduction of 02, but utilizing a ThreadPoolExecutor with dedicated workers for each task

Overall run time was equivalent to the 02.py version with incorporated asyncio API calls, however
this version required much simpler functions (i.e. Executor boilerplate handled threading, allowing simpler function
writup)

### 05.py
Utilize ThreadPoolExecutor again, this time on 01.py's Prime finder. As functions were no longer async, allowed more
intuitive creation. Along with the removal of asyncio overhead, final runtime to verify the three prime numbers
took less than a second (Event loop swapping is expensive!)
   
