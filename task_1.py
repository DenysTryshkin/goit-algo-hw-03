import os
import shutil
import argparse
from pathlib import Path

def copy_and_sort_files(src_dir, dest_dir):
    try:
        # Перевіряємо, чи існує вихідна директорія
        if not src_dir.exists() or not src_dir.is_dir():
            print(f"Помилка: Директорія {src_dir} не існує або не є директорією.")
            return
        
        # Рекурсивно перебираємо всі файли і папки у вихідній директорії
        for element in src_dir.iterdir():
            if element.is_dir():
                # Рекурсивний виклик для вкладених папок
                print(f"Обробляємо директорію: {element.name}")
                copy_and_sort_files(element, dest_dir)
            elif element.is_file():
                # Отримуємо розширення файлу (без крапки) та створюємо відповідну піддиректорію
                file_ext = element.suffix.lstrip('.').lower()
                ext_dir = dest_dir / file_ext
                ext_dir.mkdir(exist_ok=True)
                
                # Копіюємо файл до піддиректорії
                new_file_path = ext_dir / element.name
                shutil.copy2(element, new_file_path)
                print(f"Файл {element.name} скопійовано до {new_file_path}")
    
    except PermissionError as e:
        print(f"Помилка доступу: {e}")
    except Exception as e:
        print(f"Непередбачена помилка: {e}")

def main():
    # Парсимо аргументи командного рядка
    parser = argparse.ArgumentParser(description='Рекурсивне копіювання файлів за розширенням до нових директорій.')
    parser.add_argument('src_dir', type=str, help='Шлях до вихідної директорії')
    parser.add_argument('dest_dir', nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням dist)')
    
    args = parser.parse_args()
    
    # Створюємо шляхи до вихідної та цільової директорії
    src_path = Path(args.src_dir)
    dest_path = Path(args.dest_dir)
    
    # Створюємо цільову директорію, якщо її ще немає
    dest_path.mkdir(exist_ok=True)
    
    # Запускаємо функцію для копіювання та сортування файлів
    copy_and_sort_files(src_path, dest_path)

if __name__ == "__main__":
    main()

# Для запуску коду, введи команду наведену нижче
# /usr/local/bin/python3 /Users/denys/Desktop/hw-algo/goit-algo-hw-03/task_1.py /Users/denys/Desktop/hw-algo/goit-algo-hw-03/source_folder
# Запуск Python: /usr/local/bin/python3 - це шлях до інтерпретатора Python на вашому комп'ютері. Цей шлях може змінюватися залежно від способу встановлення Python.
# Вказівка скрипта: /Users/denys/Desktop/hw-algo/goit-algo-hw-03/task_1.py - це абсолютний шлях до вашого скрипта task_1.py, який ви хочете виконати.
# Вказівка вихідної директорії: /Users/denys/Desktop/hw-algo/goit-algo-hw-03/source_folder - це шлях до директорії, з якої ваш скрипт буде копіювати файли та організовувати їх.
