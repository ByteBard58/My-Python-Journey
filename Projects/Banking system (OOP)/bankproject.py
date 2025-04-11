class bank():
  def __init__(self, holder_name, acc_number , current_balance):
    self._holder_name = holder_name
    self._acc_number = acc_number
    self._current_balance = current_balance
  def deposit(self, amount):
    if amount > 0:
      self._current_balance += amount
      print(f"Successfully deposited GBP{amount} from account #{self._acc_number}; New Balance: {self._current_balance}")
    else :
      print('Please Enter A Valid Amount to Deposit')
  def withdraw(self, amount):
    if amount>0:
      if amount <= self._current_balance:
        self._current_balance -= amount 
        print(f"Sucessfully withdrawn GBP{amount} from account #{self._acc_number}; New balance: {self._current_balance}")
      else :
        print(f"Insufficiant Balance, Withdraw Failed ! (Account #{self._acc_number})")
    else :
      print("Please Enter A Valid Amount to Withdraw")
  def showinfo(self):
    print(f"Account Holder's Name: {self._holder_name}")
    print(f"Account Number: {self._acc_number}")
    print(f"Current Balance: {self._current_balance}")

account1 = bank("Sakib Hossain", "82940690427", 12)
account2 = bank("Atif Iqbal Sascha", "82320692199", 126300)
account3 = bank("Mahmud Hasan", "12940690510", 999210000)

account1.deposit(1000)
print(f"\n")
account2.withdraw(10000.97)
print(f"\n")
account3.withdraw(9992100)
print(f"\n")
account1.showinfo()
print(f"\n")
account2.showinfo()
print(f"\n")
account3.showinfo()