from time import sleep
from threading import Thread
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово №  {i + 1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

stop = datetime.now()
print(f'Работа потоков {stop - start}')

start = datetime.now()

a = Thread(target=write_words, args=(10, 'example5.txt'))
b = Thread(target=write_words, args=(30, 'example6.txt'))
c = Thread(target=write_words, args=(200, 'example7.txt'))
d = Thread(target=write_words, args=(100, 'example8.txt'))

a.start()
b.start()
c.start()
d.start()


c.join()


stop = datetime.now()

print(f'Работа потоков {stop - start}')
