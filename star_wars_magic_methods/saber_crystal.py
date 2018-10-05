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
            color_list=[x+y for x,y in zip(self.color,other)]
        else:
            color_list=[x+y for x,y in zip(self.color,other.color)]
        if max(color_list)>255:
            self.color = tuple([255 if i > 255 else i for i in color_list])
        else:
            self.color=tuple(color_list)
        return self
   
   def __iadd__(self,other): 
        if type(other)==tuple:
            color_list=[x+y for x,y in zip(self.color,other)]
        else:
            color_list=[x+y for x,y in zip(self.color,other.color)]
        if max(color_list)>255:
            self.color = tuple([255 if i > 255 else i for i in color_list])
        else:
            self.color=tuple(color_list)
        return self
   def __sub__(self,other):
        if type(other)==tuple:
            color_list=[x-y for x,y in zip(self.color,other)]
        else:
            color_list=[x-y for x,y in zip(self.color,other.color)]
        if min(color_list)<0:
            self.color = tuple([0 if i < 0 else i for i in color_list])
        else:
            self.color=tuple(color_list)
        return self
                
   def __isub__(self,other):
        if type(other)==tuple:
            color_list=[x-y for x,y in zip(self.color,other)]
        else:
            color_list=[x-y for x,y in zip(self.color,other.color)]
        if min(color_list)<0:
            self.color = tuple([0 if i < 0 else i for i in color_list])
        else:
            self.color=tuple(color_list)
        return self    
   
   def __contains__(self,other):
        if type(other)==tuple:
            return any(x == y for x, y in zip(self.color, other) if x!=0)
        else:
            return any(x == y for x, y in zip(self.color, other.color) if x!=0)