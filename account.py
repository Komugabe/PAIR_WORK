class Bank_Account:
	def __init__(self):
		self.total_amount = "0"
		self.name = "Rumbi Gwanzi"
		self.id = "123"
		self.creation_date = "todaydate"

	def welcome(self):
		self.name = "welcome to your Bank_Accountplease enter your pin"
	def print_current_balance (self):
		print('Your current balance:{}'.format(self.total_amount))
	def deposit(self):
			self.total_amount +=float(input('Hello{}, please enter amount'))
			self.print_current_balance()

	def withdraw(self):
				amount_to_withdraw = float(input('Enter amount to withdraw'))
					   if amount_to withdraw > self.total_amount:
					print('Insufficient Balance!!)
					else:
						self.total_amount-=amount_to_withdraw
						self.print_current_balance()
	if _name_=='_main':
	    				print('Your Balance =%' %self.balance)
Bank_Account = Bank_Account
Bank_Account. SavingAccount()
Bank_Account.CheckingAccount()

	while True:
		input_value = int(input('Enter 1 to see your balance,\n2 to deposit,\n3 to withdraw'))
		if input_value==1:
		bank.print_current_balance()
		elif input_value==2:
			bank.deposit()
					elif input_value==3:
						bankwithdraw()
					else:
						print('Please enter a valid input.')