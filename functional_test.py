from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_add_post(self):
        # Suzy Q Wants to post on our website
        self.browser.get('http://localhost:8000/post/new')
        driver = webdriver.Firefox()
        driver.get('http://localhost:8000/post/new')

        # She is invited to enter a title, and enters her title
        inputbox = self.browser.find_element_by_id('id_title')  
        inputbox.send_keys('Suzy Q and her Blog Post')  
        
		#When she hits enter, she is transferred to the content box
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1) 

        # She is invited to enter a her post, and enters her post
        inputbox = self.browser.find_element_by_id('id_text')  
        inputbox.send_keys('Howdy Yall Im Suzy Q')  
		
		#When she clicks save, she is transferred back to the homepage
        driver.find_element_by_class('save').click() 
        time.sleep(1) 
        self.assertIn('blog',self.browser.title)
    def test_add_comment(self):
        # Suzy Q Wants to post a comment on our website
        self.browser.get('http://localhost:8000/post/1')
        driver = webdriver.Firefox()
        driver.get('http://localhost:8000/post/1')

        # She is invited to enter a comment by clicking the button
        driver.find_elements_by_link_text('Add Comment').click()
        time.sleep(1)
		
		#She is taken to the comment page, and is prompted to enter author
        inputbox = self.browser.find_element_by_id('id_author')  
        inputbox.send_keys('Suzy Q')  
        
		#When she hits enter, she is transferred to the content box
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1) 

        # She is invited to enter a her comment, and enters her comment
        inputbox = self.browser.find_element_by_id('id_text')  
        inputbox.send_keys('I love this post lol')  
		
		#When she clicks save, she is transferred back to the post
        driver.find_element_by_class('save').click() 
        time.sleep(1) 
        self.assertIn('post/1',self.browser.current_url)
		
    def test_delete_comment(self):
        # Suzy Q Wants to post on our website
        self.browser.get('http://localhost:8000/post/1')
        driver = webdriver.Firefox()
        driver.get('http://localhost:8000/post/1')

        # She sees the X to delete an unsightly comment and clicks it
        driver.find_element_by_class('gliphcon_remove').click()  
        time.sleep(1)         
        

tester = NewVisitorTest()
tester.setUp()
tester.test_add_post()
tester.test_add_comment()
tester.test_delete_comment()
tester.tearDown()