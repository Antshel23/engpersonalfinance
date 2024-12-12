from flask import Blueprint
from controllers.pension_controller import get_pension_pot

pension_routes = Blueprint('pension', __name__)

# Define the route for the POST request
pension_routes.route('/calculate/pot', methods=['POST'])(get_pension_pot)