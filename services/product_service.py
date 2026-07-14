# Contains the business logic for managing products.
# This service communicates with the database service
# to read from and write to the db.json file.

from services.database_service import load_database, save_database
from services.openfoodfacts_service import get_product_by_barcode


# Validate product information before saving it.
def validate_product(product):

    # Product name is required.
    # strip() removes spaces so that "   " is treated as empty.
    if not product.get("name", "").strip():
        return "Product name is required."

    # Product category is required.
    if not product.get("category", "").strip():
        return "Product category is required."

    # Product price is required.
    if "price" not in product:
        return "Product price is required."

    # Product quantity is required.
    if "quantity" not in product:
        return "Product quantity is required."

    # Price must be either an integer or a decimal number.
    if not isinstance(product["price"], (int, float)):
        return "Price must be a number."

    # Quantity must be a whole number.
    if not isinstance(product["quantity"], int):
        return "Quantity must be an integer."

    # Price cannot be negative.
    if product["price"] < 0:
        return "Price cannot be negative."

    # Quantity cannot be negative.
    if product["quantity"] < 0:
        return "Quantity cannot be negative."

    # Everything is valid.
    return None


# Retrieve every product stored in the database.
def get_all_products():

    # Load the entire database from db.json.
    database = load_database()

    # Return only the list of products.
    return database["products"]


# Add a new product to the database.
def add_product(product):

    # Validate the product information.
    error = validate_product(product)

    # If validation fails, return the error.
    if error:
        return {"error": error}

    # Load the current database.
    database = load_database()

    # Get the current list of products.
    products = database["products"]

    # Generate the next available product ID.
    if products:
        next_id = max(product["id"] for product in products) + 1
    else:
        next_id = 1

    # Assign the generated ID to the new product.
    product["id"] = next_id

    # Add the new product to the products list.
    database["products"].append(product)

    # Save the updated database.
    save_database(database)

    # Return the newly created product.
    return product


# Update an existing product using its ID.
def update_product(product_id, updated_product):

    # Validate the updated product information.
    error = validate_product(updated_product)

    # If validation fails, return the error.
    if error:
        return {"error": error}

    # Load the current database.
    database = load_database()

    # Search through every product.
    for product in database["products"]:

        # Check whether this is the product we want.
        if product["id"] == product_id:

            # Update the product with the new information.
            product.update(updated_product)

            # Save the updated database.
            save_database(database)

            # Return the updated product.
            return product

    # Return None if the product does not exist.
    return None


# Delete a product from the database using its ID.
def delete_product(product_id):

    # Load the current database.
    database = load_database()

    # Search through every product.
    for product in database["products"]:

        # Check whether this is the product we want.
        if product["id"] == product_id:

            # Remove the product from the products list.
            database["products"].remove(product)

            # Save the updated database.
            save_database(database)

            # Indicate that deletion was successful.
            return True

    # Return False if the product was not found.
    return False
# Add a product to the inventory using its barcode.
def add_product_by_barcode(barcode):

    # Ask the Open Food Facts service for product information.
    product = get_product_by_barcode(barcode)

    # If no product was found, return an error.
    if product is None:
        return {"error": "Product not found."}

    # Create a product dictionary using the information from the API.
    new_product = {
        "name": product.get("product_name", "Unknown Product"),
        "category": product.get("categories", "Unknown Category"),
        "price": 0.0,      # Default price
        "quantity": 0       # Default quantity
    }

    # Save the product into db.json.
    return add_product(new_product)

# Search for products by name.
def search_product_by_name(name):

    # Load the database.
    database = load_database()

    # Store matching products.
    results = []

    # Check every product.
    for product in database["products"]:

        # Compare names without considering uppercase/lowercase.
        if name.lower() in product["name"].lower():
            results.append(product)

    # Return all matching products.
    return results