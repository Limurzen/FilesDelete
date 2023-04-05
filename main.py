import os
import hashlib

def get_file_checksum(filename):
    """Функция, которая возвращает хеш-сумму файла"""
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def find_duplicate_files(starting_directory):
    """Функция, которая ищет дубликаты файлов в заданной директории"""
    # Словарь, в котором ключи - это хеш-суммы файлов, а значения - это списки файлов
    # с той же хеш-суммой.
    duplicates = {}
    for dirpath, dirnames, filenames in os.walk(starting_directory):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            file_checksum = get_file_checksum(full_path)
            if file_checksum in duplicates:
                duplicates[file_checksum].append(full_path)
            else:
                duplicates[file_checksum] = [full_path]
    return duplicates

def delete_duplicate_files(duplicates):
    """Функция, которая удаляет дубликаты файлов из списка"""
    for key, value in duplicates.items():
        if len(value) > 1:
            print("Найдены дубликаты файлов:")
            for file_path in value:
                print(file_path)
            while True:
                answer = input("Удалить эти файлы? (y/n): ")
                if answer.lower() == "y":
                    for file_path in value[1:]:
                        os.remove(file_path)
                    print("Файлы удалены.")
                    break
                elif answer.lower() == "n":
                    print("Файлы не были удалены.")
                    break
                else:
                    print("Неправильный ответ. Введите y или n.")
    print("Поиск и удаление дубликатов завершены.")

# Пример использования функций
duplicates = find_duplicate_files("/path/to/directory")
delete_duplicate_files(duplicates)
