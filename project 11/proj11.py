#https://www.cse.msu.edu/~cse231/Online/Projects/Project11/Project11.pdf


UNITS = ["ml","oz"]
MLperOZ = 29.5735295625  # ml per oz
DELTA = 0.000001

class Volume(object):
    def __init__(self, magnitude= 0, units= "ml"):   # this line is incomplete: parameters needed
        '''Docstring'''





        if type(magnitude) == int or type(magnitude) == float:
            if magnitude >= 0:
                self.magnitude = magnitude  
        
        
        if type (units) == None:
            self.units = "ml"
        else:
            self.units = units


        
    def __str__(self):    # this line is incomplete: parameters needed
        '''Docstring'''
        return (f"{self.magnitude}{type(self.magnitude)}, {self.units}{type(self.units)}")
        
    def __repr__():    # this line is incomplete: parameters needed
        '''Docstring'''
        pass
        
    def is_valid():     # this line is incomplete: parameters needed
        '''Docstring'''
        pass
    
    def get_units():     # this line is incomplete: parameters needed
        '''Docstring'''
        pass
    
    def get_magnitude():  # this line is incomplete: parameters needed
        '''Docstring'''
        pass
    
    def metric():      # this line is incomplete: parameters needed
        '''Docstring'''
        pass
        
    def customary():    # this line is incomplete: parameters needed
        '''Docstring'''
        pass
        
    def __eq__():  # this line is incomplete: parameters needed
        '''Docstring'''
        pass
       
    def add():  # this line is incomplete: parameters needed
        '''Docstring'''
        pass
    
    def sub(): # this line is incomplete: parameters needed
        '''Docstring'''
        pass