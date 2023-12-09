'''
Написать упрощенный вариант утилиты `tail` -- скрипт, выводящий в `stdout` последние 10 строк каждого из переданных файлов.

если передано больше одного файла, то перед обработкой очередного файла необходимо вывести его имя. Подробности смотрите в оригинальной утилите `tail`, ваш скрипт должен повторять форматирование.
если не передано ни одного файла, то нужно вывести последние 17 строк из `stdin`.
'''

import sys

def main():
    if len(sys.argv) == 1:
        f = sys.stdin
        lines = f.readlines()
        for line in lines[-17:]:
            print(line, end='')
        f.close()
    else:
        for i, file in enumerate(sys.argv[1:]):
            if i > 0:
                print()
            print(f'==> {file} <==')
            f = open(file)
            lines = f.readlines()
            for line in lines[-10:]:
                print(line, end='')
            f.close()

if __name__ == '__main__':
    main()