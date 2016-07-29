import math

class Point:
    '''Point class represents a point in 2D geometric coordinates.'''

    def __init__(self, x=0, y=0):
    	'''
    	Initialise the Point object to the specified coordinates. Default
    	position is the origin.
    	'''
    	self.move(x, y)
    
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
        Theorem. The distance is returned as a float.
        '''
        return math.sqrt(
            (self.x - other_point.x)**2 +
            (self.y - other_point.y)**2)
