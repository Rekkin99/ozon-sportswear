from django.test import TestCase, Client
from .models import Product
from .forms import Catalogue

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')
        
    def test_add_product_using_add_product_template(self):
        response = Client().get('/add-product/')
        self.assertTemplateUsed(response, 'add_product.html')
        
    def test_show_catalogue_using_catalogue_template(self):
        response = Client().get('/catologue/')
        self.assertTemplateUsed(response, 'catalogue.html')
    
    def test_product_detail_using_product_detail_template(self):
        product = Product.objects.create(
            name="Ozon Foot",
            price=100000,
        )
        response = Client().get(f'/product/{product.id}/')
        self.assertTemplateUsed(response, 'product_detail.html')

    def test_nonexistent_page(self):
        response = Client().get('/burhan_always_exists/')
        self.assertEqual(response.status_code, 404)
        
    def test_product_creation(self):
        product = Product.objects.create(
            name="Ozon Foot",
            price=100000,
            category="footwear",
            is_featured=True
        )
        self.assertTrue(product.is_featured)
        self.assertEqual(product.category, 'footwear')
        self.assertEqual(product.name, 'Ozon Foot')
        self.assertEqual(product.price, 100000)
        
    def test_product_default_values(self):
        product = Product.objects.create(
            name="Ozon Foot",
            price=100000,
        )
        self.assertFalse(product.is_featured)
        self.assertEqual(product.category, 'footwear')
    
    
    # The Form-Test is Set-Up by Chat-GPT    
    def setUp(self):
        self.valid_data = {
            "name": "Adidas Predator",
            "price": 1200000,
            "description": "High-quality football shoes.",
            "thumbnail": "https://example.com/shoe.jpg",
            "category": "footwear",
            "is_featured": True
        }

    def test_valid_form(self):
        form = Catalogue(data=self.valid_data)
        self.assertTrue(form.is_valid(), "Form should be valid with correct data.")

    def test_missing_required_field(self):
        invalid_data = self.valid_data.copy()
        del invalid_data["name"]  # Remove required field
        form = Catalogue(data=invalid_data)
        self.assertFalse(form.is_valid(), "Form should be invalid without 'name'.")
        self.assertIn("name", form.errors)

    def test_invalid_price_type(self):
        invalid_data = self.valid_data.copy()
        invalid_data["price"] = "one million"  # Invalid type
        form = Catalogue(data=invalid_data)
        self.assertFalse(form.is_valid(), "Form should be invalid with non-integer price.")
        self.assertIn("price", form.errors)

    def test_invalid_category_choice(self):
        invalid_data = self.valid_data.copy()
        invalid_data["category"] = "food"  # Not in CATEGORY_CHOICES
        form = Catalogue(data=invalid_data)
        self.assertFalse(form.is_valid(), "Form should be invalid with invalid category.")
        self.assertIn("category", form.errors)

    def test_blank_thumbnail_url(self):
        data = self.valid_data.copy()
        data["thumbnail"] = ""  # This is allowed (nullable field)
        form = Catalogue(data=data)
        self.assertTrue(form.is_valid(), "Form should be valid with blank thumbnail.") 



        