
import pytest

from utilities.DriverWrapper import DriverWrapper


@pytest.mark.usefixtures('get_browser_name')
@pytest.mark.usefixtures('get_base_url')
@pytest.mark.usefixtures('get_base_host')
class BaseTest(object):

    def setup(self):
        self.driver = DriverWrapper.get_webdriver()
        try:
            self.driver.maximize_window()
            self.driver.get(self.base_url)

        except Exception as error:
            DriverWrapper.close_driver()
            pytest.fail('Setup test failed: {}'.format(error))

    def teardown(self):
        DriverWrapper.close_driver()

    def add_rout_in_url_and_go_to_url(self, url):
        """Get base url, add routs in the base url and go in to the url with routs"""
        print('______________base URL_____________')
        print(self.base_url)
        base_url = self.base_url
        edit_url = base_url + url
        print('\n-------edit-url-----------\n' + str(edit_url))
        self.driver.get(edit_url)
        return self



