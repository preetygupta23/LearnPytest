import logging

def test_logfile():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    logger.addHandler(fileHandler)
    formatter= logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")

    logger.info("A information")

    logger.warning("A warning message")

    logger.error("A major error has occurred")

    logger.critical("Critical issue")