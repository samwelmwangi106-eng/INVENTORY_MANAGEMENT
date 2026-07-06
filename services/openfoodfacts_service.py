# Contains functions for communicating with the OpenFoodFacts API

import requests

# Base URL of the OpenFoodFacts API
OPENFOODFACTS_API = "https://world.openfoodfacts.org/api/v3/product/"


def get_product_by_barcode(barcode):
    """
    Fetch product information from OpenFoodFacts using a barcode.
    """

    # Build the complete API URL
    url = f"{OPENFOODFACTS_API}{barcode}.json"

    # Required by OpenFoodFacts
    headers = {
        "User-Agent": "InventoryManagement/1.0 (your_email@gmail.com)"
    }

    # Send GET request
    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    print("URL:", url)
    print("Status Code:", response.status_code)

    # Request failed
    if response.status_code != 200:
        print(response.text)
        return None

    data = response.json()

    # Product not found
    if data.get("product") is None:
        return None

    # Return only the product information
    return data["product"]