from loguru import logger
import os
from dotenv import find_dotenv
logger.remove()
logger.add(os.path.join(os.path.dirname(find_dotenv()),'notebooks','log','log.log'), backtrace=True,  diagnose=True, format="-"*200+"\n{time: YYYY-MM-DD HH:mm:ss} | {level} | {module}.{function}.{line} — {message}", level='INFO', colorize=False)

#logger.add(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log','log.log'), backtrace=True,  diagnose=True, format="\n\n\n{time: YYYY-MM-DD HH:mm:ss} | {level} | {module}.{function}.{line} — {message}", level='INFO', colorize=False)




