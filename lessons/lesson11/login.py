import logging


logging.basicConfig(filename='app.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format='%(process)d %(asctime)s %(name)s - %(levelname)s - %(message)s')