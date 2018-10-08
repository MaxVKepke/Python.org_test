import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilities.DriverWrapper import DriverWrapper


class BasePage(object):

    '''Upper top-bar menu in header'''
    top_par_menu = (By.CSS_SELECTOR, 'div.top-bar.do-not-print')

    button_Python_header = (By.CSS_SELECTOR, 'li.python-meta a[href="/"]')
    button_psf_header = (By.CSS_SELECTOR, 'li.psf-meta a[href="/psf-landing/"]')
    button_Docs_header = (By.CSS_SELECTOR, 'li.docs-meta a[href="https://docs.python.org"]')
    button_PypI_header = (By.CSS_SELECTOR, 'li.pypi-meta a[href="https://pypi.python.org/"]')
    button_Jobs_header = (By.CSS_SELECTOR, 'li.jobs-meta a[href="/jobs/"]')
    button_Community_header = (By.CSS_SELECTOR, 'li.shop-meta a[href="/community/"]')

    '''Log-image'''
    logo_image_link = (By.CSS_SELECTOR, 'img.python-logo')

    '''Search menu'''
    search_widget = (By.CSS_SELECTOR, 'div.options-bar.do-not-print')

    search_icon = (By.CSS_SELECTOR, 'span.icon-search')
    input_search_field = (By.CSS_SELECTOR, 'input.search-field.placeholder')
    button_go_locator = (By.CSS_SELECTOR, 'button.search-button')
    button_socialize = (By.CSS_SELECTOR, 'li.tier-1.last a.action-trigger')

    header_element_list = [top_par_menu, logo_image_link, search_widget,]

    '''Navigation menu in footer'''
    top_part_footer = (By.CSS_SELECTOR, 'ul.sitemap.navigation.menu.do-not-print')

    about_in_footer = (By.CSS_SELECTOR, 'ul.sitemap.navigation.menu.do-not-print li.element-1')
    getting_started_in_footer = (By.CSS_SELECTOR, 'ul.sitemap.navigation.menu.do-not-print a[href="/about/gettingstarted/"]')

    download_in_footer = (By.CSS_SELECTOR, 'ul.sitemap.navigation.menu.do-not-print li.element-2')
    mac_os_x_in_footer = (By.CSS_SELECTOR, 'ul.sitemap.navigation.menu.do-not-print a[href="/downloads/mac-osx/"]')

    documentation_in_footer = (By.CSS_SELECTOR, 'ul.sitemap.navigation.menu.do-not-print li.element-3')
    audio_visual_talks_part_footer = (By.CSS_SELECTOR, 'ul.sitemap.navigation.menu.do-not-print a[href="/doc/av"]')

    community_in_footer = (By.CSS_SELECTOR, 'ul.sitemap.navigation.menu.do-not-print li.element-4')
    diversity_footer = (By.CSS_SELECTOR, 'ul.sitemap.navigation.menu.do-not-print a[href="/community/diversity/"]')

    success_stories_in_footer = (By.CSS_SELECTOR, 'ul.sitemap.navigation.menu.do-not-print li.element-5')
    arts_footer = (By.CSS_SELECTOR, 'ul.sitemap.navigation.menu.do-not-print a[href="/about/success/#arts"]')

    news_in_footer = (By.CSS_SELECTOR, 'ul.sitemap.navigation.menu.do-not-print li.element-6')
    psf_news_footer = (By.CSS_SELECTOR, 'ul.sitemap.navigation.menu.do-not-print a[href="http://pyfound.blogspot.com/"]')

    contributing_footer = (By.CSS_SELECTOR, 'ul.sitemap.navigation.menu.do-not-print li.element-7')
    core_mentorship_footer = (By.CSS_SELECTOR, 'ul.sitemap.navigation.menu.do-not-print a[href="/dev/core-mentorship/"]')

    events_in_footer = (By.CSS_SELECTOR, 'ul.sitemap.navigation.menu.do-not-print li.element-8')
    python_events_footer = (By.CSS_SELECTOR, 'ul.sitemap.navigation.menu.do-not-print a[href="/events/python-events"]')

    navigation_menu_in_footer_list = [top_part_footer, about_in_footer, download_in_footer, documentation_in_footer,
                                      community_in_footer, success_stories_in_footer, news_in_footer,
                                      contributing_footer, events_in_footer]

    '''Lower part of footer'''
    footer_links_navigation = (By.CSS_SELECTOR, 'ul.footer-links.navigation.menu.do-not-print')

    tab_help_and_general = (By.CSS_SELECTOR, 'ul.footer-links.navigation.menu.do-not-print" a.[href="/about/help/"]')
    tab_diversity = (By.CSS_SELECTOR, 'ul.footer-links.navigation.menu.do-not-print" a[href="/community/diversity/"]')
    tab_submit = (By.CSS_SELECTOR, 'ul.footer-links.navigation.menu.do-not-print" a[href="https://github.com/python/pythondotorg/issues"]')
    tab_status = (By.CSS_SELECTOR, 'ul.footer-links.navigation.menu.do-not-print" a[href="https://status.python.org/"]')

    copyright_links_navigation = (By.CSS_SELECTOR, 'div.container div.copyright')

    lower_part_of_footer_list = [footer_links_navigation, copyright_links_navigation]
    '''======================================================================================================'''

    wait_element_time = 10

    def __init__(self):
        self.driver = DriverWrapper.get_webdriver()
        self.wait = WebDriverWait(self.driver, self.wait_element_time)

    def push(self, element_locator):
        """Bush on elements with some locator"""
        button = self.wait.until(EC.presence_of_element_located(element_locator), 'There is no input')
        push = button.click()
        return push

    def is_element_present(self, field_locator, error='There is no element on page'):
        """Wait element on page until element presence"""
        field = self.wait.until(EC.presence_of_element_located(field_locator), error)
        if field is True:
            return field
        else:
            return False

    def back_to_privies_page(self, field_locator):
        """If element not found back to privies page"""
        try:
            self.wait.until(EC.presence_of_element_located(field_locator))
            return True
        except:
            self.driver.back()

    def enable_drop_down(self, element_locator):
        """Move to element with drop-dawn"""
        find_elements = self.wait.until(EC.presence_of_element_located(element_locator))
        ActionChains(self.driver).move_to_element(find_elements).perform()
        return find_elements

    def get_current_url(self):
        """Get url page which you are"""
        url = self.driver.current_url
        print('\n---------CURRENT URL-------------\n' + url)
        return url

    def scroll_into_view(self, element_locator):
        """Scroll page to the element"""
        button = self.wait.until(EC.presence_of_element_located(element_locator))
        self.driver.execute_script("return arguments[0].scrollIntoView();", button)

    def check_element_on_page(self, list_of_element_locator):
        """Check present element on page"""
        """Browse the list elements"""
        for widget in list_of_element_locator:
            assert self.is_element_present(widget) is False, \
                '''Check present widget on hom page'''
            print('\n----------------------------\n' + str(widget))

    def get_list_elements(self, element_locator):
        time.sleep(0.5)
        list_elements = self.wait.until(EC.presence_of_all_elements_located(element_locator))
        return list_elements

