from utils.pension_utils import calculate_pension_pot
from flask import request, jsonify
import json

def get_user_pension_input():
    data = request.json
    current_salary = data.get('current_salary')
    personal_contribution = data.get('personal_contribution', 0)
    employer_contribution = data.get('employer_contribution', 0)
    current_pot = data.get('current_pot', 0)
    retirement_age = data.get('retirement_age')
    current_age = data.get('current_age')
    
    if not current_salary or not retirement_age or current_age >= retirement_age or current_age < 16 :
        return {"error": "Missing/incorrect required fields"}, 400
    else:
        return {
            "current_salary": current_salary,
            "personal_contribution": personal_contribution,
            "employer_contribution": employer_contribution,
            "current_pot": current_pot,
            "retirement_age": retirement_age,
            "current_age": current_age,
        }

def return_pension_pot():
    user_input = get_user_pension_input()
    
    if isinstance(user_input, dict) and "error" in user_input:
        return jsonify(user_input), 400
    
    pension_pot_data = json.loads(calculate_pension_pot(**user_input))
    return pension_pot_data, 200