"""def run():
    from loguru import logger
    a=logger.add('log.log', backtrace=False,  diagnose=False, format="\n\n\n{time: YYYY-MM-DD HH:mm:ss} | {level} | {module}.{function}.{line} — {message}", level='INFO', colorize=False)
    return 1

if __name__=='__main__':
    run()
"""

from loguru import logger

logger.remove()
logger.add('logs/log.log', backtrace=False,  diagnose=False, format="\n\n\n{time: YYYY-MM-DD HH:mm:ss} | {level} | {module}.{function}.{line} — {message}", level='INFO', colorize=False)
logger.info('logging started')


"""
class log():
    def __init__(self):
        logger.remove()
        logger.add('logs/log.log', backtrace=False,  diagnose=False, format="\n\n\n{time: YYYY-MM-DD HH:mm:ss} | {level} | {module}.{function}.{line} — {message}", level='INFO', colorize=False)
        logger.info('logging started')
        self.ger=logger"""



