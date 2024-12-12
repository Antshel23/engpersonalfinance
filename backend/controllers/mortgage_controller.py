from utils.mortgage_utils import calculate_mortgage_repayment
from flask import request

def get_mortgage_repayment():
    # Recieve user-input JSON payload
    data = request.json 
    amount = data.get('amount')
    interest_rate = data.get('interest_rate')
    years = data.get('years')
    
    if not amount or not interest_rate or not years:
        return {"error": "Missing required fields"}, 400
    
    # Call utils with params
    repayment = calculate_mortgage_repayment(amount, interest_rate, years)
    
    # Return user-output JSON payload
    return {"Monthly repayment": repayment}