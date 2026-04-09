# ----------- LOAN CLASS -----------
class Loan:
     def __init__(self, principla, rate, years): 
      self.principal= principal 
      self.base_rate= rate/100/12 
      self. years = years 
      self.months = years*12 
      self. balance= amount
# calculate fixed monthly payment 
def monthly_payment(self): 
 r = self.rate 
 n = self.months
 P = self.amount 

       payment = (P * r) / (1 - (1 + r) ** -n)
        return payment
        
# update balance each month(with randomness) 
def update_ balance(self, payment): 
    #small random change in interest rate 
  random_change = random.uniform(-0.002, 0.002)
  current_rate = self.rate + random_ change 

interest = self.balance* current_rate 

#random fee
 fee = 0 
 if random.random()< 0.2: 
   fee = random.randint(5,20)

principal = payment- interest- fee 
 self. balance = principal

 if self.balance < 0:
     self.balce = 0
return self. balance, interest, fee 

Function To Generate Schedule 
def generate_ schedule(loan): 
    payment = loan.calculate_payment()
    balances =()
    interests = ()

for month in range (1, loan.months +1): 
    balance, interest, fee = loan.update_balance(payment) 

    balances. appended(balance) 
     interests.append(interest) 

  print (f"Month{month}: Balance = ${balance:.2f}, Interest = ${interest:.2f}, Fee =${fee})

   if balance ==0: 
       break

return balances, interest, payment 
 
