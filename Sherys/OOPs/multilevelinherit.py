class factory:
  def __init__(self, material, size):
    self.material = material
    self.size = size


class seccondfactory(factory):
  def __init__(self, material, size, cost):
    super().__init__(material, size)
    self.cost = cost

class finalfactory(seccondfactory):
  def __init__(self, material, size, cost, design):
    super().__init__(material, size, cost)
    self.design = design

# obj1 = finalfactory()         #Demands material, size, cost, design


#This is multi level inheritance. It's just like the inheritance we see in real life. 

# You can consider the first class which is named factory as the grandfather, the seccondfactory as father and the finalfactory as the grandson.
# When the grandfather dies, The father inherit his property.
#  And when the father dies the grandson inheritance the father's properties.
#  Here you can notice that the father's property includes the property. 
# He earned himself and the property he inherited from the grandfather,
#  so the grandson inheritance, both his father's and his grandfather's properties.

# In this example, the seccondfactory class inherits the blueprint of the factory class and the finalfactory class inherits the seccondfactory's blueprint. Which actually means that the finalfactory processes both the secondfactory's and the factory's blueprints.




