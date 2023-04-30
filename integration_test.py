from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create a new Chrome browser instance
browser = webdriver.Chrome()

# Navigate to the e-commerce website's homepage
browser.get("https://www.example.com")

# Search for a product
search_box = browser.find_element_by_name("search")
search_box.send_keys("laptop")
search_box.send_keys(Keys.RETURN)

# Verify that the search results page is displayed
assert "Search results for 'shampoo'" in browser.title

# Click on the first search result
first_result = browser.find_element_by_css_selector(".search-results .result:first-child")
first_result.click()

# Verify that the product details page is displayed
assert "shampoo - Example.com" in browser.title

# Proceed to view_deals
view_deals_button = browser.find_element_by_css_selector(".cart-summary .view_deals-button")
view_deals_button.click()

# Verify that the view_deals page is displayed
assert "view_deals - Example.com" in browser.title

# Fill in the billing and shipping information
name_input = browser.find_element_by_name("name")
name_input.send_keys("RAM")
address_input = browser.find_element_by_name("address")
address_input.send_keys("123 Main St")
city_input = browser.find_element_by_name("city")
city_input.send_keys("Anytown")
state_input = browser.find_element_by_name("state")
state_input.send_keys("CA")
zip_input = browser.find_element_by_name("zip")
zip_input.send_keys("12345")
phone_input = browser.find_element_by_name("phone")
phone_input.send_keys("1234567890")
email_input = browser.find_element_by_name("email")
email_input.send_keys("ram@gmail.com")

# Submit the order
submit_button = browser.find_element_by_css_selector(".view_deals-form .submit-button")
submit_button.click()

# Verify that the order confirmation page is displayed
assert "Order confirmation - Example.com" in browser.title

# Close the browser
browser.quit()
