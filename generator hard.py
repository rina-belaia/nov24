# open file
# generator open file
# line search
# test generator
# try - except

def log_file_search(file_path, keyword):
    try:
        with open(file_path, "r") as file:
            for line in file:
                if keyword in line:
                    yield line
    except FileNotFoundError:
        print(f"File {file_path} not found.")


for line in log_file_search("server_logs.txt", "ERROR"):
    print(line)
