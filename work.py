class Bank_Account:
	def __init__(self, name, date, id, total_amount):
		self.name = "Rumbi Gwanzi"
		self.total_amount = "0"
		self.id = "123"
		self.creation_date = "todaydate"
		self.date = "todaydate, pastdate"
		
def deposit(self,total_amount):
	self._balance +=total_amount
def withdraw(self,total_amount):
	if self._balance > total_amount:
		self._balance-= total_amount
		return total_amount
	else:
		return "Insufficient funds"

	def checkbalance(self):
		return self._balance

b1 = Bank_Account('Rumbi Gwanzi', 5000, 123)



print("Obi Ezeakachi: £",b1.checkbalance())
y1 = int(input("Enter 1 if you want to make a withdrawal, enter 2 if you don't"))
if y1 == 1:
   w1= int(input("How much do you want to withdraw"))
   print("Withdrawal: £",b1.withdraw(w1))
else:
   d1= int(input("How much do you want to deposit"))   
   b1.deposit(d1)   
   print("Current Balance:",b1.checkbalance())                                        

