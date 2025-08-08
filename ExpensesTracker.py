import datetime

def add_expense(amount, category):
         date = datetime.date.today()
         with open("expenses.txt", "a") as file:
            file.write(f"{date},{i},{category},{amount}\n")
         print("Expense added!")

def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No expenses recorded yet.")

i=1
while(i!=0):
    
        n=int(input("Enter 1 to add expense and 2 to view expense"))
        if(n==1):
               amt=input("Enter the amount:")
               category=input("Enter the expense:")
               i=input("Enter the sl no:")
               add_expense(amt,category)
        else:
               view_expenses()  
     



