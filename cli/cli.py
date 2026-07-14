import sys
import os
# Add the project root directory to Python's search path.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Import the product service functions.
from services.product_service import (
    get_all_products,
    add_product,
    update_product,
    delete_product,
    add_product_by_barcode,
    search_product_by_name
)


# Display all products in the inventory.
def view_products():
    # Get every product from the database.
    products = get_all_products()

    # Check whether there are any products.
    if not products:
        print("\nNo products found.\n")
        return

    print("\n========== PRODUCT LIST ==========")

    # Display each product.
    for product in products:
        print(f"""
ID: {product["id"]}
Name: {product["name"]}
Category: {product["category"]}
Price: {product["price"]}
Quantity: {product["quantity"]}
-------------------------------
""")


# Add a new product manually.
def create_product():
    print("\n===== ADD NEW PRODUCT =====")

    # Ask the user for product information.
    name = input("Product Name: ")
    category = input("Category: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    # Create a dictionary.
    product = {
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity
    }

    # Save the product.
    result = add_product(product)

    # Check for validation errors.
    if "error" in result:
        print("\nError:", result["error"])
    else:
        print("\nProduct added successfully!")
        print(result)


# Add a product using a barcode.
def create_product_by_barcode():
    print("\n===== ADD PRODUCT USING BARCODE =====")

    # Ask for the barcode.
    barcode = input("Enter barcode: ")

    # Send the barcode to the service.
    result = add_product_by_barcode(barcode)

    # Check whether the product exists.
    if "error" in result:
        print("\nError:", result["error"])
    else:
        print("\nProduct added successfully!")
        print(result)


# Update an existing product.
def edit_product():
    print("\n===== UPDATE PRODUCT =====")

    # Ask for the product ID.
    product_id = int(input("Enter Product ID: "))

    # Ask for the updated details.
    name = input("New Name: ")
    category = input("New Category: ")
    price = float(input("New Price: "))
    quantity = int(input("New Quantity: "))

    # Store the updated data.
    updated_product = {
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity
    }

    # Update the product.
    result = update_product(product_id, updated_product)

    # Check whether the product exists.
    if result is None:
        print("\nProduct not found.")
    elif "error" in result:
        print("\nError:", result["error"])
    else:
        print("\nProduct updated successfully!")
        print(result)


# Delete a product.
def remove_product():
    print("\n===== DELETE PRODUCT =====")

    # Ask for the product ID.
    product_id = int(input("Enter Product ID: "))

    # Delete the product.
    deleted = delete_product(product_id)

    # Show the result.
    if deleted:
        print("\nProduct deleted successfully.")
    else:
        print("\nProduct not found.")


# Display the main menu.
def menu():

    while True:

        print("""
==================================
 INVENTORY MANAGEMENT SYSTEM
==================================
1. View Products
2. Add Product
3. Add Product by Barcode
4. Search products
5. Update Product
6. Delete Product
7. Exit
==================================
""")

        # Ask the user to choose an option.
        choice = input("Choose an option: ")

        if choice == "1":
            view_products()

        elif choice == "2":
            create_product()

        elif choice == "3":
            create_product_by_barcode()

        elif choice == "4":
            search_product()

        elif choice == "5":
            edit_product()

        elif choice == "6":
            remove_product()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

# Search for a product by its name.
def search_product():

    print("\n===== SEARCH PRODUCT =====")

    # Ask the user for the product name.
    name = input("Enter product name: ")

    # Search the database.
    products = search_product_by_name(name)

    # If nothing is found.
    if not products:
        print("\nNo products found.")
        return

    print("\n========== SEARCH RESULTS ==========")

    # Display every matching product.
    for product in products:
        print(f"\nID: {product['id']}")
        print(f"Name: {product['name']}")
        print(f"Category: {product['category']}")
        print(f"Price: {product['price']}")
        print(f"Quantity: {product['quantity']}")
        print("-----------------------------")


# Start the program.
if __name__ == "__main__":
    menu()