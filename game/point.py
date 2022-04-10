from __future__ import annotations

import math


class Point(object):
    """A class representing a point on a 2D plane"""

    def __init__(self, pos: tuple[int, int]) -> None:
        self.x = pos[0]
        self.y = pos[1]

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def set_x(self, x: int) -> None:
        """Set the x value of the point"""
        
        self.x = x

    def set_y(self, y: int) -> None:
        """Set the y value of the point"""

        self.y = y

    def get_distance(self, point: Point) -> int:
        """Returns the distance from the current point to another point"""

        x_diff = point.x - self.x
        y_diff = point.y - self.y

        return int(math.sqrt(x_diff ** 2 + y_diff ** 2))

    def get_angle(self, point: Point) -> float:
        """Returns the angle from the current point to aother point"""

        x_diff = point.x - self.x
        y_diff = point.y - self.y  

        if point.x < self.x:
            return math.atan(y_diff / x_diff) * (180 / math.pi) + 180

        elif point.x >= self.x:
            return math.atan(y_diff / x_diff) * (180 / math.pi) + (360 if y_diff < 0 else 0)
            