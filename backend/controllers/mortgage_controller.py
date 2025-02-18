from utils.mortgage_utils import calculate_mortgage_repayment
from flask import request, jsonify
import json

def get_user_mortgage_info():
    data = request.json 
    amount = data.get('amount')
    interest_rate = data.get('interest_rate')
    years = data.get('years')
    
    if not amount or not interest_rate or not years:
        return {"error": "Missing required fields"}, 400
    else:
        return {
            "amount": amount,
            "interest_rate": interest_rate,
            "years": years,
         }

def return_mortgage_info():
    user_input = get_user_mortgage_info()
    
    if isinstance(user_input, dict) and "error" in user_input:
        return jsonify(user_input),400

    mortgage_data = json.loads(calculate_mortgage_repayment(**user_input))
    return mortgage_data, 200