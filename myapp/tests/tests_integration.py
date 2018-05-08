from selenium import webdriver
from django.test import LiveServerTestCase
import os
from myapp.models import Person
from selenium.webdriver.chrome.options import Options

class TestIntegration(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(TestIntegration, cls).setUpClass()
        options = Options()
        options.add_argument("--headless")
        cls.driver = webdriver.Chrome(os.environ.get('WEBDRIVER'), chrome_options=options)
        cls.driver.set_window_size(1000, 550)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_flow(self):
        self.driver.get('%s/people/create/' % self.live_server_url)
        self.driver.find_element_by_id('id_fname').send_keys('fname')
        self.driver.find_element_by_id('id_lname').send_keys('lname')
        self.driver.find_element_by_id('id_age').send_keys('11')
        self.driver.find_elements_by_css_selector('input[type="submit"]')[0].click()

        # WebDriverWait(self.driver, 5).until(lambda driver: 'list' in driver.current_url)
        p = Person.objects.filter(fname='fname', lname='lname', age=11)
        uuid = p[0].uuid
        self.assertEqual(len(p), 1)

        # Make sure edit is working
        self.driver.get('%s/people/edit/%s/' % (self.live_server_url, uuid))
        self.assertEqual(self.driver.find_element_by_id('id_fname').get_property('value'), 'fname')
        self.assertEqual(self.driver.find_element_by_id('id_lname').get_property('value'), 'lname')
        self.assertEqual(self.driver.find_element_by_id('id_age').get_property('value'), '11')

        # Update object
        self.driver.find_element_by_id('id_age').clear()
        self.driver.find_element_by_id('id_age').send_keys('12')
        self.driver.find_elements_by_css_selector('input[type="submit"]')[0].click()
        p = Person.objects.filter(uuid=uuid)
        self.assertEqual(len(p), 1)

        p = p[0]
        self.assertEqual(p.fname, 'fname')
        self.assertEqual(p.lname, 'lname')
        self.assertEqual(p.age, 12)

        self.driver.get('%s/people/delete/%s/' % (self.live_server_url, uuid))
        self.driver.find_elements_by_css_selector('input[type="submit"]')[0].click()
        p = Person.objects.filter(uuid=uuid)
        self.assertEqual(len(p), 0)
