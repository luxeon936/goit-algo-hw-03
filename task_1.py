import os
import shutil
import argparse

def parse_arguments():
    # Опис програми та параметрів
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання файлів та їх сортування за типами (розширеннями).")
    parser.add_argument('source_dir', help="Шлях до вихідної папки")
    parser.add_argument('destination_dir', nargs='?', default='dist', help="Шлях до папки призначення (за замовчуванням: 'dist')")
    return parser.parse_args()

def copy_and_sort_files(source_dir, destination_dir):
    try:
        # Перевірка наявності вихідної папки
        if not os.path.exists(source_dir):
            print(f"Помилка: вихідна папка '{source_dir}' не існує.")
            return

        # Створення папки призначення, якщо вона ще не існує
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
            print(f"Створено папку призначення: '{destination_dir}'.")

        # Рекурсивно проходимо по всіх файлах та папках у вихідній папці
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    # Визначення розширення файлу
                    _, extension = os.path.splitext(file)
                    extension = extension[1:].lower() if extension else 'no_extension'

                    # Створення шляху до папки за типом файлу (розширенням)
                    dest_subdir = os.path.join(destination_dir, extension)
                    if not os.path.exists(dest_subdir):
                        os.makedirs(dest_subdir)
                        print(f"Створено папку '{dest_subdir}' для файлів з розширенням '.{extension}'.")

                    # Копіюємо файл до відповідної папки
                    shutil.copy2(file_path, dest_subdir)
                    print(f"Файл '{file_path}' скопійовано до '{dest_subdir}'.")
                except Exception as e:
                    print(f"Помилка під час копіювання файлу '{file_path}': {e}")
    except Exception as e:
        print(f"Помилка під час обробки папки '{source_dir}': {e}")

def main():
    args = parse_arguments()
    copy_and_sort_files(args.source_dir, args.destination_dir)

if __name__ == "__main__":
    main()
