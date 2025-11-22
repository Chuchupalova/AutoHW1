class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setitem__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("side_a must be positive")
            super().__setattr__(name, value)
        elif name == "angle_a":
            if not (0 <= value <= 180):
                raise ValueError("angle_a must be between 0 and 180")
            super().__setattr__(name, value)

            super().__setattr__("angle_b", 180 - value)
        else:
            super().__setattr__(name, value)
    def __str__(self):
        return f"Rhombus:" side={self.side_a}, angle={self.angle_a}, angle_b{self.angle_b}"