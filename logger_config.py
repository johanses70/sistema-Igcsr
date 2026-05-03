import logging

def configurar_logger():
    logger = logging.getLogger("SoftwareFJ")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("logs.txt")
    file_handler.setLevel(logging.ERROR)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
