from physics import Vec2D


# Circle Collider class
class CircleCollider(object):
    def __init__(
        self,
        position: tuple[float, float],
        radius: float = 200.0,
        color: tuple[int, int, int] = (255, 255, 255),
    ):
        self.position: Vec2D = Vec2D(position[0], position[1])
        self.radius: float = radius
        self.color: tuple[int, int, int] = color
