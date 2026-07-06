# contains the business logic 
# Temporary inventory
products = [
    {
        "id": 1,
        "name": "Laptop",
        "category": "Electronics",
        "price": 75000,
        "quantity": 10
    },
    {
        "id": 2,
        "name": "Mouse",
        "category": "Accessories",
        "price": 1500,
        "quantity": 25
    }
]

def get_all_products():
    #returns all products in the inventory
    return products