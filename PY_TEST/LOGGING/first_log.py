import logging

# Create and Configure Logger
logging.basicConfig(filname="/Users/ddesai/dd/python/Python/PY_TEST/LOGGING/test.log", level=logging.DEBUG)
logger = logging.getLogger()
logger.error("First Message")

print(logger.level)