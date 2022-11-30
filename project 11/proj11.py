#https://www.cse.msu.edu/~cse231/Online/Projects/Project11/Project11.pdf


UNITS = ["ml","oz"]
MLperOZ = 29.5735295625  # ml per oz
DELTA = 0.000001

class Volume(object):
    def __init__(self, magnitude= 0, units= "ml"):   # this line is incomplete: parameters needed



        if magnitude >=0:
            if type(magnitude) == int or type(magnitude) == float:
                self.magnitude = magnitude
                self.units = units
            else:
                self.magnitude = 0
                self.units = None
        else:
            self.magnitude = 0
            self.units = None

        if units not in UNITS:
            self.magnitude = None
            self.units = None


        
    def __str__(self):    # this line is incomplete: parameters needed
        '''Docstring'''
        if self.magnitude == None or self.magnitude == 0:
            return ("Not a Volume")
        else:
            return (f"{self.magnitude:.3f} {self.units}")
        
    def __repr__(self):    # this line is incomplete: parameters needed
        '''Docstring'''
        if self.magnitude == None or self.magnitude == 0 :
            return ("Not a Volume")
        else:
            return (f"{round(self.magnitude,6):.6f} {self.units}")
        
        
    def is_valid(self):     # this line is incomplete: parameters needed
        '''Docstring'''
        if self.magnitude != None:
            return True
        else:
            return False
    
    def get_units(self):     # this line is incomplete: parameters needed
        '''Docstring'''
        if self.magnitude != None:
            return self.units
        else:
            return None
    
    def get_magnitude(self):  # this line is incomplete: parameters needed
        '''Docstring'''
        if self.magnitude != None:
            return self.magnitude
        else:
            return None
    
    def metric(self):      # this line is incomplete: parameters needed
        '''Docstring'''
        if self.units in UNITS:
            return self.units
        else:
            return None

    def customary(self):    # this line is incomplete: parameters needed
        '''Docstring'''
        if self.units 
        
    def __eq__(self): #this line is incomplete: parameters needed
        '''Docstring'''
        pass
       
    def add(self):  # this line is incomplete: parameters needed
        '''Docstring'''
        pass
    
    def sub(self): # this line is incomplete: parameters needed
        '''Docstring'''
        pass

G = Volume(10.123455123, "ml")
print(G.__repr__())
