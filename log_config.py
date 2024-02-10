import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
    datefmt='%d/%m/%Y %I:%M:%S',
    encoding='utf-8',
    handlers=[
        logging.StreamHandler(),  # Логирование в консоль
        logging.FileHandler('bot.log')  # Логирование в файл
    ])
