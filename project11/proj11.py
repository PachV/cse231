#   Project11
#   __init__ gets called when a class is being constructed
#   methods will be called when the operants match, like "==", "-","+"
#   and same with calling them manually

UNITS = ["ml","oz"]
MLperOZ = 29.5735295625  # ml per oz
DELTA = 0.000001

class Volume(object):
    def __init__(self, magnitude= 0, units= "ml"):
        if magnitude >= 0:
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

    def __str__(self): 
        '''make a formatted string for the instance
            with 3 decimal places and return it
            
        '''
        if self.magnitude == None or self.magnitude == 0:
            return ("Not a Volume")
        else:
            return (f"{self.magnitude:.3f} {self.units}")
        
    def __repr__(self): 
        '''also makes a formatted string but in more
            detail for debugging purposes
            and return it
        '''
        if self.magnitude == None or self.magnitude == 0 :
            return ("Not a Volume")
        else:
            return (f"{round(self.magnitude,6):.6f} {self.units}")
        
    def is_valid(self):   
        '''check if the magnitude is valid then return the result'''
        if self.magnitude != None:
            return True
        else:
            return False
    
    def get_units(self): 
        '''get the unit of the instance, and return it'''
        if self.magnitude != None:
            return self.units
        else:
            return None
     
    def get_magnitude(self): 
        '''get the magnitude of the instance, and return it'''
        if self.magnitude != None:
            return (self.magnitude)
        else:
            return None
    
    def metric(self):      
        '''change the unit to metric and return a 
            new instance of the class
        '''
        if self.units == "ml":
            return Volume(self.magnitude, self.units)
        else:
            return Volume(self.magnitude*MLperOZ)

    def customary(self):    
        '''change the unit to imperial units and return a 
            new instance of the class
        '''
        if self.units == "oz":
            return Volume(self.magnitude, self.units)
        else:
            return Volume(self.magnitude/MLperOZ, "oz")
        
    def __eq__(self, other): 
        '''this method will be called when two instances of the class
            gets "==" and return true if its equal together
        '''
        if abs(self.magnitude - other.magnitude) < DELTA:
            if self.units == other.units:
                return True
        return False
       
    def add(self,other):
        '''the left operant will be the main one, if the right one is 
            the other unit, it will be converted to the left operant
            and add it together and return a new instance of the class

            if the other is just a int/flt, it will just be added
            to the self.magnitude and return a new instance of the class
        '''
        if type(other) == float or type(other) == int:
            total = self.magnitude + other
            return Volume(total, self.units)

        if self.units == "ml":
            if other.units == "oz":
                total = self.magnitude + other.magnitude * MLperOZ
                return( Volume(total, "ml"))
            else:
                total = self.magnitude + other.magnitude
                return( Volume(total, "ml"))
                
        if self.units == "oz":
            if other.units == "ml":
                total = (self.magnitude) + other.magnitude/MLperOZ
                return Volume(total, "oz")
            else:
                total = (self.magnitude) + other.magnitude
                return Volume(total,"oz")

        return None
    
    def sub(self, other): 
        '''same as add() but with a minus sign'''
        if type(other) == float or type(other) == int:
            total = self.magnitude - other
            return Volume(total, self.units)

        if self.units == "ml":
            if other.units == "oz":
                total = self.magnitude - other.magnitude * MLperOZ
                return( Volume(total, "ml"))
            else:
                total = self.magnitude - other.magnitude
                return Volume(total, "ml")

        if self.units == "oz":
            if other.units == "ml":
                total = (self.magnitude) - other.magnitude/MLperOZ
                return Volume(total, "oz")
            else:
                total = self.magnitude - other.magnitude

                return Volume(total,"oz")
        return None
