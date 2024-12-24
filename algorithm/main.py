from random_number_gen import random_to_file
from rich.console import Console




console = Console()




while True:

    try:
        counter_input = input("How many numbers do you want to generate : ")
        num = int(counter_input)

        if num <= 0:
            console.print("\nPlease enter a positive number.\n", style="bold red")
        
        else:
            file_path = random_to_file(counter = num)
            console.print(f"\nyour random file numer generated in --> {file_path}\n", style="bold green")
            break

    except :
        console.print("\nInvalid input. Please enter a valid number.\n", style="bold red")


    
