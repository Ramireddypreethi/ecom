import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from entity.product import Product
from entity.customer import Customer
from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl
from exception.customernotfound import CustomerNotFound
from exception.productnotfound import ProductNotFound



class TestEcommerceSystem(unittest.TestCase):
    def setUp(self):
        self.repository = OrderProcessorRepositoryImpl()


        # Create a sample customer and product for testing
        self.customer = Customer(customer_id=17, name="raghu", email="rahu2@gmail.com", password="rahu@48")
        self.product = Product(product_id=115, name="pillow", price=599, description="soft pillow", stockQuantity=20)

        # Add sample customer and product to the repository for testing
        self.repository.create_customer(self.customer)
        self.repository.create_product(self.product)
#  Write test case to test Product created successfully or not.
    def test_product_created_successfully(self):
        """Test case to check if product is created successfully."""
        product = self.repository.get_product_by_id(115)  # Use the new product ID
        self.assertTrue(product)
        
# Write test case to test product is added to cart successfully or not
    def test_product_added_to_cart_successfully(self):
        """Test case to check if product is added to cart successfully."""
        quantity = 4
        result = self.repository.add_to_cart(self.customer, self.product, quantity)
        self.assertTrue(result)  # Ensure product was added successfully

# Write test case to test product is ordered successfully or not.
    def test_product_ordered_successfully(self):
        """Test case to check if product is ordered successfully."""
        quantity = 1
        shipping_address = "98 Oak"
        result = self.repository.place_order(self.customer, [(self.product, quantity)], shipping_address)
        self.assertTrue(result)  # Ensure the order was placed successfully
        # to check condition is true or false,if false error will display

# write test case to test exception is thrown correctly or not when customer id or productid not found in database.
    def test_exception_thrown_when_customer_not_found(self):
        """Test case to check if exception is thrown when customer ID not found."""
        with self.assertRaises(CustomerNotFound):
            self.repository.get_customer_by_id(20)  # Using a non-existent customer ID

    def test_exception_thrown_when_product_not_found(self):
        """Test case to check if exception is thrown when product ID not found."""
        with self.assertRaises(ProductNotFound):
            self.repository.get_product_by_ide(200)  # Using a non-existent product ID

if __name__ == "__main__":
    unittest.main()

