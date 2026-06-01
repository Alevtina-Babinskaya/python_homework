import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        logger.log(logging.INFO, f"function: {func.__name__} | positional parameters: {args} | keyword parameters: {kwargs} | return: {value}")
        return value
    return wrapper

@logger_decorator
def hello_world():
    print("Hello, world!")

@logger_decorator
def return_true(*args):
    a, b = args[:2]
    return a + b > a - b

@logger_decorator
def get_decorator(**kwargs):
    return logger_decorator

hello_world()
return_true(1, 2, 3)
get_decorator(a=1, b=2)