# Tests for the Open Food Facts service.
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from services.openfoodfacts_service import get_product_by_barcode


# Test retrieving a product using a valid barcode.
def test_get_product_by_barcode():

    # Barcode for Coca-Cola.
    barcode = "5449000000996"

    # Get the product from the API.
    product = get_product_by_barcode(barcode)

    # Check that a product was returned.
    assert product is not None

    # Check that the product has a name.
    assert "product_name" in product


# Test using an invalid barcode.
def test_invalid_barcode():

    # This barcode should not exist.
    barcode = "0000000000000"

    # The function should return None.
    product = get_product_by_barcode(barcode)

    assert product is None