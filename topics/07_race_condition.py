# RACE CONDITION => It’s the concurrent access (to the same time) to two or more threads to a 
# shared resource, as a global variable, data base, file, etc, it can cause unexpected results on
# each execution of code. It  is due to that while one thread is modifying the shared resource, 
# the other read it and modify to the same time, whether before  that the resource had been 
# uploaded with the new value or no.

# CRITICAL SECTION => It is the code segment in which one or more threads access concurrently to
# a shared resource as a file, global variable, data structure, network resource, etc. To avoid 
# running condition, one thread can access to critical section at a time.

# LOCKS => They are mechanism that avoid race condition through the access a shared resource 
# sequentially (one thread at a time), making modification atomically (without interruption by 
# other threads). Locks reduce the performance of the program, and can sometimes cause mutual 
# locks between threads (deadlocks). Therefore, in some cases it is advisable to use concurrency
# models to treat race condition.

# It is a bad practice to use shared resources as global variables, because if synchronization
# mechanisms such as locks or concurrency models are not used, there may be race condition.

# NOTE => Having race conditions generates a vulnerability known as “Denial of Services” (DoS)
# within a system or software. This is achieved if an attacker accesses a shared resource, block
# it and never releases it (deadlock), causing that the program to wait forever and is jam.

from concurrent.futures import ThreadPoolExecutor

counter = 0  # Shared resource.

def increment_counter():
    global counter
    
    for _ in range(1000000):  
        total_value = counter  # <-╻
        total_value += 1  #        │ => Critical section.
        counter = total_value  # <-╹

futures = []
with ThreadPoolExecutor(max_workers=2) as executor:
    futures.append(executor.submit(increment_counter))
    futures.append(executor.submit(increment_counter))
    executor.shutdown(wait=True)  # Close the thread pool, blocking the entry of more tasks and
    # waiting for the jobs within it to finish executing.

print(f"Counter = {counter}")  # The expected value is 2000000 (1000000 for each thread).

# NOTE => If you run this code with Cpython, the race condition will not occur because this 
# implementation of python due to the GIL (global interpreter lock) does not allow running 
# threads in parallel (at the same time). I recommend you run the code at 
# "https://www.online-python.com/".