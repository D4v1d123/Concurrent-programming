# THREAD POOL => A specific set of threads that are responsible for solving an indefinite number 
# of tasks concurrently. The main objective of thread pools is to reuse existing threads instead
# of creating and destroying threads for each task (higher cost in terms of resources). Because 
# of this, it is good practice to use them because it maintains a balance between performance 
# and resource consumption.

# It is recommended that tasks assigned to the thread pool be pure functions that have no 
# dependencies on other functions within the thread pool, to avoid race conditions. 

# TASK TYPES:

# * CPU-BOUND TASKS => These are functions that perform complex calculations and are limited by 
# the CPU's processing speed.
# * INPUT/OUTPUT-BOUND TASKS => These are functions that transfer data from one point to another, 
# for this reason they are limited by the data transfer speed, such as the reading and writing to
# disk, network speed, etc.

# Finally, a thread pool allows you to add tasks synchronously or asynchronously, check their 
# status, get responses, assign callback functions to process them and generate results. 

# submit => Method that allows tasks to be assigned to a thread pool.

# add_done_callback => Method that obtains a response given by a task that has finished, then 
# passes it as an argument to a callback function to process it and get a result.

# NOTE => In Python, for CPU-bound tasks computation it is recommended to use process pool 
# instead of threads pool due to Global Interpreter Lock (GIL) limitations. 

from time import sleep
from concurrent.futures import ThreadPoolExecutor

# CPU-bound task.
def add_price_products(product_list):
    subtotal = 0
    
    for product in product_list:
        subtotal += product["amount"] * product["unit_cost"]
        
    return subtotal

# Input/Output-bound task.
def get_user_data(id): 
    sleep(2)  # Simulate database query waiting time.
    user_data = [
        {
            "id": 10025293327, 
            "name": "nayara costa", 
            "mail": "n4ya34@outlook.com", 
            "age": 39
        }
    ]
    
    return user_data

def calc_total_prise(future):  # Callback function for "add_price_products".
    subtotal = future.result()
    iva = (subtotal * 0.19)
    transport_cost = (subtotal * 0.05)
    total = subtotal + iva + transport_cost
  
    print("\nTOTAL TO PAY:")
    print(f"* Subtotal:       ${subtotal:.2f} \
          \n* IVA:            ${iva:.2f} \
          \n* Transport cost: ${transport_cost:.2f} \
          \n-------------------------- \
          \nTOTAL:            ${total:.2f}")

def show_user_data(future):  # Callback function for "get_user_data".
    user_data = future.result()
    
    print("\nCUSTOMER:")
    print(f"* Name: {user_data[0]["name"].title()}. \
          \n* Mail: {user_data[0]["mail"]}. \
          \n* Age: {user_data[0]["age"]}.")


nayaras_purchase = [
    {"product": "rice (500 gr)", "amount": 12, "unit_cost": 0.86},
    {"product": "chocoramo (65 gr)", "amount": 2, "unit_cost":  0.62},
    {"product": "toothbrush colgate", "amount": 1, "unit_cost": 0.30},
    {"product": "lentil (500 gr)", "amount": 7, "unit_cost": 1.04}
]

christians_purchase = [
    {"product": "egg", "amount": 24, "unit_cost": 0.20},
    {"product": "chocolate the sun", "amount": 3, "unit_cost":  1.24}
]

esteban_purchase = [
    {"product": "traditional ramo cake (230 gr)", "amount": 1, "unit_cost": 0.86},
    {"product": "beans (500 gr)", "amount": 4, "unit_cost":  1.24},
    {"product": "sanson wine", "amount": 2, "unit_cost": 3.37},
    {"product": "rise (500 gr)", "amount": 7, "unit_cost": 0.82},
    {"product": "vegetable oil (2500 ml)", "amount": 1, "unit_cost": 4.45},
    {"product": "oreo cookies (24 units)", "amount": 2, "unit_cost": 2.15},
    {"product": "chocoramo (65 gr)", "amount": 1, "unit_cost":  0.62}
]

futures = []  # Futures list.

#                 Number of threads in the thread pool.
#                                   ↓
with ThreadPoolExecutor(max_workers=2) as executor:  # Create thread pool using the context manager "with".
#                                            ↑
#                                  Object or thread pool.


    futures.append(executor.submit(add_price_products, esteban_purchase))
    futures.append(executor.submit(add_price_products, christians_purchase))
    futures.append(executor.submit(add_price_products, nayaras_purchase))
    
#           Add a task or function to the thread pool.                                                 
#                              ↓
    futures.append(executor.submit(get_user_data, 10025293327))
#                                        ↑             ↑
#                                    Task or       Arguments.
#                                    function.
    
    for index, value in enumerate(futures):
        if index < len(futures) - 1:
            # Add a callback function to tasks "add_price_products".
            futures[index].add_done_callback(calc_total_prise) 
        else:
            # Add a callback function to the task "get_user_data".
            futures[index].add_done_callback(show_user_data)         