import json

def calculate_takehome(salary,student_loan_plan,pension_contribution,other_contribution):
    non_taxable_income = 12570
    pension_contribution_currency = salary * pension_contribution / 100
    other_contribution_currency = salary * other_contribution / 100
    salary_post_sacrifice = salary - (pension_contribution_currency + other_contribution_currency)
    if student_loan_plan == 1:
        student_loan_threshold = 22015
    elif student_loan_plan == 2:
        student_loan_threshold = 27295
    
    def calculate_taxable_allowance(salary_post_sacrifice):
        if salary_post_sacrifice > non_taxable_income:
            return salary_post_sacrifice - non_taxable_income
        else:
            return salary_post_sacrifice
        
    def calculate_income_tax(taxable_allowance):
        basic_threshold = 30000
        high_threshold = 112570
        if taxable_allowance < non_taxable_income:
            return 0
        elif taxable_allowance < basic_threshold:
            return taxable_allowance * 0.2
        elif taxable_allowance < high_threshold:
            basic_calc = basic_threshold * 0.2
            high_calc = (taxable_allowance - basic_threshold) * 0.4
            return basic_calc + high_calc
        else:
            basic_calc = basic_threshold * 0.2
            high_calc = (taxable_allowance - basic_threshold) * 0.4
            super_calc = (taxable_allowance - (basic_threshold + high_threshold)) * 0.45
            return basic_calc + high_calc + super_calc
        
    result = {
        
    }
    
    return result