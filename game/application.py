from __future__ import annotations

import pygame

from typing import TYPE_CHECKING

from logging_module.custom_logging import get_logger
from utils.math import between
from graphics.conn_pygame_graphics import ConnPygameGraphics
from graphics.constants import RESOLUTION, FPS, BALL_COLOR, BALL_RADIUS
from game.ball import Ball
from game.point import Point

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

        self.ball: Ball = Ball(self, BALL_COLOR, BALL_RADIUS, Point((100, 100)))
        self.shooting: bool = False 

        # Main loop

        self.run_main_loop()

    def graphics_handler(self) -> None:
        """Handles graphics for the application"""

        self.clock.tick(self.fps)

        # make changes to game surface as you like
        self.game_surface.fill(pygame.Color('black'))
        self.ball.draw_ball(self.game_surface)
        
        self.conn_pygame_graphics.tick()


    def events_handler(self) -> None:
        """Handles events for the application"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.logger.info('exiting application')
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos = mouse_pos[0], self.game_surface.get_height() - mouse_pos[1]

                ball_area = (self.ball.pos.x - self.ball.radius, self.ball.pos.y + self.ball.radius), (self.ball.pos.x + self.ball.radius, self.ball.pos.y - self.ball.radius)

                if between(mouse_pos, *ball_area):
                    self.logger.info('Shooting!')
                    self.shooting = True

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos = mouse_pos[0], self.game_surface.get_height() - mouse_pos[1]

                if self.shooting:
                    new_point = Point((mouse_pos[0], mouse_pos[1]))

                    power = min(self.ball.pos.get_distance(new_point), 300) // 30
                    angle_to_shoot = (self.ball.pos.get_angle(new_point) + 180) % 360
                    
                    self.logger.info(f'Power -> {power}')
                    self.logger.info(f'Angle to shoot at -> {angle_to_shoot:.2f} degrees')

                    self.shooting = False


    def run_main_loop(self) -> None:
        """Runs the main loop of the application"""

        while self.running:
            self.graphics_handler()
            self.events_handler()