from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Page.BasePage import BasePage


class IframeWidget(BasePage):

    the_psf_link_locator = (By.CSS_SELECTOR, 'a.customisable-highlight')
    button_load_more_tweets_locator = (By.CSS_SELECTOR, 'button.timeline-LoadMore-prompt')

    tweet_locator = (By.CSS_SELECTOR, 'li.timeline-TweetList-tweet.customisable-border')

    def __init__(self):
        super(IframeWidget, self).__init__()
        self.iframe = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
        self.driver.switch_to_frame(self.iframe)
        self.wait = WebDriverWait(self.driver, self.wait_element_time)

    '''Switch from iframe to main content '''
    def switch_to_main_content(self, element_locator):
        self.driver.switch_to_default_content()
        assert BasePage().is_element_present(element_locator) is False, \
            '''Check is there, block with element locator present on page, after exit the iframe'''


