class student():
  def __init__(self,name,grade,section,roll):
    self.name = name
    self.grade = grade 
    self.section = section
    self.roll = roll
    self.marks = {}

  def addmarks(self,sub,marks):
    if sub in self.marks :
      print(f"The subject '{sub}' is alreeady registered")
    else :
      self.marks[sub] = int(marks)

  def avg_marks(self):
    if not self.marks:
      print("No marks were given")
      return 0
    else:
      total_marks = sum(self.marks.values())
      average_marks = total_marks/len(self.marks)
      return average_marks
  
  def presentation(self):
    print(f"Student's name: {self.name}")
    print(f"Roll Number: {self.roll}")
    print(f"Grade: {self.grade}")
    print(f"Section: {self.section}")
    print(f"Marks: {self.marks}")
    print(f"Average Marks: {self.avg_marks()}")

bitch1 = student("Zubayer Rahman", "Ten", "B", "04")
bitch2 = student("Atif Iqbal Sascha", "Ten", "A", "19")
bitch3 = student("Sakib Hossain", "Ten", "A", "13")

bitch1.addmarks("General Math", "98")
bitch1.addmarks("Higher Math", "98")
bitch1.addmarks("Chemistry", "99")
bitch1.addmarks("Physics", "95")

bitch2.addmarks("General Math", "100")
bitch2.addmarks("Higher Math", "100")
bitch2.addmarks("Chemistry", "94")
bitch2.addmarks("Physics", "100")

bitch3.addmarks("General Math", "88")
bitch3.addmarks("Higher Math", "85")
bitch3.addmarks("Chemistry", "81")
bitch3.addmarks("Physics", "95")



bitch1.presentation()
print(f"\n")
bitch2.presentation()
print(f"\n")
bitch3.presentation()
