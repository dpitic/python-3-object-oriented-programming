import math

class Point:
    '''Point class represents a point in 2D.'''
    
    def move(self, x, y):
        '''Move the point to the given coordinates.'''
        self.x = x
        self.y = y

    def reset(self):
        '''Move the point to the origin.'''
        self.move(0, 0)

    def calculate_distance(self, other_point):
        '''
        Calculate the distance to the specified point using the Pythagoras
        Theorem.
        '''
        return math.sqrt(
            (self.x - other_point.x)**2 +
            (self.y - other_point.y)**2)
