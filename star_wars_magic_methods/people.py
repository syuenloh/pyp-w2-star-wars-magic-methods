class People(object):
    def __init__(self, name, dark_side=False):
        self.name=name
        self.dark_side=dark_side
        self.light_side=not dark_side
        
    def __str__(self):
        return self.name
    
    def __call__(self):
        return ("Help me {}, you're my only hope.".format(self.name))

    def __truediv__(self,other):
        if type(other)==int or type(other)==float:
            raise TypeError
        return("{} swings a lightsaber at {}.".format(self.name,other.name))
        
    def __mul__(self,other):
        if type(other)==int or type(other)==float:
            raise TypeError
        return("{} throws a thermal detonator at {}!".format(self.name,other.name))
    
    def __rshift__(self,other):
        if type(other)==int or type(other)==float:
            raise TypeError
        return("{} uses the force to push {} away from them.".format(self.name,other.name))

    def __lshift__(self,other):
        if hasattr(other, '__class__'):
            return("{} uses the force to pull {} towards them.".format(self.name,other.name))
        raise TypeError

    def __neg__(self):
        self.light_side=False
        self.dark_side=True
    
    def __pos__(self):
        self.light_side=True
        self.dark_side=False

    def __invert__(self):
        self.dark_side=not self.dark_side
        self.light_side=not self.light_side
    
    def __xor__(self,other):
        return("{} force chokes {}.".format(self.name,other.name))
    
    def __eq__(self,other):
       if other.name=="Han Solo":
           return ("{} shoots {}. BECAUSE HAN SHOOTS FIRST.".format(other.name,self.name))
       else:
           return ("{} shoots {}.".format(self.name,other.name))