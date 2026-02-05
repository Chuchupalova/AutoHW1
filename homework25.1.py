from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
driver.maximize_window()

#тут локатори
locators = {
    "email_input_xpath": (By.XPATH, "//input[@name='email']"),
    "password_input_xpath": (By.XPATH, "//input[@name='password' and @name='password']"),
    "sign_in_button_xpath": (By.XPATH, "//button[@text()='Sign In']"),
    "email_input_in_form_xpath": (By.XPATH, "//form//input[@name='email']"),
    "sign_in_button_countains_xpath": (By.XPATH, "//button[contains[@text()='Sign')]"),


    "garage_title_xpath": (By.XPATH, "//h1[text()='Garage']"),
    "add_car_button_xpath": (By.XPATH, "//button[text()='Add-car']"),
    "add_car_button_contains_xpath": (By.XPATH, "//button[contains(@class, 'btn') and contains (text(), 'Add')]"),
    "car_list_xpath": (By.XPATH, "//div[contains(@class='car-list')]"),
    "car_item_xpath": (By.XPATH, "//div[contains(@class, 'car-list')]//div[contains(@class, 'car-item')]"),


    "add_car_button_testid_xpath": (By.XPATH, "//button[@data-testid='add-car-button']"),
    "add_car_modal_xpath": (By.XPATH, "//div[contains(@class,'modal') and .//h5[text()='Add car']]"),
    "add_car_modal_title_xpath": (By.XPATH, "//h5[text()='Add car']"),
    "brand_select_xpath": (By.XPATH, "//select[@id='brandSelect']"),
    "model_select_xpath": (By.XPATH, "//select[@id='modelSelect']"),
    "mileage_input_xpath": (By.XPATH, "//input[@name='mileage']"),
    "add_car_submit_button_xpath": (By.XPATH, "//button[text()='Add']"),
    "modal_close_button_xpath": (By.XPATH, "//button[contains(@class,'close')]"),
    "validation_error_xpath": (By.XPATH, "//div[contains(@class,'invalid-feedback')]"),
    "year_input_xpath": (By.XPATH, "//input[@placeholder='Year']"),
    "brand_options_xpath": (By.XPATH, "//select[@id='brandSelect']/option"),
    "audi_brand_option_xpath": (By.XPATH, "//select[@id='brandSelect']/option[text()='Audi']"),
    "model_options_xpath": (By.XPATH, "//select[@id='modelSelect']/option"),
    "cancel_button_xpath": (By.XPATH, "//button[text()='Cancel']"),
    "last_car_item_xpath": (By.XPATH, "(//div[contains(@class,'car-item')])[last()]"),

#CSS
    "email_input_css": (By.CSS_SELECTOR, "input[name='email']"),
    "password_input_css": (By.CSS_SELECTOR, "input[name='password']"),
    "login_button_css": (By.CSS_SELECTOR, "button[type='submit']"),
    "email_input_in_form_css": (By.CSS_SELECTOR, "form input[name='email']"),
    "primary_button_css": (By.CSS_SELECTOR, "button.btn-primary"),

    "garage_title_css": (By.CSS_SELECTOR, "h1"),
    "add_car_button_css": (By.CSS_SELECTOR, "button[data-testid='add-car-button']"),
    "car_list_css": (By.CSS_SELECTOR, "div.car-list"),
    "car_item_css": (By.CSS_SELECTOR, "div.car-list div.car-item"),
    "last_car_item_css": (By.CSS_SELECTOR, "div.car-item:last-child"),

    "modal_css": (By.CSS_SELECTOR, "div.modal"),
    "modal_title_css": (By.CSS_SELECTOR, "div.modal h5"),
    "brand_select_css": (By.CSS_SELECTOR, "select#brandSelect"),
    "model_select_css": (By.CSS_SELECTOR, "select#modelSelect"),
    "mileage_input_css": (By.CSS_SELECTOR, "input[name='mileage']"),

    "submit_button_css": (By.CSS_SELECTOR, "button.btn-primary[type='submit']"),
    "secondary_button_css": (By.CSS_SELECTOR, "button.btn-secondary"),
    "close_button_css": (By.CSS_SELECTOR, "button.close"),
    "validation_error_css": (By.CSS_SELECTOR, "div.invalid-feedback"),
    "year_input_css": (By.CSS_SELECTOR, "input[placeholder='Year']"),

    "brand_options_css": (By.CSS_SELECTOR, "select#brandSelect option"),
    "audi_brand_option_css": (By.CSS_SELECTOR, "select#brandSelect option[value='Audi']"),
    "model_options_css": (By.CSS_SELECTOR, "select#modelSelect option"),
    "modal_content_css": (By.CSS_SELECTOR, "div.modal-content"),
    "modal_footer_buttons_css": (By.CSS_SELECTOR, "div.modal-footer button"),
}

driver.quit()