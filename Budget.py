
#function defintion 1
def Userincome (): 
    while True :
        try:
            income = int(input("Enter your monthly income after taxes : "))
            
            if income <= 0 :
                print ("Invalid amount entered." +  " Inputs can not be zero or negative.\nTry again!")
            else:
                print ("Total monthly income : ", income)
                return income
        except ValueError:
            print ("Invalid input. Enter a numeric value!") # exception handling - tells the users what values are permitted
          
    
# income = Userincome()    

#function definiton 2
def Expenses_Details ():
    while True :
        try:
            # inner while true loop used to check the input value of the respective expenses 
            while True:
                food = round(float(input("\nEnter total food expense: ")),2)
                if food <= 0 :
                    print ("Invalid amount entered." +  " Inputs can not be zero or negative.\nTry again!")
                else:
                    break
           
            while True :
                
                mortgage = round(float(input("Enter total mortgage or rent expense: ")),2)
                if mortgage <= 0 :
                    print ("Invalid amount entered." +  " Inputs can not be zero or negative.\nTry again!")
                else:
                    break
            while True:
                telephone = round(float(input("Enter total telephone expense : ")),2)
                if telephone <=0 :
                    print ("Invalid amount entered." +  " Inputs can not be zero or negative.\nTry again!")
                else:
                    break
               
            while True :
                water =  round(float(input("Enter total water expense : ")),2)
                if water <= 0 :
                    print ("Invalid amount entered." +  " Inputs can not be zero or negative.\nTry again!")
                else:
                    break
                
            while True :
                electricity = round(float(input("Enter total electricity expense : ")),2)
                if electricity <= 0 :
                    print ("Invalid amount entered." +  " Inputs can not be zero or negative.\nTry again!")
                else:
                    break
            while True :
                other_exp = round(float(input("Enter total other expenses : ")),2)
                if other_exp <= 0 :
                    print ("Invalid amount entered." +  " Inputs can not be zero or negative.\nTry again!")
                else:
                    break
                
            # dictionary used to store the name and values of each expense
            expenses = {
            "food" :  food ,
            "mortgage" :mortgage,
            "telephone" : telephone,
            "water" : water,
            "electricity" : electricity ,
            "other expenses" : other_exp
            }
            
            
            total_exp = sum (expenses.values())
            max_expense = max (expenses.values())
            min_expense = min (expenses.values())
    
            max_item = " "
            min_item = " "
    
            for key in expenses : # loop used to check each key in the dictionary
            
                if expenses[key] == max_expense: # compares the value of key to see if it matches with the value of the maximum exp
                    max_item = key
                if expenses [key] == min_expense:
                    min_item = key
        
            print ("\n~~~~~ EXPENSES SUMMARY ~~~~~~~~")
            print ("Total yearly expenses : ", total_exp)
            print ("Maximum amount of money was spent on:",max_item ,"-","$",max_expense)
            print ("Minimum amount of money was spent on:", min_item, "-","$",min_expense)
            
            #python stores multiple return statements as a tuple
            return total_exp, max_item , max_expense 
           
            
        except ValueError :
           print ("Invalid input. Enter a numeric value!") # exception handling - tells the users what values are permitted
           break
#unpacking the tuple         
total_exp, max_item, max_expense = Expenses_Details()

#function definition 3      
def balance ( income , total_exp):
   remaining_bal = income - total_exp
   if remaining_bal <= 0:
       print("\n WARNING! You have a negative or break even balance!")
       print ("Your balance for the year is : ", remaining_bal)
   else:
       print ("Your remaining balance for the year is : ", remaining_bal)
       return remaining_bal
 
# Calculate_bal = balance(income, total_exp)
    
# function defintion 4
def BudgetAdvice (max_item , max_expense):
    print ("\n~~~~~~~ BUDGET ADVICE ~~~~~~~ ")
    if max_item == "mortgage" :
        print ( f"You spent the most amount of money on {max_item} : ${max_expense}" + "\n This is a fixed expense so payments can not be minimized" +
        " \nTry to cut back on the  remaining expenses")
    elif max_item == "food" :
        print ( f"You spent the most amount of money on {max_item} :${max_expense}" +
                "\nPlease try to cut back on this expense and only purchase essential items")
    elif max_item == "telephone" :
        print ( f"You spent the most amount of money on {max_item} :${max_expense}" +
               "\nTry to find cheaper ISPs in your area")
    elif max_item == "water" :
        print ( f"You spent the most amount of money on {max_item} :${max_expense}" +
                "\nTry to conserve more water ")
    elif max_item == "electricity":
        print ( f"You spent the most amount of money on {max_item} :${max_expense}" +
                "\nTry to conserve more electricity ")
    elif max_item == "other expenses":
        print ( f"You spent the most amount of money on {max_item} :${max_expense}" +
                "\n Please cut back on these expenses")
        
# advice = BudgetAdvice(max_item, max_expense)    
       
