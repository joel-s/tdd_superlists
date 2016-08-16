from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Fred visits the to-do list home page
        self.browser.get("http://localhost:8000")

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
        inputbox.send_keys("Think about what to do")

        # When he types Enter, the page updates and now lists
        # "1: Think about..."
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('todo_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1. Think about what to do', [row.text for row in rows])

        # There is still a text box inviting him to add another item
        self.fail("Finish the test!")

        # He enters "Make a more detailed to-do list" and presses Enter

        # The page updates again, and now shows both items on the list

        # Fred sees a statement that the site has generated a unique URL for
        # his list

        # Fred visits the URL, and sees that his to-do list is there

if __name__ == '__main__':
    unittest.main()
