# Intro to Async Programming

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
   