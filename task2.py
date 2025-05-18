class Calculator:
    def __init__(self,num1,num2):
     self.num1=num1
     self.num2=num2
     
   #function   
    def add(self):
     return self.num1 + self.num2
    def sub(self):
     return self.num1 - self.num2
    def multi(self):
     return self.num1 * self.num2
    def div(self):
        if self.num2==0:
         return"ERROR....Then number cannot be zero"
        return self.num1 / self.num2
calc=Calculator(num1,num2)
    
     #user input number
num1=float(input("Enter your first number:"))
num2=float(input("Enter your second number:"))
#create calculator object

#input operator
print(f"Choose your operator(+,-,*,/)")
operator=(input("Enter your operator"))
if operator== '+':
 print(f"The sum is:{calc.add()}")
elif operator== '-':
 print(f"The sub is:{calc.sub()}")
elif operator== '*':
 print(f"The multi is:{calc.multi()}")
elif operator== '/':

 print(f"The div is:{calc.div()}")