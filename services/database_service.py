# Handles reading and writing data to db.json.

import json
import os

# Get the project root directory.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build the full path to db.json.
DATABASE_FILE = os.path.join(BASE_DIR, "db.json")


# Load data from db.json.
def load_database():

    # Create the file if it does not exist.
    if not os.path.exists(DATABASE_FILE):

        database = {
            "products": []
        }

        with open(DATABASE_FILE, "w") as file:
            json.dump(database, file, indent=4)

    # Read the database.
    with open(DATABASE_FILE, "r") as file:
        return json.load(file)


# Save data into db.json.
def save_database(database):

    with open(DATABASE_FILE, "w") as file:
        json.dump(database, file, indent=4)