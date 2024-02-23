from loguru import logger
logger.add('notebooks\logs\log.log', format="{time: YYYY-MM-DD HH:mm:ss} | {level} | {module}.{function}.{line} — {message}", level='INFO', colorize=True)


