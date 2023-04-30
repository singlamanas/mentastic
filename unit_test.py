
import mysql.connector
from unittest.mock import Mock
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import unittest
from login_page import LoginPage

class FlaskTest(unittest.TestCase):
    # db=mysql.connection
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.app.root_path = app.root_path  # Set the root path of the app
        self.app.template_folder = app.template_folder  # Set the path to the templates folder
        self.db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password ="password",
            database = "data_base_name", #apne data base ka name for used in flask
            auth_plugin = "mysql_native_password"  # and uss data_base ka password
        )

        self.cursor= self.db.cursor()
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.example-ecommerce-website.com/products")
        self.driver.maximize_window()

    def test_items_display_clearly(self):
        items = self.driver.find_elements_by_css_selector(".product")
        for item in items:
            title = item.find_element_by_css_selector(".product-title").text
            price = item.find_element_by_css_selector(".product-price").text
            image = item.find_element_by_css_selector(".product-image").get_attribute("src")
            self.assertNotEqual("", title.strip(), f"Title is empty for item: {image}")
            self.assertNotEqual("", price.strip(), f"Price is empty for item: {image}")
            self.assertTrue(image.startswith("https://"), f"Image URL is invalid for item: {image}")

    def test_items_categorized_by_name(self):
        categories = ["men", "tends", "collection"]
        for category in categories:
            category_link = self.driver.find_element_by_link_text(category)
            category_link.click()
            category_title = self.driver.find_element_by_css_selector(".category-title").text
            self.assertEqual(category_title, category, f"Expected category title '{category}' but got '{category_title}'")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.example-ecommerce-website.com/products")
        self.driver.maximize_window()

    def test_items_have_descriptions(self):
        items = self.driver.find_elements_by_css_selector(".product")
        for item in items:
            title = item.find_element_by_css_selector(".product-title").text
            description = item.find_element_by_css_selector(".product-description").text
            self.assertNotEqual("", description.strip(), f"Description is empty for item: {title}")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.example-ecommerce-website.com/checkout")
        self.driver.maximize_window()

    def test_shipping_address_written(self):
        shipping_address = self.driver.find_element_by_css_selector(".shipping-address").text
        self.assertNotEqual("", shipping_address.strip(), "Shipping address is empty")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.example-ecommerce-website.com/products/123")
        self.driver.maximize_window()

    def test_product_review_written(self):
        review_form = self.driver.find_element_by_css_selector(".product-review-form")
        name_input = review_form.find_element_by_name("name")
        rating_input = review_form.find_element_by_name("rating")
        comment_input = review_form.find_element_by_name("comment")
        submit_button = review_form.find_element_by_css_selector(".submit-button")
        name_input.send_keys("John Doe")
        rating_input.send_keys("4")
        comment_input.send_keys("This product is great!")
        submit_button.click()
        success_message = self.driver.find_element_by_css_selector(".success-message").text
        self.assertEqual("Your review has been submitted.", success_message)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.example-ecommerce-website.com/products/123")
        self.driver.maximize_window()

    def test_product_image_available(self):
        product_image = self.driver.find_element_by_css_selector(".product-image")
        image_src = product_image.get_attribute("src")
        self.assertNotEqual("", image_src.strip(), "Product image is not available")




    def setUp(self):
        self.login_page = LoginPage()

    def test_login_success(self):
        username = "exampleuser"
        password = "examplepassword"
        self.assertTrue(self.login_page.login(username, password))

    def test_login_empty_credentials(self):
        username = ""
        password = ""
        self.assertFalse(self.login_page.login(username, password))

    def test_login_incorrect_credentials(self):
        username = "exampleuser"
        password = "wrongpassword"
        self.assertFalse(self.login_page.login(username, password))

    def test_login_username_only(self):
        username = "exampleuser"
        password = ""
        self.assertFalse(self.login_page.login(username, password))

    def test_login_password_only(self):
        username = ""
        password = "examplepassword"
        self.assertFalse(self.login_page.login(username, password))

    def tearDown(self):
        self.login_page.close()

if __name__ == '__main__':

    cov=coverage.Coverage()
    cov.start()
    unittest.main()
    cov.stop()
    cov.save()
    cov.report()