# tests/test_models.py
import unittest
from models import Product  # Assuming your Product model is in the models.py file
from faker import Faker

fake = Faker()

class TestProductModel(unittest.TestCase):
    
    def test_update_product(self):
        # Create a fake product (simulating a database or an in-memory object)
        product = Product(name=fake.company(),
                          description=fake.text(max_nb_chars=200),
                          price=99.99,
                          sku=fake.uuid4(),
                          category=fake.word())
        
        # Simulate saving the product to a "database"
        product.save()  # Assuming the 'save' method persists the product
        
        # Simulate the "update" operation
        new_name = fake.company()
        product.name = new_name
        product.save()  # Save the updated product
        
        # Retrieve the product again to confirm the update
        updated_product = Product.read(product.sku)  # Assuming 'read' method fetches by SKU
        
        # Check that the name has been updated
        self.assertEqual(updated_product['name'], new_name)
        self.assertEqual(updated_product['sku'], product.sku)

if __name__ == '__main__':
    unittest.main()
