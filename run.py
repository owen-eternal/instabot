from selenium import webdriver
import os
import time
from random import randint

class InstaBot():
    list_of_links = []

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('chromedriver')
        self.base_url = 'https://instagram.com' 
        self.hashtag_url = 'explore/tags'

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

        
    def find_user(self, user_account):
        driver = self.driver
        self.user_account = user_account

        driver.get(f'{self.base_url}/{self.user_account}')

    def filter_algo(self, num_of_pics):
        driver = self.driver
        
        #find all "a" tags
        all_links = driver.find_elements_by_tag_name('a')

        #retrieve all picture links from tags
        #filter out all links that aren't picture related 
        correct_links = list(filter(lambda link: '.com/p/' in link.get_attribute('href'), all_links))

        #get the 3 pictures link and add them to list of links
        for i in range(num_of_pics):
            picture_link = correct_links[i].get_attribute('href')
            if picture_link not in self.list_of_links:
                self.list_of_links.append(picture_link)

    def like(self, num_of_pics):
        self.filter_algo(num_of_pics)
        driver = self.driver

        for picture in self.list_of_links:
            driver.get(picture)
            like_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
            like_button.click()
            time.sleep(1)
    
        self.list_of_links.clear()
        driver.get(f'{self.base_url}/{self.user_account}')

    def comment(self, num_of_pics, comments):
        self.filter_algo(num_of_pics)
        driver = self.driver

        for picture in self.list_of_links:
            #get link
            driver.get(picture)
            #click comment box
            comment_field = driver.find_element_by_class_name('RxpZH')
            comment_field.click()
            time.sleep(1)
            
            #add a comment
            type_comment = driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']")
            type_comment.send_keys(comments[randint(0,4)])
            time.sleep(1)
            submit_button = driver.find_element_by_xpath("//button[@type='submit']")
            submit_button.click()
            time.sleep(1)

        self.list_of_links.clear()
        driver.get(f'{self.base_url}/{self.user_account}')
    
if __name__ == "__main__":

    BOT_EMAIL = os.environ.get('BOT_EMAIL')
    print(BOT_EMAIL)
    BOT_PASSWORD = os.environ.get('DB_PASSWORD')

    USER = 'Kolumbusbeats'
    LIKES_PP = 3 #number of picures liked
    COMMENTS_PP = 3

    COMM_LIST = [
                        'Interesting feed, I love it!',
                        'The best post I have seen today',
                        'wonderful',
                        'see why you are my favourite instagramer??',
                        'This is beautiful. I am looking forward to seeing more posts from you. '
                    ]
    
    ig_bot = InstaBot(BOT_EMAIL, BOT_PASSWORD)
    ig_bot.login()  
    ig_bot.find_user(USER)
    ig_bot.like(LIKES_PP)
    ig_bot.comment(COMMENTS_PP, COMM_LIST)
     

