from updater import update
import logging
from settings import INSTALL_DIR

if __name__ == '__main__':
    logger = logging.getLogger()
    logging.basicConfig(filename=rf"{INSTALL_DIR}\log.txt", filemode='w')
    update()
