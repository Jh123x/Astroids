import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen,
            pygame.Color(255, 255, 255),
            self.position,
            self.radius,
            2,
        )
        
    def update(self, dt: int):
        self.position += self.velocity * dt