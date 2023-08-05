import logging
import os
from logging.handlers import TimedRotatingFileHandler

from rich.logging import RichHandler

logger = logging.getLogger(__name__)

log_dir = os.path.join(os.path.normpath(
    os.getcwd() + os.sep + os.pardir), 'logs')
log_fname = os.path.join(log_dir, 'logger.log')

# shell_handler = logging.StreamHandler()
shell_handler = RichHandler()
file_handler = TimedRotatingFileHandler(
    log_fname.strip('.'),  when='midnight',backupCount=30)
file_handler.suffix = r'%Y-%m-%d-%H-%M-%S.log'

logger.setLevel(logging.DEBUG)
shell_handler.setLevel(logging.CRITICAL)
file_handler.setLevel(logging.DEBUG)


# the formatter determines what our logs will look like
# fmt_shell = '%(levelname)s %(asctime)s %(message)s'
fmt_shell = '%(message)s'
fmt_file = '%(levelname)8s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s'

shell_formatter = logging.Formatter(fmt_shell)
file_formatter = logging.Formatter(fmt_file)

# here we hook everything together
shell_handler.setFormatter(shell_formatter)
file_handler.setFormatter(file_formatter)

logger.addHandler(shell_handler)
logger.addHandler(file_handler)

