# Tests for the product service.
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from services.product_service import (
    validate_product,
    add_product
)


# Test that a valid product passes validation.
def test_validate_product_success():

    product = {
        "name": "Bread",
        "category": "Food",
        "price": 60,
        "quantity": 20
    }

    assert validate_product(product) is None


# Test that an empty product name fails.
def test_validate_product_no_name():

    product = {
        "name": "",
        "category": "Food",
        "price": 60,
        "quantity": 20
    }

    assert validate_product(product) == "Product name is required."


# Test adding a product.
def test_add_product():

    product = {
        "name": "Milk",
        "category": "Dairy",
        "price": 120,
        "quantity": 8
    }

    result = add_product(product)

    # Check that the product received an ID.
    assert "id" in result

    # Check the name.
    assert result["name"] == "Milk"