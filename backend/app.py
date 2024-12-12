from flask import Flask
from routes.mortgage_routes import mortgage_routes  # Import blueprint

app = Flask(__name__)

# Register blueprint
app.register_blueprint(mortgage_routes)

if __name__ == "__main__":
    app.run(debug=True)
