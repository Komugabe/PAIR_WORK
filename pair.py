class Bank_Account:

     # constructor or initializer
    def __init__(self, name, money, date, id):
         self.__name = "name"
         self.__balance = "money" 
         self.__date = "creation_date"  
         self.__id = "id"
    
    def datecheck():
        def check_creation_date(date):
            day = int(date[0:2])
            month = int(date[2:4])
            year = date[4:6]
    
        if ( (day<=days_in_month(month)) and (0<month<13) ):
         return True
        else:
            return False

    def deposit(self, money):
         self.__balance += money

    def withdraw(self, money):
         if self.__balance > money :
             self.__balance -= money
             return money
         else:
             return "Insufficient funds"

    def checkbalance(self):
         return self.__balance


b1 = Bank_Account('Rumbi Gwanzi', 5000, 29/9/2022, 123)
b2 = Bank_Account('Komugabe', 7000, 29/9/2022,2222)
b3 = Bank_Account('Cabellaro', 10000, 29/9/2022,3333)
d1 = 0
d2 = 0
d3 = 0


print("Rumbi Gwanzi: £",b1.checkbalance())
y1 = int(input("Enter 1 if you want to make a withdrawal, enter 2 if you don't"))
if y1 == 1:
   w1= int(input("How much do you want to withdraw"))
   print("Withdrawal: £",b1.withdraw(w1))
else:
   d1= int(input("How much do you want to deposit"))   
   b1.deposit(d1)   
   print("Current Balance:",b1.checkbalance())                                        

print("Komugabe",b2.checkbalance())
y1 = int(input("Enter 1 if you want to make a withdrawal, enter 2 if you don't"))
if y1 == 1:
   w2= int(input("How much do you want to withdraw"))
   print(b2.withdraw(w2))
else:
   d2= int(input("How much do you want to deposit"))
   b2.deposit(d2)

print("Cabellaro:",b3.checkbalance())
y1 = int(input("Enter 1 if you want to make a withdrawal, enter 2 if you don't"))   
if y1 == 1:
   w3= int(input("How much do you want to withdraw"))
   print("Withdrawal:",b3.withdraw(w3))
else:
   d3= int(input("How much do you want to deposit"))
   b3.deposit(d3) 

print("Current Balance:",b3.checkbalance())



print("Rumbi Gwanzi: £",b1.checkbalance())
y1 = int(input("Enter 1 if you want to make a withdrawal, enter 2 if you don't"))
if y1 == 1:
   w1= int(input("How much do you want to withdraw"))
   print("Withdrawal: £",b1.withdraw(w1))
else:
   d1= int(input("How much do you want to deposit"))   
   b1.deposit(d1)   
   print("Current Balance:",b1.checkbalance())                                        


def test_savings_update():
    assert  Bank_Account b1 > 9000

def test_savings_update
    widthdraw = int(input('Enter a number: '))
  assert withdraw > 0 # Test if it true
except AssertionError :
  print("Number is negative")