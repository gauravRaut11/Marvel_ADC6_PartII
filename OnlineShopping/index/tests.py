from django.test import TestCase
from .models import Item
from cart.models import Cart, Order
# models test
class Test_product(TestCase):
    def setUp(self):
        a1 = Item.objects.create(product_name="jug",category="grocessory",price=10)
        a2 = Item.objects.create(product_name="vans",category="fashion",price=10)
        c1 = Cart.objects.create(item=a1)

    def test_is_valid(self):
        self.assertTrue(Cart.objects.exists())

    def test_product_price(self):
       item =Item.objects.create(price=10)
       self.assertTrue(item.test_price())

    def test_Product_category(self):
        item=Item.objects.create(product_name="jug",category="grocessory",price=10)
        self.assertTrue(item.test_product_category())

    def test_home_page_contains_correct_templete(self):
        response = self.client.get('/')
        self.assertContains(response, 'home.html')

    def test_get_products_count(self):
        self.assertEqual(Item.objects.count(),2)


    def test_itemCategory_from_Name(self):
        prd=Item.objects.get(product_name='vans')
        self.assertEqual(prd.category,'fashion')