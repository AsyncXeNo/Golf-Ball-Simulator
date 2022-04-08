from __future__ import annotations

from typing import TYPE_CHECKING
from logging_module.custom_logging import get_logger

if TYPE_CHECKING:
    import logging


class Ball(object):
    """Class representing the ball in the game"""

    def __init__(self, color: tuple[int, int, int, int], radius: int, pos: tuple[int, int]) -> None:
        self.logger: logging.Logger = get_logger('game')

        self.color: tuple[int, int, int, int] = color
        self.radius: int = radius
        self.pos: tuple[int, int] = pos
