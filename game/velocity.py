
class Velocity(object):
    """Class representing velocity"""

    def __init__(self, initial: int, max_vel: int, direction: float) -> None:
        self.current = initial
        self.max = max_vel
        self.direction = direction
