from loguru import logger
import os 

a=logger.add(os.getcwd()+'\log.log', backtrace=False,  diagnose=False, format="\n\n\n{time: YYYY-MM-DD HH:mm:ss} | {level} | {module}.{function}.{line} — {message}", level='INFO', colorize=False)

