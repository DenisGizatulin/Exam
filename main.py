import json

def read_json_file(file_path): # Функция для чтения данных из файла
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)  # Считываем JSON файл
    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
    except json.JSONDecodeError:
        print("Ошибка: Некорректный формат JSON в файле.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
    return None

def display_data(data): # Функция для вывода данных на экран
    if not data:
        print("Данные отсутствуют или не были загружены.")
        return

    print("Name:", data.get("Name", "N/A"))
    print("Mobile:", data.get("Mobile", "N/A"))
    print("Boolean:", data.get("Boolean", "N/A"))
    print("Pets:", ", ".join(data.get("Pets", [])))
    print("Address:")
    address = data.get("Address", {})
    print("  Permanent address:", address.get("Permanent address", "N/A"))
    print("  Current address:", address.get("current Address", "N/A"))

def main():
    # Указание пути файла
    file_path = 'exam_file.json'
    # Вызовы функций
    data = read_json_file(file_path)
    display_data(data)

if __name__ == "__main__":
    main()