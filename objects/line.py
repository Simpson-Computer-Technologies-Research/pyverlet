from physics import Vec2D
import math, pygame


# Custom Line Class
class Line(object):
    def __init__(
        self,
        start: tuple[float, float],
        length: float,
        angle: float,
        width: int = 1,
        color: tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        self.start: Vec2D = Vec2D(start[0], start[1])
        self.length: float = length
        self.angle: float = angle
        self.width: int = width
        self.color: tuple[int, int, int] = color
        self.end: Vec2D = self.calculate_end()

    # Calculate the end
    def calculate_end(self) -> Vec2D:
        degree: float = math.sin(math.radians(self.angle))
        x: float = self.start.x + self.length
        y: float = self.start.y + self.length * degree
        return Vec2D(x, y)

    # Set the line angle
    def set_angle(self, angle: float) -> None:
        self.angle = angle

    # Set the width of the line
    def set_length(self, length: float) -> None:
        self.length = length

    # Draw the line
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.line(
            screen, self.color, self.start.get(), self.end.get(), self.width
        )
