class Vec2D:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y
    
    # When two Vec2D variables are substracted
    def __sub__(self, other: 'Vec2D') -> 'Vec2D':
        return Vec2D(self.x - other.x, self.y - other.y)
    
    # When two Vec2D variables are added
    def __add__(self, other: 'Vec2D') -> 'Vec2D':
        return Vec2D(self.x + other.x, self.y + other.y)
    
    # When two Vec2D variables are multiplied
    def __mul__(self, scalar: float) -> 'Vec2D':
        return Vec2D(self.x * scalar, self.y * scalar)
    
    # When two Vec2D variables are divided
    def __truediv__(self, scalar: float) -> 'Vec2D':
        return Vec2D(self.x / scalar, self.y / scalar)
    
    # When to the power
    def __pow__(self, scalar: float) -> 'Vec2D':
        return Vec2D(self.x ** scalar, self.y ** scalar)
    
    # Reset the position
    def zero(self) -> 'Vec2D':
        self.x = 0.0
        self.y = 0.0
        return self

    # Set the position
    def set(self, x: float = None, y: float = None) -> 'Vec2D': # type: ignore
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        return self
    
    # Get the position
    def get(self) -> tuple[float, float]:
        return (self.x, self.y)

    # Dot product
    def dot(self, vec: 'Vec2D') -> float:
        return self.x * vec.x + self.y * vec.y
    
    # Magnitude
    def magnitude(self) -> float:
        return (self.x * self.x + self.y * self.y) ** 0.5
    
    # Copy the vector
    def copy(self) -> 'Vec2D':
        return Vec2D(self.x, self.y)
    
    # Normalize
    def normalize(self) -> 'Vec2D':
        mag: float = self.magnitude()
        return Vec2D(self.x / mag, self.y / mag)
    
    # Scale all values
    def mult(self, other: 'Vec2D') -> 'Vec2D':
        self.x *= other.x
        self.y *= other.y
        return self
    
    # Add to all values
    def add(self, scalar: float) -> 'Vec2D':
        self.x += scalar
        self.y += scalar
        return self
        
    # Substract from all values
    def sub(self, scalar: float) -> 'Vec2D':
        self.x -= scalar
        self.y -= scalar
        return self

    # Divide from all values
    def div(self, other: 'Vec2D') -> 'Vec2D':
        self.x /= other.x
        self.y /= other.y
        return self
    