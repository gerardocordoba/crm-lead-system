loan_amount = 10000
interest_rate = 0.05
loan_term = 5
payment_frequency = 12
down_payment = 500

total_interest = loan_amount * interest_rate * loan_term
number_of_payments = loan_term * payment_frequency
down_payment_percentage = down_payment / loan_amount * 100
monthly_payment = (loan_amount - down_payment + total_interest) / number_of_payments

print("Loan Amount: $", loan_amount)
print("Interest Rate: ", interest_rate)
print("Loan Term: ", loan_term)
print("Payment Frequency: ", payment_frequency)
print("Down Payment: $", down_payment)
print("Down Payment Percentage: ", down_payment_percentage, "%")
print("Total Interest: $", total_interest)
print("Number of Payments: ", number_of_payments)
print("Monthly Payment: $", monthly_payment)
