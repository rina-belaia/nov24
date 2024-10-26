# import file
# generator
# open file
# file reader
# check
# test
import csv


def filter_csv(file_path, column_index, value):
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[column_index] == value:
                    yield row
    except FileNotFoundError:
        print(f"File {file_path} not found.")


for row in filter_csv("data.csv", 1, "desired_value"):
    print(row)

