import time
import os
import psutil
from save_performance_data_to_word import save_performance_data_to_word
from rich.prompt import Prompt
from rich.console import Console
from random_number_gen import random_to_file
from merge_sort import merge_sort
from quick_sort import q_sort as main_q_sort
from buble_sort import buble_sort
from quick_sort_without_partition import q_sort




console = Console()



# def performance(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         performance_data = {
#             "function": func.__name__,
#             "time_taken": end_time - start_time,
#         }
#         return result, performance_data
#     return wrapper






# generate , read file
def file_reader():
    global count_numbers


    while True:

        try:
            is_file = input("Enter '1' load the file or any thing to generate file number  [1/any] : ")

            if is_file == "1":
                file_path = input("Enter your file path : ")
                break


            else:
                counter_input = input("How many numbers do you want to generate : ")
                num = int(counter_input)

                if num <= 0:
                    console.print("\nPlease enter a positive number.\n", style="bold red")
                
                else:
                    file_path = random_to_file(counter = num)
                    console.print(f"\nyour random file numer generated in --> {file_path!r}\n", style="bold green")
                    count_numbers = int(counter_input)
                    break

        except :
            console.print("\nInvalid input. Please enter a valid number.\n", style="bold red")

    try :
        with open(file_path, "r") as f:
            numbers = [int(line.strip()) for line in f.readlines()]
            console.print(f"\nyour numbers Extracted\n", style="bold green")
    except :
        console.print("\nError while reading file.\n", style="bold red")
        exit()

    return numbers



# time, memory decorator
def performance(func):
    def wrapper(*args, **kwargs):
        process = psutil.Process(os.getpid())
        start_memory = process.memory_info().rss
        start_time = time.perf_counter()  
        result = func(*args, **kwargs)
        end_time = time.perf_counter()  
        end_memory = process.memory_info().rss 

        memmory = end_time - start_time
        performance_data = {
            "function": func.__name__.replace("_decorated", "").replace("main_q_sort","partition_quck_sort").replace("q_sort","quick_sort"),
            "time_taken":  memmory if memmory >= 0 else 0.0000001,  
            "memory_usage": (end_memory - start_memory) / 10**6 ,
            "number_count": int(count_numbers)
        }
        return result, performance_data
    return wrapper




def write_file(file_name, sorted_nums):

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)
    console.print(f"\nyour random file numer generated in --> {file_path!r}\n", style="bold green")

    try :
        with open(file_path, "w") as file:
            for num in sorted_nums:
                file.write(str(num) + "\n")
            console.print(f"\nyour sorted numbers in {file_path}\n", style="bold green")

    except :
        console.print("\nError while reading file.\n", style="bold red")




# numbers = file_reader()




@performance
def merge_sort_decorated(numbers):
    return merge_sort(numbers)

@performance
def q_sort_decorated(numbers):
    return q_sort(numbers)

@performance
def main_q_sort_decorated(numbers):
    return main_q_sort(numbers)

@performance
def buble_sort_decorated(numbers):
    return buble_sort(numbers)

@performance
def python_sort_decorated(numbers):
    return sorted(numbers)





    
# main func usage
if __name__ == "__main__":
    list_data = []
    numbers = file_reader()

    sort_iput = Prompt.ask("Enter your your algorithem or 'all' for teat all algorithem sort", choices=["all", "merge", "quick", "partition_quick", "python", "buble"], default="all")

    def main_merge():

        result, performance_data = merge_sort_decorated(numbers)
        list_data.append(performance_data)
        print(list_data)
        write_file(file_name="merge_sorted.txt", sorted_nums=result)
        file_path = save_performance_data_to_word(list_data, flag="merge")
        console.print(f"\nyour Reporting functions in {file_path}\n", style="bold blue")


    def main_quick():

        result, performance_data = q_sort_decorated(numbers)
        list_data.append(performance_data)
        print(list_data)
        write_file(file_name="quick_sorted.txt", sorted_nums=result)
        file_path = save_performance_data_to_word(list_data, flag="quick")
        console.print(f"\nyour Reporting functions in {file_path}\n", style="bold blue")


    def main_partition_quick():

        result, performance_data = main_q_sort_decorated(numbers)
        list_data.append(performance_data)
        print(list_data)
        write_file(file_name="partition_quick_sorted.txt", sorted_nums=result)
        file_path = save_performance_data_to_word(list_data, flag="partition_quick")
        console.print(f"\nyour Reporting functions in {file_path}\n", style="bold blue")


    def main_python():

        result, performance_data = python_sort_decorated(numbers)
        list_data.append(performance_data)
        print(list_data)
        write_file(file_name="python_sorted.txt", sorted_nums=result)
        file_path = save_performance_data_to_word(list_data, flag="python")
        console.print(f"\nyour Reporting functions in {file_path}\n", style="bold blue")

    def main_buble(numbers = numbers):

        if  len(numbers) <= 10000:

            result, performance_data = buble_sort_decorated(numbers)
            list_data.append(performance_data)
            print(list_data)
            write_file(file_name="buble_sorted.txt", sorted_nums=result)
            file_path = save_performance_data_to_word(list_data, flag="buble")
            console.print(f"\nyour Reporting functions in {file_path}\n", style="bold blue")

        else:
            performance_data = {
                "function": "bubble_sort",
                "time_taken": "Timeout",
                "memory_usage": "N/A",
                "number_count": len(numbers)  
            }
            list_data.append(performance_data)
            print(list_data)
            file_path = save_performance_data_to_word(list_data, flag="buble")
            console.print(f"\nyour Reporting functions in {file_path}\n", style="bold blue")



    if sort_iput == "all":

        result, performance_data = merge_sort_decorated(numbers)
        list_data.append(performance_data)
        print(list_data)
        write_file(file_name="merge_sorted.txt", sorted_nums=result)



        result, performance_data = q_sort_decorated(numbers)
        list_data.append(performance_data)
        print(list_data)
        write_file(file_name="quick_sorted.txt", sorted_nums=result)


        result, performance_data = main_q_sort_decorated(numbers)
        list_data.append(performance_data)
        print(list_data)
        write_file(file_name="partition_quick_sorted.txt", sorted_nums=result)
        

        result, performance_data = python_sort_decorated(numbers)
        list_data.append(performance_data)
        print(list_data)
        write_file(file_name="python_sorted.txt", sorted_nums=result)




        if  len(numbers) <= 10000:

            result, performance_data = buble_sort_decorated(numbers)
            list_data.append(performance_data)
            print(list_data)
            write_file(file_name="buble_sorted.txt", sorted_nums=result)
            file_path = save_performance_data_to_word(list_data, flag="buble")
            console.print(f"\nyour Reporting functions in {file_path}\n", style="bold blue")

        else:
            performance_data = {
                "function": "bubble_sort",
                "time_taken": "Timeout",
                "memory_usage": "N/A",
                "number_count": len(numbers)  
            }
            list_data.append(performance_data)
            print(list_data)
            file_path = save_performance_data_to_word(list_data, flag="buble")
            console.print(f"\nyour Reporting functions in {file_path}\n", style="bold blue")



        file_path = save_performance_data_to_word(list_data, flag="all")
        console.print(f"\nyour Reporting functions in {file_path}\n", style="bold blue")




    elif sort_iput == "merge":
        
        main_merge()

    elif sort_iput == "quick":

        main_quick()

    elif sort_iput == "partition_quick":

        main_partition_quick()

    elif sort_iput == "python":

        main_python()
        

    elif sort_iput == "buble":

        main_buble()

   