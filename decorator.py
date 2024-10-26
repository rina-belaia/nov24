import datetime

def log_function(log_file ="log.txt"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            timestamp = datetime.datetime.now()
            log_entry = (
                f"Function: {func.__name__}\n"
                f"Arguments: {args}\n"
                f"Result: {result}\n"
                f"Timestamp: {timestamp}\n"
            )
            with open (log_file, "a") as file:
                file.write(log_entry)

            return result
        return wrapper
    return decorator


    return wrap

@log_function("log.txt")
def add_two_numbers(a, b):
    return a + b

add_two_numbers(9, 12)