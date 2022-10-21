#Модуль для работы с константами
import string
#Модуль многопоточности
import multiprocessing as mp
from hashlib import sha256
#Для работы с итераторами
import itertools
import time


#Англ строчные константы
alphabet = string.ascii_lowercase

my_file = open("sha.txt", "r")
    #Запись строк в матрицу
array = [row.strip() for row in my_file]

def calculation(first_bits):
    #возвращает текущий процесс
    name_proc = mp.current_process().name
    #декартово множ-во для подборки паролей
    for i in itertools.product(first_bits, alphabet, alphabet, alphabet, alphabet):
        if sha256(''.join(i).encode('utf-8')).hexdigest() in array:
            print(name_proc)
            print(sha256(''.join(i).encode('utf-8')).hexdigest(), '   Пароль - ' + ''.join(i))
my_file.close()


#Ввод количества потоков
def inputNumber():
    while True:
        try:
            n = int(input("Ввести количество потоков (1-26): "))
        except ValueError:
            print("Ввести количество потоков (1-26):")
        else:
            if n >= 1 and n <= 26:
                return n
            print("Число не входит в заданный интервал")


if __name__ == "__main__":
    number_of_processes = []
    number_of_parts = inputNumber()
    # количество символов в строке
    partition_size = len(alphabet) // number_of_parts
    #возвращает абсолютное знач счетчика
    pr_st = time.perf_counter()
    #числа начиная с 0
    for i in range(number_of_parts):
        if i == number_of_parts - 1:
            first_bit = alphabet[partition_size * i:]

        else:
            first_bit = alphabet[partition_size * i: partition_size * (i + 1)]
        p = mp.Process(target=calculation, args=(first_bit,))
        number_of_processes.append(p)
        p.start()
    [proc.join() for proc in number_of_processes]
    pr_stop = time.perf_counter()
    print("--- %s seconds ---" % (pr_stop - pr_st))