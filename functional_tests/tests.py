from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)


    def tearDown(self):
        self.browser.quit()


    def assert_rows_in_list_table(self, *row_strings):
        table = self.browser.find_element_by_id('todo_list_table')
        rows = table.find_elements_by_tag_name('tr')
        for text in row_strings:
            self.assertIn(text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Fred visits the to-do list home page
        self.browser.get(self.live_server_url)

        # He observes that the title and <h1> say something about To-Do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # The page invites him to enter a to-do item
        inputbox = self.browser.find_element_by_id('new_item_box')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Think about what to do"
        inputbox.send_keys("Think about what to do", Keys.ENTER)

        # When he types Enter, he is taken to a new URL. The page updates and
        # now lists "1: Think about..."
        fred_list_url = self.browser.current_url
        self.assertRegex(fred_list_url, 'lists/.+')
        self.assert_rows_in_list_table(
            '1. Think about what to do',
        )

        # There is still a text box inviting him to add another item
        inputbox = self.browser.find_element_by_id('new_item_box')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He enters "Make a more detailed to-do list" and presses Enter
        inputbox.send_keys("Make a more detailed to-do list", Keys.ENTER)

        # The page updates again, and now shows both items on the list
        self.assert_rows_in_list_table(
            '1. Think about what to do',
            '2. Make a more detailed to-do list',
        )

        # Fred sees a statement that the site has generated a unique URL for
        # his list
        ## TODO: Implement this

        # Fred visits the URL, and sees that his to-do list is there
        ## TODO: Implement this

        # Now a new user, Wilma, comes along to the site
        ## We use a new browser session to make sure none of Fred's info is
        ## coming through from cookies etc.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Wilma visits the home page--no sign of Fred's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Think about what to do', page_text)
        self.assertNotIn('Make a more detailed to-do list', page_text)

        # Wilma starts a new list by entering an item
        inputbox = self.browser.find_element_by_id('new_item_box')
        inputbox.send_keys("Restore peace to the Middle East", Keys.ENTER)

        # Wilma gets her own unique URL
        wilma_list_url = self.browser.current_url
        self.assertRegex(wilma_list_url, 'lists/.+')
        self.assertNotEqual(fred_list_url, wilma_list_url)

        # Wilma's new page lists her item but not Fred's
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn("Restore peace to the Middle East", page_text)
        self.assertNotIn('Think about what to do', page_text)
        self.assertNotIn('Make a more detailed to-do list', page_text)

        # Satisfied, they both go back to sleep
