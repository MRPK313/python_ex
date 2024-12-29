import subprocess
import sys

# Install Python libraries
packages_import = ["psutil", "matplotlib", "rich", "docx", "psutil"]
install_name_packages = ["psutil", "matplotlib", "rich", "python-docx", "psutil"]

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

for package in packages_import:
    try:
        __import__(package)
    except ImportError:
        print(f"{package} is not installed. Installing...\n\n")
        install(install_name_packages)





import time
import os
import psutil
import matplotlib.pyplot as plt  # برای رسم نمودار اضافه شد
from save_performance_data_to_word import save_performance_data_to_word
from rich.prompt import Prompt
from rich.console import Console
from random_number_gen import random_to_file
from merge_sort import merge_sort
from quick_sort import q_sort as main_q_sort
from buble_sort import buble_sort
from quick_sort_without_partition import q_sort

console = Console()

# generate , read file
def file_reader():
    global count_numbers

    while True:

        try:
            is_file = input("Enter '1' load the file or any thing to generate file number [1/any] : ")

            if is_file == "1":
                file_path = input("Enter your file path : ")
                count_numbers = sum(1 for _ in open(file_path))  # Count lines in the file
                break

            else:
                counter_input = input("How many numbers do you want to generate : ")
                num = int(counter_input)

                if num <= 0:
                    console.print("\nPlease enter a positive number.\n", style="bold red")
                
                else:
                    file_path = random_to_file(counter=num)
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

        time_take = end_time - start_time
        memmory = (end_memory - start_memory) / 10**6
        performance_data = {
            "function": func.__name__.replace("_decorated", "").replace("main_q_sort","partition_quck_sort").replace("q_sort","quick_sort"),
            "time_taken":  time_take if time_take >= 0 else 0.0000001,  
            "memory_usage":  memmory if memmory >= 0 else 0.0000001,
            "number_count": int(count_numbers)
        }
        return result, performance_data
    return wrapper

def write_file(file_name, sorted_nums):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)

    try :
        with open(file_path, "w") as file:
            for num in sorted_nums:
                file.write(str(num) + "\n")
            console.print(f"\nyour sorted numbers in {file_path}\n", style="bold yellow")

    except :
        console.print("\nError while reading file.\n", style="bold red")

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

    sort_input = Prompt.ask("Enter your your algorithem or 'all' for teat all algorithem sort", choices=["all", "merge", "quick", "partition_quick", "python", "buble"], default="all")

    def main_merge():
        result, performance_data = merge_sort_decorated(numbers[:])
        list_data.append(performance_data)
        write_file(file_name="merge_sorted.txt", sorted_nums=result)

    def main_quick():
        result, performance_data = q_sort_decorated(numbers[:])
        list_data.append(performance_data)
        write_file(file_name="quick_sorted.txt", sorted_nums=result)

    def main_partition_quick():
        result, performance_data = main_q_sort_decorated(numbers[:])
        list_data.append(performance_data)
        write_file(file_name="partition_quick_sorted.txt", sorted_nums=result)

    def main_python():
        result, performance_data = python_sort_decorated(numbers[:])
        list_data.append(performance_data)
        write_file(file_name="python_sorted.txt", sorted_nums=result)

    def main_bubble():
        if len(numbers) <= 10000:
            result, performance_data = buble_sort_decorated(numbers[:])
            list_data.append(performance_data)
            write_file(file_name="buble_sorted.txt", sorted_nums=result)
        else:
            performance_data = {
                "function": "bubble_sort",
                "time_taken": "Timeout",
                "memory_usage": "N/A",
                "number_count": len(numbers)  
            }
            list_data.append(performance_data)

    if sort_input == "all":
        main_merge()
        main_quick()
        main_partition_quick()
        main_python()
        main_bubble()

        # Save all results in one Word file
        file_path = save_performance_data_to_word(list_data, flag="all")
        console.print(f"\nyour Reporting functions in {file_path}\n", style="bold blue")

        # رسم نمودار بر اساس performance_data
        algorithms = [item["function"] for item in list_data]
        time_taken = [item["time_taken"] if isinstance(item["time_taken"], (int, float)) else 0 for item in list_data]
        memory_usage = [item["memory_usage"] if isinstance(item["memory_usage"], (int, float)) else 0 for item in list_data]

        x = range(len(algorithms))

        plt.figure(figsize=(10, 6))

        # رسم نمودار زمان
        plt.bar(x, time_taken, width=0.4, label="Time Taken (s)", color="skyblue", align='center')
        
        # رسم نمودار استفاده از حافظه
        plt.bar(x, memory_usage, width=0.4, label="Memory Usage (MB)", color="orange", align='edge')

        plt.xticks(x, algorithms, rotation=45)
        plt.ylabel("Performance Metrics")
        plt.title("Sorting Algorithm Performance")
        plt.legend()
        plt.tight_layout()
        
        # نمایش نمودار
        plt.show()

    elif sort_input == "merge":
        main_merge()
    elif sort_input == "quick":
        main_quick()
    elif sort_input == "partition_quick":
        main_partition_quick()
    elif sort_input == "python":
        main_python()
    elif sort_input == "buble":
        main_bubble()

    # Save individual result if not "all"
    if sort_input != "all":
        file_path = save_performance_data_to_word(list_data, flag=sort_input)
        console.print(f"\nyour Reporting functions in {file_path}\n", style="bold blue")
