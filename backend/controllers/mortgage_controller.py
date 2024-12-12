from utils.mortgage_utils import calculate_mortgage
from flask import request

def get_mortgage_repayment():
    # Get input from the frontend (Flask will automatically pass `request`)
    data = request.json  # Ensure this is a POST request with JSON payload
    amount = data.get('amount')
    interest_rate = data.get('interest_rate')
    years = data.get('years')
    
    if not amount or not interest_rate or not years:
        return {"error": "Missing required fields (amount, interest_rate, years)"}, 400
    
    # Calculate the mortgage repayment
    repayment = calculate_mortgage(amount, interest_rate, years)
    
    # Return the calculated repayment as a JSON response
    return {"repayment": repayment}