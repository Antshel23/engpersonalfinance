from flask import Blueprint
from controllers.mortgage_controller import get_mortgage_repayment

mortgage_routes = Blueprint('mortgage', __name__)

# Define the route for the POST request
mortgage_routes.route('/calculate', methods=['POST'])(get_mortgage_repayment)