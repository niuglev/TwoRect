class TwoRect:
    """
    Attributes:
    - x1: The x-coordinate of the first rectangle's top left corner. (int)
    - y1: The y-coordinate of the first rectangle's top left corner. (int)
    - x2: The x-coordinate of the first rectangle's bottom right corner. (int)
    - y2: The y-coordinate of the first rectangle's bottom right corner. (int)
    - x_1: The x-coordinate of the second rectangle's top left corner. (int)
    - y_1: The y-coordinate of the second rectangle's top left corner. (int)
    - x_2: The x-coordinate of the second rectangle's bottom right corner. (int)
    - y_2: The y-coordinate of the second rectangle's bottom right corner. (int)

    Methods:
    - distance_center: Calculates the distance between the centers of the two rectangles.
      Returns the distance as a float.
    - distance_angle: Calculates the sum of the distances between the top left points and bottom right points
     of the two rectangles. Returns the sum as a float.
"""

    def __init__(self, x1, y1, x2, y2, x_1, y_1, x_2, y_2):
        """
            Initializes a TwoRect object with the given coordinates of the rectangles' corners.

            Parameters:
            - x1: The x-coordinate of the first rectangle's top left corner. (int)
            - y1: The y-coordinate of the first rectangle's top left corner. (int)
            - x2: The x-coordinate of the first rectangle's bottom right corner. (int)
            - y2: The y-coordinate of the first rectangle's bottom right corner. (int)
            - x_1: The x-coordinate of the second rectangle's top left corner. (int)
            - y_1: The y-coordinate of the second rectangle's top left corner. (int)
            - x_2: The x-coordinate of the second rectangle's bottom right corner. (int)
            - y_2: The y-coordinate of the second rectangle's bottom right corner. (int)
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2

    def distance_center(self):
        """
        Calculates and returns the distance between the centers of the two rectangles as a float.

        Returns:
        - distance: The distance between the centers of the two rectangles. (float)
        """
        try:
            int(self.x1)
            int(self.y1)
            int(self.x2)
            int(self.y2)
            int(self.x_1)
            int(self.y_1)
            int(self.x_2)
            int(self.y_2)
        except ValueError:
            return 'Incorrect input'
        xcenter = (self.x1 + self.x2) / 2
        ycenter = (self.y1 + self.y2) / 2
        x_center = (self.x_1 + self.x_2) / 2
        y_center = (self.y_1 + self.y_2) / 2
        distance = ((x_center - xcenter) ** 2 + (y_center - ycenter) ** 2) ** (1 / 2)
        return str(round(distance, 3))

    def distance_angle(self):
        """
                Calculates and returns the sum of the distances between the top left points and bottom right points
                  of the two rectangles as a float.

                Exceptions:
                ValueError: Raised if any of the input coordinates are not integers

                Returns:
                - sum_distance: The sum of the distances between the top left points and bottom right points
                  of the two rectangles. (float)

                Examples:
                point1 = Point(1, 2)
                point2 = Point(3, 4)
                point_1 = Point(5, 6)
                point_2 = Point(7, 8)
                result = point1.distance_angle()  # Returns the total distance between point1 and point_1
                """
        try:
            int(self.x1)
            int(self.y1)
            int(self.x2)
            int(self.y2)
            int(self.x_1)
            int(self.y_1)
            int(self.x_2)
            int(self.y_2)
        except ValueError:
            return 'Incorrect input'
        l_distance = ((self.x1 - self.x_1) ** 2 + (self.y1 - self.y_1) ** 2) ** (1 / 2)
        r_distance = ((self.x2 - self.x_2) ** 2 + (self.y2 - self.y_2) ** 2) ** (1 / 2)
        return round(r_distance + l_distance, 3)
