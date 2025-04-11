class id1:
  def __init__(self, name, planet):
    self.name = name 
    self.planet = planet
  def showid(self):
    print(f"I'm from {self.planet}")
class id2(id1):
  def showid(self):
    super().showid()
    print(f"I'm from {self.planet} and see u not for mind")

alien1 = id2("Sdx","JKF-24")       #The one which is called here has more priority, like: id2
alien1.showid()
