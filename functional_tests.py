from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_start_a_list_and_retrieve_it_later(self):
        # Fred visits the to-do list home page
        self.browser.get("http://localhost:8000")

        # He observes that the title say something about To-Do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Test not fully implemented')

        # The page invites him to enter a to-do item

        # He types "Think about what to do"

        # When he types Enter, the page updates and now lists
        # "1: Think about..."

        # There is still a text box inviting him to add another item

        # He enters "Make a more detailed to-do list" and presses Enter

        # The page updates again, and now shows both items on the list

        # Fred sees a statement that the site has generated a unique URL for
        # his list

        # Fred visits the URL, and sees that his to-do list is there

if __name__ == '__main__':
    unittest.main()
