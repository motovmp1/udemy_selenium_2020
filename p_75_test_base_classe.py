# Logging
import logging


class Baseclass:

    def getLogger(self):

        # cacht the name file using __name__, please check
        logger = logging.getLogger(__name__)

        # parent  logging becareful
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s :"
            " %(funcName)s :%(name)s : %(message)s")

        # filehandler object / connected above
        logger.addHandler(fileHandler)

        # formatter is connected to login
        fileHandler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)

        return logger

        # # debug print out message / this is three log
        # logger.debug("A debug statement is executed")
        # logger.info("Information stataement messages")
        # logger.warning("Something is in warning mode")
        # logger.error("A major error has happened")
        # logger.critical("Critical issues")
