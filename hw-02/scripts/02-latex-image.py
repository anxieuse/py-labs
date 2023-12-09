'''
User
Написать функцию для генерации картинок в латех.
В качестве картинки использовать любую картинку, НО:
Нужно собрать код из первой ДЗ в библиотеку при помощи setuptools/conda-build, выложить в репозиторий
Если первая ДЗ не сделана, то собрать любой пакет, который генерирует картинку
Установить библиотеку, сгенерировать картинку
После этого сгенерировать по полученному латеху PDF с таблицей из easy задачи и картинкой. PDF -  первый артефакт задачи, ссылка на репозиторий в PyPI/Anaconda - второй.
Генерировать pdf можно при помощи pdflatex.
'''

import os
import subprocess
from my_latex_package import generate_latex_table

def generate_latex_document(table_latex, image_path, output_filename):
    latex_content = f"""
    \\documentclass{{article}}
    \\usepackage{{graphicx}}
    \\begin{{document}}

    % Вставка таблицы
    \\begin{{table}}[h!]
    \\centering
    \\caption{{Пример таблицы}}
    {table_latex}
    \\end{{table}}

    % Вставка изображения
    \\begin{{figure}}[h!]
    \\centering
    \\includegraphics[width=0.5\\textwidth]{{{image_path}}}
    \\caption{{Пример изображения}}
    \\end{{figure}}

    \\end{{document}}
    """

    with open(f"{output_filename}.tex", "w") as file:
        file.write(latex_content)

    return f"{output_filename}.tex"

def compile_latex_to_pdf(tex_filename):
    subprocess.run(["tectonic", tex_filename])

def main():
    # Путь к изображению
    image_path = '/Users/leonidkorotkevich/MEGA/work/itmo/py/hw-02/artifacts/sample_image.png'
    
    # Пример таблицы
    matrix = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
    table_latex = generate_latex_table(matrix)  # используйте вашу функцию generate_latex_table

    # Создание LaTeX документа
    tex_filename = generate_latex_document(table_latex, image_path, "output_document")

    # Компиляция в PDF
    compile_latex_to_pdf(tex_filename)

if __name__ == "__main__":
    main()
