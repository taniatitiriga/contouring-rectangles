class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculate_geometry(self):
        """Calculate the lower-left corner, width, and height of the rectangle."""
        lower_left_x = min(self.x1, self.x2)
        lower_left_y = min(self.y1, self.y2)
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        return lower_left_x, lower_left_y, width, height