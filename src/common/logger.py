import logging


def init_logger():
    FORMAT = '%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s %(message)s'
    logging.basicConfig(format=FORMAT)
    root_logger = logging.getLogger(__name__)
    logging.getLogger().setLevel('INFO')
    return root_logger


logger = init_logger()
