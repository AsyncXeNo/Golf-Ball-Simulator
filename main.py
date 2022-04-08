#!venv/bin/python

from __future__ import annotations

import getopt, sys
import typing

from typing import TYPE_CHECKING
from game.application import Application
from logging_module.custom_logging import get_logger

if TYPE_CHECKING:
    import logging

logger: logging.Logger = get_logger(__name__)

argument_list: list[str] = sys.argv[1:]
options: str = ''
long_options: list[str] = ['fullscreen=']


def main() -> None:
    with open('todo.txt', 'r') as f:
        todos = f.readlines()

    if todos:
        todos = ''.join(todos)
        logger.debug(f'\nTODO\n{todos}\n')

    logger.info('hi!')

    fullscreen: bool = False

    arguments, _ = getopt.getopt(argument_list, options, long_options)
    for arg, val in arguments:
        if arg in ('--fullscreen') and val in ('true'):
            fullscreen = True
    
    Application(fullscreen=fullscreen)


if __name__ == '__main__':
    main();