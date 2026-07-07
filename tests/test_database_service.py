# Test for the database
import os
import json
from services.database_service import load_database, save_database

#Test that the database can be loaded
def test_load_database():

    # Load the database.
    database = load_database()

    # Check that the result is a dictionary.
    assert isinstance(database, dict)

    # Check that the database contains a products list.
    assert "products" in database


# Test that data can be saved successfully.
def test_save_database():

    # Create sample data.
    sample_data = {
        "products": [
            {
                "id": 1,
                "name": "Test Product",
                "category": "Testing",
                "price": 100,
                "quantity": 5
            }
        ]
    }

    # Save the data.
    save_database(sample_data)

    # Load it again.
    database = load_database()

    # Check that the product was saved.
    assert database["products"][0]["name"] == "Test Product"