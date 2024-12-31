import json

def calculate_pension_pot(current_salary, personal_contribution, employer_contribution, current_pot, retirement_age, current_age):
    years_to_retirement = retirement_age - current_age
    salary_growth_rate = 1.02
    annual_portfolio_charge = 0.0075
    inflation_rate = 0.02
    
    good_portfolio_return = ((1.055 * (1 - annual_portfolio_charge)) / (1 + inflation_rate))
    med_portfolio_return = ((1.035 * (1 - annual_portfolio_charge)) / (1 + inflation_rate))
    inflation_match_portfolio_return = ((1.02 * (1 - annual_portfolio_charge)) / (1 + inflation_rate))
    inflation_loss_portfolio_return = ((1.0 * (1 - annual_portfolio_charge)) / (1 + inflation_rate))
    
    def calculate_pot(return_rate):
        pot = current_pot
        salary = current_salary
        for year in range(1, years_to_retirement + 1):
            salary *= salary_growth_rate
            annual_contribution = ((personal_contribution + employer_contribution) * salary) / 100
            pot += annual_contribution
            pot *= return_rate
        return round(pot, 0)
    
    def calculate_drawdown(pot):
        annual_drawdown = pot * 0.04
        return round(annual_drawdown, 0)
    
    def calculate_lumpsum_drawdown(pot):
        lumpsum = pot * 0.25
        pot -= lumpsum
        annual_drawdown = pot * 0.04
        return {
            "lumpsum": round(lumpsum),
            "drawdown": round(annual_drawdown, 0)
        }
    result = {
        "current_salary": current_salary,
        "personal_contribution": personal_contribution,
        "employer_contribution": employer_contribution,
        "current_pot": current_pot,
        "retirement_age": retirement_age,
        "current_age": current_age,
        "years_to_retirement": years_to_retirement,
        "calculated_pots": {
            "high": calculate_pot(good_portfolio_return),
            "medium": calculate_pot(med_portfolio_return),
            "inflation_match": calculate_pot(inflation_match_portfolio_return),
            "inflation_loss": calculate_pot(inflation_loss_portfolio_return)
        },
        "drawdown": {
            "high": calculate_drawdown(calculate_pot(good_portfolio_return)),
            "medium": calculate_drawdown(calculate_pot(med_portfolio_return)),
            "inflation_match": calculate_drawdown(calculate_pot(inflation_match_portfolio_return)),
            "inflation_loss": calculate_drawdown(calculate_pot(inflation_loss_portfolio_return))
        }, 
        "lumpsum_drawdown": {
            "high": {
                "lumpsum": calculate_lumpsum_drawdown(calculate_pot(good_portfolio_return))["lumpsum"],
                "drawdown": calculate_lumpsum_drawdown(calculate_pot(good_portfolio_return))["drawdown"]
            },
            "medium": {
                "lumpsum": calculate_lumpsum_drawdown(calculate_pot(med_portfolio_return))["lumpsum"],
                "drawdown": calculate_lumpsum_drawdown(calculate_pot(med_portfolio_return))["drawdown"]
            },
            "inflation_match": {
                "lumpsum": calculate_lumpsum_drawdown(calculate_pot(inflation_match_portfolio_return))["lumpsum"],
                "drawdown": calculate_lumpsum_drawdown(calculate_pot(inflation_match_portfolio_return))["drawdown"]
            },
            "inflation_loss": {
                "lumpsum": calculate_lumpsum_drawdown(calculate_pot(inflation_loss_portfolio_return))["lumpsum"],
                "drawdown": calculate_lumpsum_drawdown(calculate_pot(inflation_loss_portfolio_return))["drawdown"]
            }
            }
        }
    
    return json.dumps(result, indent=4)