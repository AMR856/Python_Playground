#!/usr/bin/python3
import logging

if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)
    my_logger = logging.getLogger("AmrLogger")
    my_logger.setLevel(logging.DEBUG)
    
    formater  = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")

    my_handler = logging.FileHandler("my_log.log")
    my_handler.setFormatter(formater)
    my_handler.setLevel(logging.INFO)
    my_logger.addHandler(my_handler)
    my_logger.debug("Something's weird")
    my_logger.info("I think something")
    my_logger.critical("Try critcal here")
    my_logger.warning("Try warning here")
    my_logger.error("You got an error idiota")
"""
    Secutrity levels in the system:
    --------------------------------
    DEBUG: Testing and troubleshooting -> What is the value of x for example
    INFO: Informational messages -> You made a backup right now, you got five new emails
    WARNING: Nothing bad happended yet (The system didn't crash and we didn't get any erros) -> running low on space -> Error not critcal
    ERROR: We need to something about it but the system didn't crash yet
    CRITICAL: An essential part of your system is down and the system is gonna crash
    power supply is down, server is down
    --------------------------------
"""

"""
    logging.info("You have some new messages")
    logging.warning("This is a warning, do something about it")
    logging.critical("The server is down lol")
"""

"""
    my_logger.info("Lol this is not a good logger dude")
    my_logger.critical("I think the system is down xd")
    my_logger.log(logging.DEBUG, "A debuggin message here")
"""