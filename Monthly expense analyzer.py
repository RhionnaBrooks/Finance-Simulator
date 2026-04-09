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
                    continue
                
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

    
    print("\n" + "*"*30)
    print("      FINANCIAL REPORT")
    print("*"*30)
    print(f"1. Total Count:     {count} categories")
    print(f"2. Total Spent:     ${total}")
    print(f"3. Average Spent:   ${avg:.2f}")
    print(f"4. Highest Bill:    ${highest}")
    print(f"5. Lowest Bill:     ${lowest}")
    print(f"5. Spending Range:  ${spending_range}")
    print("*"*30)

# Run the analyzer
if __name__ == "__main__":
    monthly_expense_analyzer()

