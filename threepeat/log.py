"""
Logging settings.
"""

import logging

logging.basicConfig(
    format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO
)


def get_logger(name: str | None = None) -> logging.Logger:
    logger = logging.getLogger(name)
    return logger
