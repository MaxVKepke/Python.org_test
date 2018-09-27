import time

from Page.BasePage import BasePage
from Page.BaseTest import BaseTest
from Page.GettingStarted import GettingStarted
from Page.HomePage import HomePage
from Page.IframeWidget import IframeWidget


class TestGettingStarted(BaseTest):

    def test_persent_all_elements(self):
        route_url = '/about/gettingstarted/'
        self.add_rout_in_url_and_go_to_url(route_url)
        getting_started_page = GettingStarted()
        base_page = BasePage()

        elements_on_getting_started_page_locators = getting_started_page.getting_started_element_list
        HomePage().check_element_on_page(elements_on_getting_started_page_locators)

        '''Go to the iframe'''
        iframe_widget = IframeWidget()

        '''Locators in tweets widget'''
        psd_link = iframe_widget.the_psf_link_locator
        button_load_more_tweets = iframe_widget.button_load_more_tweets_locator

        tweets_locator = iframe_widget.tweet_locator
        '''Get list with the tweets'''
        tweets = base_page.get_list_elements(tweets_locator)
        len_tweets = len(tweets)
        print('\n---------len list--------\n' + str(len_tweets))


        base_page.scroll_into_view(button_load_more_tweets)
        base_page.push(button_load_more_tweets)

        '''Get list with the tweets after click in load more tweet button'''
        tweets_after = base_page.get_list_elements(tweets_locator)  #
        len_tweets_after_click = len(tweets_after)
        print('\n-----len after click list------\n' + str(len_tweets_after_click))

        assert len_tweets < len_tweets_after_click, \
            '''Check the len two list'''

        base_page.push(psd_link)
        current_url = base_page.get_current_url()
        expect_url = 'https://twitter.com'
        assert (expect_url in current_url) is False, \
            '''Check on conformity expected url and current url'''




