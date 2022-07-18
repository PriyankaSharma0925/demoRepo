import logging

def test_logging():

    filehandler=logging.FileHandler("logfile.log")


    logger=logging.getLogger(__name__)
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)
    logger.debug('Debug statements to be used')
    logger.info("User logged in at this time")
    logger.warning("User logged in 2 times. If third attempt fails account will be locked.")
    logger.error("Some error in login functionality")
    logger.critical("Critical error user cannot login")





