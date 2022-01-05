import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

file_handler = logging.FileHandler('found_errors.log')
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)

console = logging.StreamHandler()
console.setLevel(logging.CRITICAL)
logger.addHandler(console)
