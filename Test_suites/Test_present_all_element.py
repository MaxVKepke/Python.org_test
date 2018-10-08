from Page.BasePage import BasePage
from Test_suites.BaseTest import BaseTest
from Page.HomePage import HomePage
from Page.MainDropDownMenu import MainNavigationMenu


class TestAllElements(BaseTest):

    def test_present_elements(self):
        """Test present all element on home page"""

        home_page = HomePage()
        base_page = BasePage()

        '''Lists with locator'''
        header_element_list_locators = base_page.header_element_list
        main_nav_bar_list_elements_locator = MainNavigationMenu.main_nav_bar_list_elements
        launch_interactive_shell_list_locator = home_page.launch_interactive_shell_list
        first_part_widgets_list_locator = home_page.first_part_widget_list
        second_part_widget_list_locator = home_page.second_part_widget_list
        third_part_widget_list_locator = home_page.third_part_widget_list
        fourth_part_widget_list_locator = home_page.fourth_part_widget_list
        navigation_menu_in_footer_list_locator = base_page.navigation_menu_in_footer_list
        lower_part_of_footer_list_locator = base_page.lower_part_of_footer_list

        '''check present widget in home page'''
        home_page.check_element_on_page(header_element_list_locators)

        home_page.check_element_on_page(main_nav_bar_list_elements_locator)
        home_page.check_element_on_page(launch_interactive_shell_list_locator)
        home_page.check_element_on_page(first_part_widgets_list_locator)
        home_page.check_element_on_page(second_part_widget_list_locator)
        home_page.check_element_on_page(third_part_widget_list_locator)
        home_page.check_element_on_page(fourth_part_widget_list_locator)
        home_page.check_element_on_page(navigation_menu_in_footer_list_locator)
        home_page.check_element_on_page(lower_part_of_footer_list_locator)