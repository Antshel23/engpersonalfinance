from flask import Blueprint
from controllers.mortgage_controller import return_mortgage_info

mortgage_routes = Blueprint('mortgage', __name__)

mortgage_routes.route('/calculate/repayment', methods=['POST'])(return_mortgage_info)