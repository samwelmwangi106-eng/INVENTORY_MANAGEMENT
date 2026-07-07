# creating all routes related to products
from flask import Blueprint,request, jsonify
from services.product_service import get_all_products
from services.openfoodfacts_service import get_product_by_barcode
from services.product_service import (get_all_products,add_product,update_product,delete_product)

# Ask the service for the products
products = get_all_products()

# blueprint groups all related routes together
product_bp = Blueprint("products",__name__)

# GET all products

## return every product in our inventory
@product_bp.route("/products",methods=["GET"])
def get_products():
    #Ask the service for all products
    products = get_all_products()

    # Return the products as json
    return jsonify(products)
    

# Add (POST) new products
@product_bp.route("/products",methods=["POST"])
def create_product():
    # read the json data sent by the client
    product_data = request.get_json()

    #Ask the service to save the product
    new_product = add_product(product_data)

    # Return the newly created data
    return jsonify(new_product),201

   

# Update(PUT) a product
# updating an existing product
@product_bp.route("/products/<int:product_id>",  methods=["PUT"])
def edit_product(product_id):
    # READ(request) the updated product data
    updated_data = request.get_json()

    # Ask the service to update the product
    product = update_product(product_id, updated_data)

    # If found, return the updated product
    if product:
        return jsonify(product), 200

    # Otherwise return an error
    return jsonify({
        "error": "Product not found"
    }), 404

   
# deleting(DELETE) a product
# removing it from our inventory using its id.
@product_bp.route("/products/<int:product_id>",methods=["DELETE"])
def remove_product(product_id):

    # Ask the service to delete the product
    deleted = delete_product(product_id)

    # If successful
    if deleted:
        return jsonify({
            "message": "Product deleted successfully"
        }), 200

    # Otherwise
    return jsonify({
        "error": "Product not found"
    }), 404

    

@product_bp.route("/barcode/<barcode>",methods=["GET"])
def fetch_product(barcode):
    product = get_product_by_barcode(barcode)

    if product is None:
        return jsonify({"error": "Product not found"}),404
    
    return jsonify(product),200