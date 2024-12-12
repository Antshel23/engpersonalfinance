from flask import Blueprint
from controllers.mortgage_controller import get_mortgage_repayment

mortgage_routes = Blueprint('mortgage', __name__)

# /calculate call posts payload
mortgage_routes.route('/calculate/repayment', methods=['POST'])(get_mortgage_repayment)