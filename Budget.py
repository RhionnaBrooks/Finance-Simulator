''''👤 Person A (you)

Focus on:

income input function 
savings goal input
basic budget setup (starting values)
maybe simple validation (no negatives, etc.)

👉 You are basically handling what the user starts with'''


def Userincome ():
    while True :
        try:
            income = int(input("Enter your yearly income after tax : "))
            
            if income <= 0 :
                print ("Invalid amount entered." +  " Inputs can not be zero or negative.\nTry again!")
            else:
                print ("Total yearly income : ", income)
                return income
            
        except ValueError:
            print ("Invalid input. Enter a numeric value!") # exception handling - tells the users what values are permitted
         

def Expenses_Details ():
    while True :
        try:
            
            expenses = {
            "food" : round(float(input("Enter total amount spent on food : ")),2),
            "mortgage" :round(float(input("Enter total mortgage or rent expense: ")),2),
            "telephone" : round(float(input("Enter total telephone expense : ")),2),
            "water" : round(float(input("Enter total water expense : ")),2),
            "electricity" : round(float(input("Enter total electricity expense : ")),2),
            "other expenses" : round(float(input("Enter total other expenses : ")),2)}
            
            total_exp = sum (expenses.values())
            max_expense = max (expenses.values())
            min_expense = min (expenses.values())
    
            max_item = " "
            min_item = " "
    
            for name in expenses :
            
                if expenses[name] == max_expense:
                    max_item = name
                elif expenses [name] == min_expense:
                    min_item = name
        
      
            print ("Total yearly expenses : ", total_exp)
            print ("Maximum amount of money was spent on:",max_item ,"-","$",max_expense)
            print ("Minimum amount of money was spent on:", min_item, "-","$",min_expense)
            break
        except ValueError :
           print ("Invalid input. Enter a numeric value!") # exception handling - tells the users what values are permitted
           
result = Expenses_Details()

        
def balance ( income , expense):
    remaining_bal = income - expenses
    

    
    
    
    


    

    
    