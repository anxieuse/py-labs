'''
Написать упрощенный вариант утилиты `nl` -- скрипт, который выдает в `stdout` пронумерованные строки из файла.
Если файл не передан, то скрипт читает строки из `stdin`.

Он должен работать так же, как `nl -b a`.
'''

import sys

def main():
    if len(sys.argv) == 1:
        f = sys.stdin
    elif len(sys.argv) == 2:
        f = open(sys.argv[1])
    else:
        print('Usage: python3 01-nl.py [FILE]')
        sys.exit(1)

    for i, line in enumerate(f):
        print(f'{i + 1}\t{line}', end='')

    f.close()

if __name__ == '__main__':
    main()