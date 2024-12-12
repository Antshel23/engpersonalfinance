def calculate_pension_pot(current_salary, personal_contribution, employer_contribution, current_pot, retirement_age, current_age):
    personal_contribution = current_salary * personal_contribution / 100
    employer_contribution = current_salary * employer_contribution / 100
    total_contribution = personal_contribution + employer_contribution
    years_to_retirement = retirement_age - current_age
    portfolio_return = 1.0425
    
    for year in range(1, years_to_retirement + 1):
        current_pot += total_contribution * portfolio_return
    
    return round(current_pot, 2)