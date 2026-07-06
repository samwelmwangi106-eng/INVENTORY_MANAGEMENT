# creating all routes related to products
from flask import Blueprint,request, jsonify
from services.product_service import get_all_products
from services.openfoodfacts_service import get_product_by_barcode

# Ask the service for the products
products = get_all_products()

# blueprint groups all related routes together
product_bp = Blueprint("products",__name__)

# GET all products

## return every product in our inventory
@product_bp.route("/products",methods=["GET"])
def get_products():
    # Return the current product list as json
    return jsonify(products)


# Add (POST) new products
@product_bp.route("/products",methods=["POST"])
def add_product():
    # read the json data sent by the client
    product_data = request.get_json()

    # create a new product dictionary
    new_product = {
        "id":len(products) + 1,
        "name": product_data["name"],
        "category":product_data["category"],
        "price":product_data["price"],
        "quantity": product_data["quantity"]
    }
    # Add new product
    products.append(new_product)

    # Return the new product with status code 201 (Created)
    return jsonify(new_product), 201

# Update(PUT) a product
# updating an existing product
@product_bp.route("/products/<int:product_id>",  methods=["PUT"])
def update_product(product_id):
    # READ(request) the updated product data
    updated_data = request.get_json()

    #search for the product
    for product in products:
        # checking if the product we want
        if product["id"] == product_id:

            # update each field
            product["name"] = updated_data["name"]
            product["category"] = updated_data["category"]
            product["price"] = updated_data["price"]
            product["quantity"] = updated_data["quantity"]

            # return the updated product
            return jsonify(product), 200
        
    # if no product is found
    return jsonify({"error":"Product not found"}), 404

# deleting(DELETE) a product
# removing it from our inventory using its id.
@product_bp.route("/products/<int:product_id>",methods=["DELETE"])
def delete_product(product_id):

    # loop through all products
    for product in products:
        # check if this is the product we want to delete
        if product["id"] == product_id:
            # remove it from the list
            products.remove(product)

        # returning a success message
        return jsonify({
            "message":"Product deleted succesfully"
        }), 200
    
    # if our product never exist
    return jsonify({
        "error": "Product not found"
    }),404

@product_bp.route("/barcode/<barcode>",methods=["GET"])
def fetch_product(barcode):
    product = get_product_by_barcode(barcode)

    if product is None:
        return jsonify({"error": "Product not found"}),404
    
    return jsonify(product),200