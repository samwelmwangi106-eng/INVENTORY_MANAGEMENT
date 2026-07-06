#Import the flask class from the flask installed package
from flask import Flask
from routes.product_routes import product_bp

# creating a flask app
app = Flask(__name__)

# registering the blu blueprint so as to access the products inside it
app.register_blueprint(product_bp)

# create the home route
@app.route("/")
def home():
    return{
        "message":"Welcome to the Inventory Management API!"
    }

# STARTING THE SERVER
if __name__ == "__main__":
    app.run(debug=True)