'''
4.1

Взять функцию подсчета чисел Фибоначчи и сравнить время исполнения кода (вызова функции от большого числа n (чтобы была видна разница в запусках на потоках и процессах) 10 раз через 10 потоков\процессов) при использовании threading и multiprocessing

Необходимо сравнить время выполнения при синхронном запуске, использовании потоков и процессов. 

Артефакт - текстовый файл с результатами запуска различными методами.
'''

import time
import threading
import multiprocessing

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def main():
    n = 35
    print(f'fib({n}) = {fib(n)}')
    print()

    print('synchronous')
    start = time.time()
    for i in range(10):
        fib(n)
    print(f'{time.time() - start} seconds')
    print()

    print('threading')
    start = time.time()
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=fib, args=(n,)))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print(f'{time.time() - start} seconds')
    print()

    print('multiprocessing')
    start = time.time()
    processes = []
    for i in range(10):
        processes.append(multiprocessing.Process(target=fib, args=(n,)))
        processes[-1].start()
    for process in processes:
        process.join()
    print(f'{time.time() - start} seconds')
    print()

if __name__ == '__main__':
    main()