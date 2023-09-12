# Create a class Vector that has simple (3D) vector operators.

# In your class, you should support the following operations, given Vector a and Vector b:
# a + b # returns a new Vector that is the resultant of adding them
# a - b # same, but with subtraction
# a == b # returns true if they have the same magnitude and direction
# a.cross(b) # returns a new Vector that is the cross product of a and b
# a.dot(b) # returns a number that is the dot product of a and b
# a.to_tuple() # returns a tuple representation of the vector.
# str(a) # returns a string representation of the vector in the form "<a, b, c>"
# a.magnitude # returns a number that is the magnitude (geometric length) of vector a.
# a.x # gets x component
# a.y # gets y component
# a.z # gets z component
# Vector([a,b,c]) # creates a new Vector from the supplied 3D array.
# Vector(a,b,c) # same as above

import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other):
        return self.magnitude() == other.magnitude()

    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def to_tuple(self):
        return (self.x, self.y, self.z)

    def __str__(self):
        return f"<{self.x}, {self.y}, {self.z}>"

    @property
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

