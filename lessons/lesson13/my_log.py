import logging

logging.basicConfig(filename='app.log',
                    filemode='w',
                    level=logging.INFO,
                    format='%(process)d %(asctime)s %(name)s - %(levelname)s - %(message)s')


def my_log(func):
    def inner(*args, **kwargs):
        logging.info(f" {func.__name__} {args} {kwargs}")
        return func(*args, **kwargs)

    return inner

def f():
    def my_log(func):
        def inner(*args, **kwargs):
            logging.info(f" {func.__name__} {args} {kwargs}")
            return func(*args, **kwargs)

        return inner
    return my_log