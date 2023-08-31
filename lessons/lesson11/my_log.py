import logging


logging.basicConfig(filename='app.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format='%(process)d %(asctime)s %(name)s - %(levelname)s - %(message)s')

logging.warning('This will get logged to a file')

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


class PointError(Exception):
    pass


class Point:
    def __init__(self, x=0, y=0):
        logging.info(f"create point {x=}{y=}")
        self.__x = x
        self.__y = y

    def __repr__(self):
        return f"({self.__x}, {self.__y})"

    def __add__(self, other):
        p = Point()
        p.x = self.__x + other.__x
        p.y = self.__y + other.__y
        return p

    def add(self, other):
        p = Point()
        p.__x = self.__x + other.__x
        p.__y = self.__y + other.__y
        return p

    def __lt__(self, other):
        return self.__x + self.__y < other.__x + other.__y

    @property
    def x(self):
        print("get_x")
        return self.__x

    @x.setter
    def x(self, x):
        logging.info(f"set_x {x}")
        if type(x) is int:
            self.__x = x
        else:
            logging.error(f"set_x {x}", exc_info=True)
            raise PointError()

    @property
    def y(self):
        print("get_y")
        return self.__y

    @y.setter
    def y(self, y):

        print("set_y", y)
        if type(y) is int:
            self.__y = y
        else:
            raise ZeroDivisionError("aaa")

p = Point(25, 22)
p.x = 15
p.x = "aaa"