'''
Написать скрипт, работающий так же, как утилита `wc`, вызванная без дополнительных опций.
Т.е. для каждого переданного файла утилита выводит статистику (3 числа) и имя файла.

При этом

если передано больше одного файла, то в самом конце утилита выводит суммарную статистику (total),
если ни одного файла не передано, то утилита считывает весь вход и печатает для него статистику без имени.

'''

import sys

def main():
    if len(sys.argv) == 1:
        f = sys.stdin
        print(f'{wc(f)}')
    else:
        total = [0, 0, 0]
        for i, file in enumerate(sys.argv[1:]):
            f = open(file)
            print(f'{wc(f)} {file}')
            total = [total[i] + wc(f)[i] for i in range(3)]
            f.close()
        if len(sys.argv) > 2:
            print(f'{total[0]}\t{total[1]}\t{total[2]} total')

def wc(f):
    lines = f.readlines()
    return [len(lines), sum([len(line.split()) for line in lines]), sum([len(line) for line in lines])]

if __name__ == '__main__':
    main()