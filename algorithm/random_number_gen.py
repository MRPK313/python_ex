import random



def random_generator(start = 1000, end = 9999, counter = 500000):

    random_numbers = [random.randint(start, end) for _ in range(counter)]


    return random_numbers







if __name__ == '__main__':

    print(f"for test generate 3 number betwin 1000 to 9999 : {random_generator(counter=3)}")