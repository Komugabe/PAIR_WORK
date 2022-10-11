import pytest
class BankAccount():
	def __init__(self,name,balance,ID,creationdate):
		self.name = name
		self.balance = balance
		self.creationdate = creationdate
		self.ID = ID

 	def datecheck():
        def check_creationdate(date):
          day = int(date[0:2])
            month = int(date[2:4])
            year = date[4:6]
    
        if ( (day<=days_in_month(month)) and (0<month<13) ):
         return True
       else:
            return False

	def Depodit(self,d):
		self.balance =self.balance + d

	def withdrawal(self,w):
		if(self,balance < w):
			print("Insufficient balance !")
		else:
			self.balance = self.balance - w

class SavingsAccount(BankAccount):
    def __init__(self, date):
        self.creationdate = creationdate
        def. withdrawal(BankAccount,creationdate):
        	if (BankAccount,creationdate >= 6month):
        		print("withdrawal")
        	else:
        		Does not allow overdraft

class CheckingAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance
        def. withdrawal(BankAccount,balance):
        	if (BankAccount,balance <0):
        		print("withdrawal")
        	else:
        		$30 penaltyfee


    BankAccount('Rumbi Gwanzi', 5000, 29/9/2022, 123)
    print("BankAccount")