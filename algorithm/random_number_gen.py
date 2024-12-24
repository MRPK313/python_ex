import random
import os


def random_generator(counter = 500000, start = 1000, end = 9999):

    random_numbers = [random.randint(start, end) for _ in range(counter)]


    return random_numbers



def random_to_file(counter = 500000, start = 1000, end = 9999, file_name = "random.txt"):
    
    random_nums = random_generator(counter, start, end)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)

    with open(file_path, "w") as file:
        for num in random_nums:
            file.write(str(num) + "\n")



if __name__ == '__main__':

    print(f"for test generate 3 number betwin 1000 to 9999 : {random_generator(counter=3)}")