from flask import Flask
from routes.mortgage_routes import mortgage_routes
from routes.pension_routes import pension_routes 

app = Flask(__name__)

# Register blueprint
app.register_blueprint(mortgage_routes, url_prefix="/mortgage")
app.register_blueprint(pension_routes, url_prefix="/pension")

if __name__ == "__main__":
    app.run(debug=True)
