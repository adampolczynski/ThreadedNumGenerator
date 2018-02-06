import threading
import random
path = './numbers.txt';
path2 = './prime_numbers.txt';
prime_numbers = []
numbers = []

how_many = 300000 ## how many numbers we want
our_range = 900 ## range of numbers we want from 0

class Thread(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.name = name
        self.id = id
    def run(self):
        print_info(self.id, "Generating numbers...")
        while len(numbers) < how_many:
            generate()
        with open(path, 'w') as file:
            file.write(str(numbers))
            print_info(self.id, "Created file with "+str(len(numbers))+" numbers.")
            check_prime_numbers(self.id)

def is_prime(a):
    return all(a % i for i in range(2, a))
def parse(t):
    return int(t.replace('[', '').replace(']', '').replace(',', ''))
def generate():
    rand = random.randint(1, our_range)
    numbers.append(rand)
def print_info(threadNumber, text):
    if threadNumber == 10:
        print(text)
def check_prime_numbers(threadNumber):
    if threadNumber == 10:
        with open(path, 'r') as file:
                pnumbers = file.read()
                print('File opened. Now counting prime numbers. ')
                for number in pnumbers.split():
                    parsed = parse(number)
                    if is_prime(parsed):
                        prime_numbers.append(parsed)
                with open(path2, 'w') as file:
                    file.write(str(prime_numbers))
                    print('File created')

                    
thread1 = Thread(1,"Thread1 ")
thread2 = Thread(2,"Thread2 ")
thread3 = Thread(3,"Thread3 ")
thread4 = Thread(4,"Thread4 ")
thread5 = Thread(5,"Thread5 ")
thread6 = Thread(6,"Thread6 ")
thread7 = Thread(7,"Thread7 ")
thread8 = Thread(8,"Thread8 ")
thread9 = Thread(9,"Thread9 ")
thread10 = Thread(10,"Thread10 ")
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()

print("Exiting main thread")


