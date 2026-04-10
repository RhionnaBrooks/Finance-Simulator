import random

class Loan:
    def __init__(self, amount, interest_rate, period_years):
        # Person B: Input validation/Exception handling
        if amount <= 0 or interest_rate <= 0 or period_years <= 0:
            raise ValueError("All inputs must be positive numbers.")
        
        self.amount = amount
        self.base_rate = interest_rate / 100  # Convert percentage to decimal
        self.months = period_years * 12
        self.repayment_schedule = []

    def calculate_monthly_payment(self, current_rate):
        # Person A: Core repayment formula
        # Standard formula: (P * r) / (1 - (1 + r)^-n)
        monthly_rate = current_rate / 12
        if monthly_rate == 0:
            return self.amount / self.months
        
        payment = (self.amount * monthly_rate) / (1 - (1 + monthly_rate)**-self.months)
        return payment

    def generate_schedule(self):
        # start_span)Person A & B: Core logic + Randomness
        remaining_balance = self.amount
        total_interest_paid = 0
        
        print(f"\n Repayment Schedule (Initial Rate: {self.base_rate*100:.2f}%)")
        
        for month in range(1, self.months + 1):
            # Person B: Random "market fluctuation"
            # Interest rate changes slightly each month (e.g., +/- 0.5%)
            fluctuation = random.uniform(-0.005, 0.005)
            current_rate = self.base_rate + fluctuation
            
            monthly_payment = self.calculate_monthly_payment(current_rate)
            interest_charge = remaining_balance * (current_rate / 12)
            principal_paid = monthly_payment - interest_charge
            remaining_balance -= principal_paid
            
            # Ensure balance doesn't drop below zero due to rounding
            remaining_balance = max(0, remaining_balance)
            
            # Person B: Store data in a list
            self.repayment_schedule.append({
                "Month": month,
                "Payment": round(monthly_payment, 2),
                "Remaining": round(remaining_balance, 2)
            })

    def display_summary(self):
        # Person B: Output display
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
        print(f"Total Repayment: ${sum(item['Payment'] for item in self.repayment_schedule):.2g}")
        print(f"Average Monthly Payment: ${avg_payment:.2f}")

def run_loan_simulation():
    # Person B: User system and Exception handling
    print("\n Loan Repayment Simulator")
    try:
        amt = float(input("Enter loan amount: "))
        rate = float(input("Enter annual interest rate (e.g., 5 for 5%): "))
        years = int(input("Enter repayment period (years): "))

        # OOP implementation
        user_loan = Loan(amt, rate, years)
        user_loan.generate_schedule()
        user_loan.display_summary()

    except ValueError as e:
        print(f"Invalid input: {e}")