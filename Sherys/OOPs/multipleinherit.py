class factory:
  def __init__(self, material, size):
    self.material = material
    self.size = size

class seccondfactory(factory):
  def __init__(self, material, size, cost):
    super().__init__(material, size)
    self.cost = cost

class thirdfactory(factory,seccondfactory):                                        # Multiple Inheritence
  def __init__(self, material, size):
    super().__init__(material, size)

obj = thirdfactory()                                                  

#In multiple inheritance, The init of the inheritance which is mentioned earlier gets executed. In this case, it is "factory", not "seccondfactory"     (check line 11)