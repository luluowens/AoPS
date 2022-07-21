# Paste your code into this box
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)^12) / 12.0
def calculate_final_balance(balance, interest_rate, monthly_payment) :
    monthly_interest = interest_rate / 12.0
    for i in range(12) :
        unpaid = balance - monthly_payment
        balance = unpaid + (monthly_interest * unpaid)
    return balance
    
def min_monthly_pay(balance, annual_interest) :
    monthly_pay_lower = round(balance / 12.0, 2)
    monthly_pay_upper = round((balance * pow(1 + annual_interest / 12.0, 12)) / 12.0, 2)
    while monthly_pay_lower < monthly_pay_upper :
        monthly_pay_mid = round(monthly_pay_lower + (monthly_pay_upper-monthly_pay_lower) // 2, 2)
        new_balance = round(calculate_final_balance(balance, annual_interest, monthly_pay_mid), 1)
        if new_balance == 0.0 or new_balance == 0.1 or new_balance == -0.1:
            return monthly_pay_mid
        elif new_balance > 0 :
            monthly_pay_lower = round(monthly_pay_mid + 0.01, 2)
        else :
            monthly_pay_upper = round(monthly_pay_mid - 0.01, 2)
            
# print("Lowest Payment: " + str(min_monthly_pay(320000, 0.2)))
print("Lowest Payment: " + str(min_monthly_pay(999999, 0.18)))
    