import logging
import pygame

from typing import Optional
from logging_module.custom_logging import get_logger
from graphics.constants import IMAGE_PATH


class ConnPygameGraphics(object):
    """Graphics handler at the outermost level"""

    def __init__(self, width: int, height: int, caption: str, fullscreen: bool = False) -> None:  

        self.logger: logging.Logger = get_logger('graphics')
        self.logger.info('hello from conn_pygame_graphics!')

        pygame.init()

        self.width: int = width
        self.height: int = height
        self.caption: str = caption

        if fullscreen:
            self.window: pygame.Surface = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        else:
            self.window: pygame.Surface = pygame.display.set_mode((self.width, self.height))
            
        self.game_surface: pygame.Surface = None

        pygame.display.set_caption(self.caption)

        self.fonts: dict[str, str] = {
            'regular': None,
            'italic': None,
            'bold': None,
            'bolditalic': None
        }

        self.image_path: str = IMAGE_PATH

    def tick(self) -> None:
        """Called on every iteration of the Game Loop"""

        if not self.game_surface:
            self.logger.error('no game surface set. cannot tick')
            return

        self.window.fill((0, 0, 0))

        self.window.blit(self.game_surface, (0, 0))

        pygame.display.update()

    def set_game_surface(self, surface: pygame.Surface) -> None:
        """Sets the game surface"""

        if surface.get_size() != self.window.get_size():
            self.logger.warning('game surface size does not match window size')

        self.game_surface = surface

    # Shapes

    def draw_line(self, color: tuple[int, int, int, int], start: tuple[int, int], end: tuple[int, int], width: int = 1, surface: Optional[pygame.Surface] = None) -> pygame.Rect:
        """Draws a line of given width (default 1) on a surface (default main window surface)"""

        if not surface:
            surface = self.window

        return pygame.draw.line(surface, color, start, end, width)

    def draw_lines(self, color: tuple[int, int, int, int], points: list[tuple[int, int]], width: int = 1, closed: bool = False, surface: Optional[pygame.Surface] = None) -> pygame.Rect:
        """Draws multiple lines on the screen with given width (default 1) connecting all the points in the given sequence on a surface (default main window surface)"""

        if not surface:
            surface = self.window

        return pygame.draw.lines(surface, color, closed, points, width)

    def draw_circle(self, color: tuple[int, int, int, int], center: tuple[int, int], radius: int, quadrants: int = 0b1111, width: int = 0, surface: Optional[pygame.Surface] = None) -> pygame.Rect:
        """Draws the specified quadrants of the circle (default 0b1111) on a surface (default main window surface)"""

        if not surface:
            surface = self.window

        quadrants = [bool(quadrants & 0b1000), bool(quadrants & 0b100), bool(quadrants & 0b10), bool(quadrants & 0b1)]

        return pygame.draw.circle(surface, color, center, radius, width, *quadrants)

    def draw_rect(self, color: tuple[int, int, int, int], rect_x: int, rect_y: int, rect_width: int, rect_height: int, width: int = 0, surface: Optional[pygame.Surface] = None) -> pygame.Rect:
        """Draws a rectangle with given dimensions on a surface (default main window surface)"""

        if not surface:
            surface = self.window

        return pygame.draw.rect(surface, color, pygame.Rect(rect_x, rect_y, rect_width, rect_height), width)

    def draw_polygon(self, color: tuple[int, int, int, int], points: list[tuple[int, int]], width: int = 0, surface: Optional[pygame.Surface] = None) -> pygame.Rect:
        """Draws a polygon using the given points on a surface (defualt main window surface)"""

        if not surface:
            surface = self.window

        return pygame.draw.polygon(surface, color, points, width)

    # Images

    def convert_to_pygame_image(self, name: str) -> Optional[pygame.Surface]:
        """Loads and returns a pygame image with given name"""

        try:
            image = pygame.image.load(f'{self.image_path}{name}')
        except FileNotFoundError:
            self.logger.error('Invalid image file name. Ignoring load request')
            return

        return image

    def blit_image(self, pos: tuple[int, int], image_name: str, width: int = 0, height: int = 0, surface: Optional[pygame.Surface] = None) -> Optional[pygame.Rect]:
        """Blits an image to a surface (default main window surface)"""

        if not surface:
            surface = self.window

        image = self.convert_to_pygame_image(image_name)

        if not image:
            self.logger.error('No image file found. Ignoring blit request')
            return

        image_size = (
            width if width > 0 else int(image.get_width()),
            height if height > 0 else int(image.get_height())
        )

        image = pygame.transform.scale(image, image_size)

        return surface.blit(image, pos)

    # Text

    def render_text(self, font_type: str, size: int, text: str, color: tuple[int, int, int, int], pos: tuple[int, int], background: Optional[tuple[int, int, int, int]] = None, surface: Optional[pygame.Surface] = None) -> Optional[pygame.Rect]:
        """Renders text on a surface (default main window surface)"""

        if not surface:
            surface = self.window

        try:
            font = pygame.font.Font(self.fonts[font_type], size)
        except KeyError:
            self.logger.error(f'Invalid font type {font_type}. Ignoring render request')
            return

        text = font.render(text, True, color, background)

        return surface.blit(text, pos)