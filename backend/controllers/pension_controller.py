from utils.pension_utils import calculate_pension_pot
from flask import request

def get_pension_pot():
    data = request.json
    current_salary = data.get('current_salary')
    personal_contribution = data.get('personal_contribution',0)
    employer_contribution = data.get('employer_contribution',0)
    current_pot = data.get('current_pot',0)
    retirement_age = data.get('retirement_age')
    current_age = data.get('current_age')
    
    if not current_salary or not retirement_age or current_age >= retirement_age or current_age < 16:
        return {"error": "Missing/incorrect required fields"}, 400
    
    pension_pot = calculate_pension_pot(current_salary, personal_contribution, employer_contribution, current_pot, retirement_age, current_age)
    return {'Pension pot': pension_pot}