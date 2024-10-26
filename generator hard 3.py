import csv


def column_statistics(file_path, column_index):
    count = 0
    total = 0
    min_value = float("inf")
    max_value = float("-inf")

    try:
        print(f"Attempting to open file: {file_path}")  # Отладочное сообщение
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Пропускаем заголовок

            for row in reader:
                try:
                    value = float(row[column_index])
                    count += 1
                    total += value

                    if value < min_value:
                        min_value = value
                    if value > max_value:
                        max_value = value
                except (ValueError, IndexError):
                    continue  # Игнорируем строки с ошибками

        if count == 0:
            print("No valid data found in the specified column.")
            return None

        average = total / count if count > 0 else 0
        return count, average, min_value, max_value

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


# Пример использования
stats = column_statistics("data.csv", 1)  # Убедись, что файл не существует
if stats:
    print(f"Количество строк: {stats[0]}")
    print(f"Среднее значение: {stats[1]}")
    print(f"Минимальное значение: {stats[2]}")
    print(f"Максимальное значение: {stats[3]}")
