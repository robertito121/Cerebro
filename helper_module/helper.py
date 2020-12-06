import logging


class Helper:

    @staticmethod
    def get_logger():
        log = logging.getLogger("cerebro_application")
        handler = logging.FileHandler('cerebro.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        log.addHandler(handler)
        log.setLevel(logging.DEBUG)
        return log

