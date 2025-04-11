class status:                                                        #Super class (when inherited)
  def __init__(self,display,battery):
    self.display = display
    self.battery = battery
  def breif(self):
    print(f"The status of the phone is metioned below;\n Display:{self.display}  Battery:{self.battery} ")


class copy(status):                                                        #Sub class (when inherited)
  def __init__(self, display, battery,motherboard):
    super().__init__(display, battery)
    self.motherboard = motherboard

obj1 = copy("DAMAGED","75% Health","NOT OK")
print(obj1.display)
obj1.breif()