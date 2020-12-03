from selenium import webdriver
from random import randint
from bot.login_bot import LoginBot
import os
import time


class EngagementBot(LoginBot):
    list_of_links = []
    driver = webdriver.Chrome('chromedriver.exe')
    base_url = 'https://instagram.com' 

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