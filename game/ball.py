from __future__ import annotations

from typing import TYPE_CHECKING

from logging_module.custom_logging import get_logger
from game.point import Point
from game.velocity import Velocity

if TYPE_CHECKING:
    import logging
    import pygame

    from game.application import Application


class Ball(object):
    """Class representing the ball in the game"""

    def __init__(self, app: Application, color: tuple[int, int, int, int], radius: int, pos: Point) -> None:
        self.logger: logging.Logger = get_logger('game')

        self.app: Application = app

        self.color: tuple[int, int, int, int] = color
        self.radius: int = radius
        self.pos: Point = pos

        self.velocity = Velocity(0, 5, 0)

    def draw_ball(self, surface: pygame.Surface) -> None:
        """Draws the ball on the given surface"""

        self.app.conn_pygame_graphics.draw_circle(self.color, (self.pos.x, surface.get_height() - self.pos.y), self.radius, surface=surface)
