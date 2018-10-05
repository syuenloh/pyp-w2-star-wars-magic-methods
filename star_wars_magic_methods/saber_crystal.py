class SaberCrystal:
   def __init__(self,color=(255,0,0)):
       self.red=color[0]
       self.green=color[1]
       self.blue=color[2]
       self.color=(self.red,self.green,self.blue)
   
   def __eq__(self,other):
       return self.color==other.color
   
   def __add__(self,other):
       if type(other)==tuple:
           self.red=self.red+other[0]    
           self.green=self.green+other[1]
           self.blue=self.blue+other[2]
           self.color=(self.red,self.green,self.blue)
           while self.color<=(255,255,255):
               return self
           else:
               self.color=(255,255,255)
               return self
       else:
           self.red=self.red+other.red
           self.blue=self.blue+other.blue
           self.green=self.green+other.green
           self.color=(self.red,self.green,self.blue)
           while self.color<=(255,255,255):
               return self
           else:
               self.color=(255,255,255)
               return self

       
   def __iadd__(self,other):
       if type(other)==tuple:
           self.red=self.red+other[0]
           self.green=self.green+other[1]
           self.blue=self.blue+other[2]
           self.color=(self.red,self.green,self.blue)
           while self.color<=(255,255,255):
               return self
           else:
               self.color=(255,255,255)
               return self

       else:
           self.red=self.red+other.red
           self.blue=self.blue+other.blue
           self.green=self.green+other.green
           self.color=(self.red,self.green,self.blue)
           while self.color<=(255,255,255):
               return self
           else:
               self.color=(255,255,255)
               return self
   
   def __sub__(self,other):
        if type(other)==tuple:
            self.red=self.red-other[0]
            self.green=self.green-other[1]
            self.blue=self.blue-other[2]    
            self.color=(self.red,self.green,self.blue)
            while self.color<=(255,255,255):
                return self
            else:
                self.color=(0,0,0)
                return self
        else:
            self.red=self.red-other.red
            self.blue=self.blue-other.blue
            self.green=self.green-other.green
            self.color=(self.red,self.green,self.blue)
            while self.color<=(255,255,255):
                return self
            else:
                self.color=(0,0,0)
                return self
   
   def __isub__(self,other):
       if type(other)==tuple:
           self.red=self.red-other[0]
           self.green=self.green-other[1]
           self.blue=self.blue-other[2]
           self.color=(self.red,self.green,self.blue)
           return self
       else:
           self.red=self.red-other.red
           self.blue=self.blue-other.blue
           self.green=self.green-other.green
           self.color=(self.red,self.green,self.blue)
           return self
       
   def __contains__(self,other):
        if type(other)==tuple:
            return any(x == y for x, y in zip(self.color, other) if x!=0)
        else:
            return any(x == y for x, y in zip(self.color, other.color) if x!=0)