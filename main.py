import json

try:
    # Открытие и чтение файла
    with open('exam_file.json', 'r', encoding='utf-8') as file:
        data = json.load(file)  # Считываем JSON файл

    # Вывод информации на экран
    print("Name:", data.get("Name", "N/A"))
    print("Mobile:", data.get("Mobile", "N/A"))
    print("Boolean:", data.get("Boolean", "N/A"))
    print("Pets:", ", ".join(data.get("Pets", [])))
    print("Address:")
    address = data.get("Address", {})
    print("  Permanent address:", address.get("Permanent address", "N/A"))
    print("  Current address:", address.get("current Address", "N/A"))

except FileNotFoundError:
    print("Ошибка: Файл 'exam_file.json' не найден.")
except json.JSONDecodeError:
    print("Ошибка: Некорректный формат JSON в файле.")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")