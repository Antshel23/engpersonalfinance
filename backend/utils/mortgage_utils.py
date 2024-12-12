def calculate_mortgage_repayment(amount, interest_rate, years):
    monthly_interest_rate = interest_rate / 12 / 100
    number_of_payments = years * 12
    repayment = amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
    return round(repayment, 2)