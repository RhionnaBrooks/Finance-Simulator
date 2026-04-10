


def Userincome (): 
    while True :  #while true loop is used to restart the function until the user enters a valid entry for income
        try:
            income = int(input("Enter your monthly income after taxes : "))
            
            if income <= 0 :
                print ("Invalid amount entered." +  " Inputs can not be zero or negative.\nTry again!")
            else:
                print ("Total monthly income : ", income)
                return income
        except ValueError:
            print ("Invalid input. Enter a numeric value!") # exception handling - tells the users what values are permitted
          
    
income = Userincome()    

def monthly_expense_analyzer():
    
    categories = ["Food", "Rent", "Phone", "Water", "Power", "Other"]
    expenses = []
    
    print("\n" + "="*30)
    print("   MONTHLY EXPENSE TRACKER")
    print("="*30)
    
   
    for item in categories:
        while True:  #while true loop is used to restart the function until the user enters a valid entry for amount
            try:
              
                amount = int(input(f"Enter {item} amount ($): "))
                
                if amount < 0:
                    print("Amount cannot be negative. Try again.")
                else:
                    expenses.append(amount) # updates the list
                    break
            except ValueError:
                print("Invalid input. Please enter a whole number.")
    
   
    count = len(expenses)
    total = sum(expenses)
   
    avg = total / count if count > 0 else 0
   
    highest = max(expenses)
    lowest = min(expenses)
    spending_range = highest - lowest
    
    maxitem_index = expenses.index(highest) #used to find the index of the highest value in the list
    max_item = categories [maxitem_index]  # used to store the value of the highest value to the name in the corresponding index

    
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

   #python stores multiple return statements as a tuple
    return total , max_item , highest 
 


# Run the analyzer by unpacking the tuple
total, max_item ,highest = monthly_expense_analyzer()

        
def balance ( income , total):
   remaining_bal = income - total
   if remaining_bal <= 0:
       print("\n WARNING! You have a negative or break even balance!")
       print ("Your balance for the year is : ", remaining_bal)
   else:
       print ("Your remaining balance for the year is : ","$", remaining_bal)
       return remaining_bal
 
Calculate_bal = balance(income, total)
    

def BudgetAdvice (max_item , highest):
    print ("\n~~~~~~~ BUDGET ADVICE ~~~~~~~ ")
    if max_item == "Food" :
        print ( f"You spent the most amount of money on {max_item} :${highest}" +
                "\nPlease try to cut back on this expense and only purchase essential items")
    elif max_item == "Phone" :
        print ( f"You spent the most amount of money on {max_item} :${highest}" +
               "\nTry to find cheaper ISPs in your area")
    elif max_item == "Water" :
        print ( f"You spent the most amount of money on {max_item} :${highest}" +
                "\nTry to conserve more water ")
    elif max_item == "Power":
        print ( f"You spent the most amount of money on {max_item} :${highest}" +
                "\nTry to conserve more electricity ")
    elif max_item == "Other":
        print ( f"You spent the most amount of money on {max_item} :${highest}" +
                "\n Please cut back on these expenses")
        
advice = BudgetAdvice(max_item, highest)    
    
        
        
        
    


    

    
    

