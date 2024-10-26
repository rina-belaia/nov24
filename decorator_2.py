def my_decorator(*args, my_param1=None, my_param2=None):
    # my_param1 и my_param2 - это опциональные параметры, которые может принимать декоратор
    def _my_decorator(f):
        def wrap(*args, **kwargs):
            print('my_param1', my_param1)
            print('my_param2', my_param2)

            # Дополнительная логика ДО выполнения функции
            result = f(*args, **kwargs)
            # Дополнительная логика ПОСЛЕ выполнения функции
            return result
        return wrap
    if len(args) == 1 and callable(args[0]):
        return _my_decorator(args[0])    # случай когда декорируем без параметров
    else:
        return _my_decorator             # декорируем с параметрами