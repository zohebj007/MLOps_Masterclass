"""
11_logging.py

Topic: logging module basics, named loggers, handlers, rotating handler
"""
import logging
from logging.handlers import RotatingFileHandler
import os

def easy():
    print("== Easy: basicConfig console logging ==")
    logging.basicConfig(level=logging.INFO)
    logging.info("info message")
    logging.error("error message")

def intermediate():
    print("\n== Intermediate: named logger with formatter ==")
    logger = logging.getLogger("mlops")
    if not logger.handlers:
        h = logging.StreamHandler()
        fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        h.setFormatter(fmt)
        logger.addHandler(h)
    logger.setLevel(logging.DEBUG)
    logger.debug("debug")
    logger.info("info")

def advanced():
    print("\n== Advanced: RotatingFileHandler (logs/rot.log) ==")
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger("rot")
    if not logger.handlers:
        fh = RotatingFileHandler("logs/rot.log", maxBytes=1024, backupCount=2)
        fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(fh)
    logger.setLevel(logging.INFO)
    for i in range(30):
        logger.info("line %d", i)
    print("wrote rotating logs to logs/rot.log")

if __name__ == "__main__":
    easy(); intermediate(); advanced()
