"""Import the flask class from the flask installed package"""
from flask import Flask

# creating a flask app
app = Flask(__name__)

# create the home route
@app.route("/")
def home():
    return{
        "message":"Welcome to the Inventory Management API!"
    }

# STARTING THE SERVER
if __name__ == "__main__":
    app.run(debug=True)