# Deadlock, creating and avoiding

##### What can lead to a deadlock situation, and why is it undesirable?
Poor threading control, resource allocation, or an inability to self-timeout

##### How is the Dining Philosophers problem related to the problem of deadlock?
Limited resources in an concurrent environment. 5 philosophers, 5 forks, but a philosopher requires 2 forks, and cannot 
put a fork down until they have a bite. WIth no way to coordinate, each philosopher can end up stuck with only one fork, 
unable to release said fork
In compsci, consider a series of memory intensive programs. Each program self allocates half of their needed RAM to 
begin, and then immediately request the remaining RAM required. The system, however, does not have sufficient memory to 
accommodate, and the programs are greedy little buggers who refuse to release memory. Every program is stuck, and the 
system is overloaded. Deadlock Gang

##### What are the four Coffman Conditions?
Scenarios that may cause a concurrent to encounter deadlock
 - Non shareable resource(s), accessible by a single thread at a time
 - Multiple processes require multiple resources
 - Processes will not voluntarily release resources
 - Circular wait, Where X waits for Y waits for Z waits for X to finish. Philosopher's Table

##### How can resource ranking solve the problem of deadlock? What other problems can occur when this is implemented?


##### How can ignoring locks solve deadlock? What problems can this introduce? 


##### How is livelock related to deadlock?


##Scripts
### 01.py
Simulate deadlock by two functions trying to call Locks A and B. Function 1 acquires A Then B, 
Function 2 acquires B then A. Neither function releases locks, and tries to acquire what has already been acquired by 
the other. Deadlock, script freezes
(Rewritten to class format to show what happens when static lock acquisition occurs with no control)
Of note, simply rewriting the functions to both await acquiring Lock A -> Lock B can resolve deadlock, but doing so 
defeats the purpose of multi-threading 
(see Lock.main var 'work') 

### 02.py


### 03.py
