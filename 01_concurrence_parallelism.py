# CONCURRENCY => It is the ability of a system to be able of handle multiple tasks at the same 
# time (not necessarily in parallel), intercalating their execution on the same CPU core.  

# PARALLELISM => It is the execution of two tasks at the same time or in parallel, this optimizes 
# the use of hardware resources and increases the software performance. For two or mare processes 
# to run at the same time, each must run on a CPU core.  

# PROCESS => It is the instance of a program with its own memory resource, CPU, permissions, date 
# input/output operation, all of them are assigned by the operating system.  

# THREADS => Known as threads or lightweight processes, they are tasks that can be executed in 
# parallel within the same process or program. Additionally, threads share the same memory space 
# with other threads.

from time import sleep, time
import threading  # Threads creation library.

def add(num1, num2):
    result = num1 + num2
    sleep(2)  #                             <-╻             
    print(f"Add result: {result}")  #         │
#                                             │
def subtract(num1, num2):  #                  │
    result = num1 - num2  #                   │ 
    sleep(1)  #                             <-│ => Simulate the time it might take the function
    print(f"Subtraction result: {result}")  # │    in generate a result.
#                                             │
def multiply(num1, num2):  #                  │
    result = num1 * num2  #                   │
    sleep(3)  #                             <-╹
    print(f"Multiplication result: {result}")

# Code execution of sequential way.  
start = time()
add(1, 10)
subtract(1, 10)
multiply(1, 10)
end = time()

print(f"EXECUTION TIME WITHOUT CONCURRENCY (SEQUENTIAL EXECUTION): {end - start} seconds.\n")

# Creation of threads for the tasks or functions to be executed.
task1 = threading.Thread(target=add, args=(1, 10,))
task2 = threading.Thread(target=subtract, args=(1, 10,))
task3 = threading.Thread(target=multiply, args=(1, 10,))

# Execution of tasks or functions of concurrent way.
task1.start()
task2.start()
task3.start()

# Wait for all tasks to finish executing to continue with the execution of the program.
start = time()
task1.join()
task2.join()
task3.join()
end = time()

print(f"EXECUTION TIME WITH CONCURRENCY: {end - start} seconds.")

