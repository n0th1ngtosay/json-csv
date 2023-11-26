import os
import json

# Путь к папке с JSON файлами
folder_path = 'jsons'

data = []

# Проверка существования папки
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    # Проход по файлам в папке
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):  # Проверка, что файл .json
            file_path = os.path.join(folder_path, filename)

            # Чтение данных из JSON файла
            with open(file_path, 'r') as file:
                json_data = json.load(file)
                # Получение данных о названии файла и областях и добавление их в список
                areas = json_data.get('areas', [])
                # Убираем расширение .json из названия файла
                data.append({'filename': os.path.splitext(
                    filename)[0], 'areas': areas})

# Путь для сохранения файла
output_file_path = 'zones.txt'

# Запись данных в текстовый файл без расширения .json в названиях файлов
with open(output_file_path, 'w') as output_file:
    for entry in data:
        output_file.write(f"{entry['filename']}\n")
        output_file.write(f"{entry['areas']}\n\n")

# Чтение данных из текстового файла и формирование словаря
input_file_path = 'zones.txt'
parsed_data = {}

with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()
    i = 0
    while i < len(lines):
        filename = lines[i].strip()
        areas = eval(lines[i + 1].strip())
        parsed_data[filename] = {'areas': areas}
        i += 3  # Переходим к следующей записи

# Новый путь для сохранения данных
output_file_path = 'zones.txt'

# Запись данных в текстовый файл
with open(output_file_path, 'w') as output_file:
    output_file.write("{\n")  # Начало файла
    for filename, areas_data in parsed_data.items():
        output_file.write(f"'{filename}': {areas_data},\n")
    output_file.write("}")  # Конец файла
