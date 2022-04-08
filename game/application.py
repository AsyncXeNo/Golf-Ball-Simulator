from __future__ import annotations

import pygame

from typing import TYPE_CHECKING
from logging_module.custom_logging import get_logger
from graphics.conn_pygame_graphics import ConnPygameGraphics
from graphics.constants import RESOLUTION, FPS, BALL_COLOR, BALL_RADIUS

if TYPE_CHECKING:
    import logging


class Application(object):
    """Class which handles the game"""

    def __init__(self, fullscreen: bool = False) -> None:
        self.logger: logging.Logger = get_logger('game')

        self.logger.info('starting application!')

        pygame.init()

        # Application stuff

        self.conn_pygame_graphics: ConnPygameGraphics = ConnPygameGraphics(RESOLUTION[0], RESOLUTION[1], 'golf', fullscreen=fullscreen)
        self.game_surface: pygame.Surface = pygame.Surface(RESOLUTION) 
        self.conn_pygame_graphics.set_game_surface(self.game_surface)

        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.fps: int = FPS

        self.running: bool = True

        # Game stuff



        # Main loop

        self.run_main_loop()

    def graphics_handler(self) -> None:
        """Handles graphics for the application"""

        self.clock.tick(self.fps)

        # make changes to game surface as you like
        self.game_surface.fill(pygame.Color('black'))
        # self.conn_pygame_graphics.draw_circle(BALL_COLOR, (RESOLUTION[0] // 2, RESOLUTION[1] // 2), BALL_RADIUS, surface=self.game_surface)
        
        self.conn_pygame_graphics.tick()


    def events_handler(self) -> None:
        """Handles events for the application"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.logger.info('exiting application')
                pygame.quit()


    def run_main_loop(self) -> None:
        """Runs the main loop of the application"""

        while self.running:
            self.graphics_handler()
            self.events_handler()