
def Userincome (): 
    while True :  # outer while true loop is used to restart the function until the user a valid entry of income
        try:
            income = int(input("Enter your monthly income after taxes : "))
            
            if income <= 0 :
                print ("Invalid amount entered." +  " Inputs can not be zero or negative.\nTry again!")
            else:
                print ("Total monthly income : ", income)
                return income
        except ValueError:
            print ("Invalid input. Enter a numeric value!")
            # exception handling - tells the users what values are permitted
          
    

def monthly_expense_analyzer():
    
    categories = ["Food", "Rent", "Phone", "Water", "Power", "Other"]
    expenses = []
    
    print("\n" + "="*30)
    print("   MONTHLY EXPENSE TRACKER")
    print("="*30)
    
   
    for item in categories:
        while True:
            try:
              
                amount = int(input(f"Enter {item} amount ($): "))
                
                if amount < 0:
                    print("Amount cannot be negative. Try again.")
                else:
                    expenses.append(amount)
                    break
            except ValueError:
                print("Invalid input. Please enter a whole number.")
    
   
    count = len(expenses)
    total = sum(expenses)
   
    avg = total / count if count > 0 else 0
   
    highest = max(expenses)
    lowest = min(expenses)
    spending_range = highest - lowest
    
    maxitem_index = expenses.index(highest)
    max_item = categories [maxitem_index]

    
    print("\n" + "*"*30)
    print("      FINANCIAL REPORT")
    print("*"*30)
    print(f"1. Total Count:     {count} categories")
    print(f"2. Total Spent:     ${total}")
    print(f"3. Average Spent:   ${avg:.2f}")
    print(f"4. Highest Bill:    ${highest}")
    print(f"5. Lowest Bill:     ${lowest}")
    print(f"6. Spending Range:  ${spending_range}")
    print("*"*30)
    
    return total , max_item , highest 
 


# Run the analyzer
#total, max_item ,highest = monthly_expense_analyzer()

        
def balance ( income , total):
   remaining_bal = income - total
   if remaining_bal <= 0:
       print("\n WARNING! You have a negative or break even balance!")
       print ("Your balance for the year is : ", remaining_bal)
   else:
       print ("Your remaining balance for the year is : ","$", remaining_bal)
       return remaining_bal
 
    

def BudgetAdvice (max_item , highest):
    print ("\n~~~~~~~ BUDGET ADVICE ~~~~~~~ ")
    if max_item == "Food" :
        print ( f"You spent the most amount of money on {max_item} :${highest}" +
                "\nPlease try to cut back on this expense and only purchase essential items")
        print ('''                                        ''')
    elif max_item == "Phone" :
        print ( f"You spent the most amount of money on {max_item} :${highest}" +
               "\nTry to find cheaper ISPs in your area")
        print ('''                                        ''')
    elif max_item == "Water" :
        print ( f"You spent the most amount of money on {max_item} :${highest}" +
                "\nTry to conserve more water ")
        print ('''                                        ''')
    elif max_item == "Power":
        print ( f"You spent the most amount of money on {max_item} :${highest}" +
                "\nTry to conserve more electricity ")
        print ('''                                        ''')
    elif max_item == "Other":
        print ( f"You spent the most amount of money on {max_item} :${highest}" +
                "\n Please cut back on these expenses")
   


import random

class Loan:
    def __init__(self, amount, interest_rate, period_years):
       
        if amount <= 0 or interest_rate <= 0 or period_years <= 0:
            raise ValueError("All inputs must be positive numbers.")
        
        self.amount = amount
        self.base_rate = interest_rate / 100  # Convert percentage to decimal
        self.months = period_years * 12
        self.repayment_schedule = []

    def calculate_monthly_payment(self, current_rate):
         
        # Standard formula: (P * r) / (1 - (1 + r)^-n)
        monthly_rate = current_rate / 12
        if monthly_rate == 0:
            return self.amount / self.months
        
        payment = (self.amount * monthly_rate) / (1 - (1 + monthly_rate)**-self.months)
        return payment

    def generate_schedule(self):
        remaining_balance = self.amount
        total_interest_paid = 0
        
        print(f"\n Repayment Schedule (Initial Rate: {self.base_rate*100:.2f}%)")
        
        for month in range(1, self.months + 1):
            # Random "market fluctuation"
            # Interest rate changes slightly each month (e.g., +/- 0.5%)
            fluctuation = random.uniform(-0.005, 0.005)
            current_rate = self.base_rate + fluctuation
            
            monthly_payment = self.calculate_monthly_payment(current_rate)
            interest_charge = remaining_balance * (current_rate / 12)
            principal_paid = monthly_payment - interest_charge
            remaining_balance -= principal_paid
            
            # Ensure balance doesn't drop below zero due to rounding
            remaining_balance = max(0, remaining_balance)
            
            #  Store data in a list
            self.repayment_schedule.append({
                "Month": month,
                "Payment": round(monthly_payment, 2),
                "Remaining": round(remaining_balance, 2)
            })

    def display_summary(self):
      
        if not self.repayment_schedule:
            print("No schedule generated.")
            return

        print(f"{'Month':<10} | {'Payment':<12} | {'Balance':<12}")
        print("-" * 40)
        for entry in self.repayment_schedule:
            print(f"{entry['Month']:<10} | ${entry['Payment']:<11} | ${entry['Remaining']:<11}")
        
        # Statistics 
        avg_payment = sum(item['Payment'] for item in self.repayment_schedule) / self.months
        print("-" * 40)
        print(f"Total Repayment: ${sum(item['Payment'] for item in self.repayment_schedule):.2f}")
        print(f"Average Monthly Payment: ${avg_payment:.2f}")

def run_loan_simulation():
    #  User system and Exception handling
     print("\n Loan Repayment Simulator")
     try:
        amt = float(input("Enter loan amount: "))
        rate = float(input("Enter annual interest rate (e.g., 5 for 5%): "))
        years = int(input("Enter repayment period (years): "))

        return amt , rate , years
        # OOP implementation
        user_loan = Loan(amt, rate, years)
        user_loan.generate_schedule()
        user_loan.display_summary()
        
     except ValueError :
        print("Invalid input. Enter a numeric value!")
        

        
#main function
choice = 0
while choice <= 3 :
    print ("1. Budget Planner and Monthly Expense Analyzer")
    print ("2. Loan Payment Schedule")
    print ("3. Exit")
    
    choice = int(input("\nPlease enter your choice : "))
    
    if choice == 1 :
        income = Userincome()
        total, max_item ,highest = monthly_expense_analyzer()
        Calculate_bal = balance(income, total)
        advice = BudgetAdvice(max_item, highest)
        
    elif choice == 2 :
        amt, rate, years = run_loan_simulation()
        user_loan = Loan(amt, rate, years)
        user_loan.generate_schedule()
        user_loan.display_summary()
         
    elif choice == 3:
        print ("Exiting.............")
        break
    
    else:
        print("Invalid Choice !")
        choice = 0
    


    

    
    




