from fileinput import filename
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formater = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('./findup.log')
file_handler.setFormatter(formater)
logger.addHandler(file_handler)