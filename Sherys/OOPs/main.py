class first:
  __x = 56   #x is an attribute
  print(__x)   #Encapsulation in action

  def z():     #z is a methood 
    a = 100
    print(a)

  def __fckoff(n):   #Encapsulated methood
    print(n)
  __fckoff(10)

first.z()

obj = first    #obj is an Object
obj.z()        #same as first.z()   /line 13



#A blueprint(class) and instance(object) demostration
#or, usage of Constructor 
class school_stats:
  
  x = 30                             #Class attribute

  def fck():                         #Class Method
    pass

  def __init__(self, study_quality, reputation, result, activities):
    self.study_quality = study_quality                                              #Object Attribute
    self.reputation = reputation
    self.result = result
    self.activities = activities
  def detes(self):                                                                  #Object Methood
    print(f"The details for the school are as following :\n Study Quality: {self.study_quality}, Repuation: {self.reputation}, Result: {self.result}")

NGBHS = school_stats("shit", "shit", "medcore", "medcore")
ISC = school_stats("great", "great", "good", "good")
NGGHS = school_stats("shit", "medcore", "bad", "medcore")

print(ISC.study_quality)
ISC.detes()

#If there is "self" in the attribute or methood, it is a object attribute or methood