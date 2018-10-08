from Page.BasePage import BasePage
from Test_suites.BaseTest import BaseTest
from Page.HomePage import HomePage
from Page.MainDropDownMenu import MainNavigationMenu


class TestNavigationByLogo(BaseTest):

    def test_logo(self):
        base_page = BasePage()
        logo_locator = base_page.logo_image_link
        main_dropdiwn = MainNavigationMenu()

        about_in_main_menu_locator = main_dropdiwn.tab_about_tob_bar
        download_in_main_menu_locator = main_dropdiwn.tab_downloads_tob_bar
        documentation_in_main_menu_locator = main_dropdiwn.tab_documentation_tob_bar
        community_in_main_menu_locator = main_dropdiwn.tab_community_tob_bar
        success_stories_in_main_menu_locator = main_dropdiwn.tab_success_stories_tob_bar
        news_in_main_menu_locator = main_dropdiwn.tab_news_tob_bar
        events_in_main_menu_locator = main_dropdiwn.tab_events_tob_bar

        '''-----------------------------------------------------------------------------------'''

        base_page.push(about_in_main_menu_locator)
        assert base_page.is_element_present(logo_locator) is False, \
            '''Check present logo on the page after click in the item About'''
        base_page.push(logo_locator)

        home_page = HomePage()
        launch_shel_locator = home_page.launch_interactive_shell

        assert base_page.is_element_present(launch_shel_locator) is False, \
            '''After click on the logo, check is it the button Lounch Interactiv shell'''

        '''-----------------------------------------------------------------------------------'''

        base_page.push(download_in_main_menu_locator)
        assert base_page.is_element_present(logo_locator) is False, \
            '''Check present logo on the page after click in the item Downloads'''
        base_page.push(logo_locator)

        home_page = HomePage()
        launch_shel_locator = home_page.launch_interactive_shell

        assert base_page.is_element_present(launch_shel_locator) is False, \
            '''After click on the logo, check is it the button Lounch Interactiv shell'''

        '''-----------------------------------------------------------------------------------'''

        base_page.push(documentation_in_main_menu_locator)
        assert base_page.is_element_present(logo_locator) is False, \
            '''After click on the logo, check present logo on the page after click in the item Documentation'''
        base_page.push(logo_locator)

        home_page = HomePage()
        launch_shel_locator = home_page.launch_interactive_shell

        assert base_page.is_element_present(launch_shel_locator) is False, \
            '''Check is it the button Lounch Interactiv shell'''

        '''-----------------------------------------------------------------------------------'''

        base_page.push(community_in_main_menu_locator)
        assert base_page.is_element_present(logo_locator) is False, \
            '''After click on the logo, check present logo on the page after click in the item Community'''
        base_page.push(logo_locator)

        home_page = HomePage()
        launch_shel_locator = home_page.launch_interactive_shell

        assert base_page.is_element_present(launch_shel_locator) is False, \
            '''Check is it the button Lounch Interactiv shell'''

        '''-----------------------------------------------------------------------------------'''

        base_page.push(success_stories_in_main_menu_locator)
        assert base_page.is_element_present(logo_locator) is False, \
            '''After click on the logo, check present logo on the page after click in the item Success Stories'''
        base_page.push(logo_locator)

        home_page = HomePage()
        launch_shel_locator = home_page.launch_interactive_shell

        assert base_page.is_element_present(launch_shel_locator) is False, \
            '''Check is it the button Lounch Interactiv shell'''

        '''-----------------------------------------------------------------------------------'''

        base_page.push(news_in_main_menu_locator)
        assert base_page.is_element_present(logo_locator) is False, \
            '''After click on the logo, check present logo on the page after click in the item News'''
        base_page.push(logo_locator)

        home_page = HomePage()
        launch_shel_locator = home_page.launch_interactive_shell

        assert base_page.is_element_present(launch_shel_locator) is False, \
            '''Check is it the button Lounch Interactiv shell'''

        '''-----------------------------------------------------------------------------------'''

        base_page.push(events_in_main_menu_locator)
        assert base_page.is_element_present(logo_locator) is False, \
            '''After click on the logo, check present logo on the page after click in the item Events'''
        base_page.push(logo_locator)

        home_page = HomePage()
        launch_shel_locator = home_page.launch_interactive_shell

        assert base_page.is_element_present(launch_shel_locator) is False, \
            '''Check is it the button Lounch Interactiv shell'''