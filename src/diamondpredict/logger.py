from loguru import logger
import os
os.chdir("../../notebooks")
logger.add(os.getcwd()+'\logs\log.log', format="{time: YYYY-MM-DD HH:mm:ss} | {level} | {module}.{function}.{line} — {message}", level='INFO', colorize=True)


