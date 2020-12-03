from selenium import webdriver
import time

class LoginBot():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('chromedriver')
        self.base_url = 'https://instagram.com' 

    def login(self):
        driver = self.driver
        driver.get(f'{self.base_url}/accounts/login/')
        time.sleep(1)

        #username field
        username_field = driver.find_element_by_xpath("//input[@name='username']")
        username_field.send_keys(self.username)

        #password field
        password_field = driver.find_element_by_xpath("//input[@name='password']")
        password_field.send_keys(self.password)

        #login button
        login_button = driver.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        time.sleep(5)

        #LOGIN NOTIFICATIONS

        save_info_title = driver.find_element_by_xpath("//div[@class='olLwo']")
        if save_info_title.text == 'Save Your Login Info?':
            driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']").click()
            time.sleep(1)

        push_notif_title = driver.find_element_by_xpath("//h2[@class='_7UhW9      x-6xq  yUEEX   KV-D4          uL8Hv         ']")
        if push_notif_title.text == 'Turn on Notifications':
            driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']").click()
        
        time.sleep(5)