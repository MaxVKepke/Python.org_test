from Page.BasePage import BasePage
from Test_suites.BaseTest import BaseTest
from Page.MainDropDownMenu import MainNavigationMenu


class TestElements(BaseTest):

    def test_drop_down_in_top_bar(self):

        navigator_menu = MainNavigationMenu()
        base_page = BasePage()

        documentation_item = navigator_menu.tab_documentation_tob_bar
        docs_item = navigator_menu.item_docs_locator
        talk_item = navigator_menu.item_talks_locator
        begin_guide_item = navigator_menu.item_begin_guide_locator
        develop_guide_item = navigator_menu.item_develop_guide_locator
        faq_item = navigator_menu.item_faq_locator
        english_docs_item = navigator_menu.item_english_docs_locator
        pep_index_item = navigator_menu.item_pep_index_locator
        python_books_item = navigator_menu.item_python_books_locator
        python_essays_item = navigator_menu.item_python_essays_locator

        base_page.enable_drop_down(documentation_item)
        navigator_menu.enable_drop_down(docs_item)
        assert navigator_menu.is_element_visible(docs_item) is False, \
            '''Check on the main page in the main bar, documentation drop-down visible item Docs or not '''

        navigator_menu.enable_drop_down(talk_item)
        assert navigator_menu.is_element_visible(talk_item) is False, \
            '''Check on the main page in the main bar, documentation drop-down visible item Talk or not '''

        navigator_menu.enable_drop_down(begin_guide_item)
        assert navigator_menu.is_element_visible(begin_guide_item) is False, \
            '''Check on the main page in the main bar, documentation drop-down visible item Begin Guide or not '''

        navigator_menu.enable_drop_down(develop_guide_item)
        assert navigator_menu.is_element_visible(develop_guide_item) is False, \
            '''Check on the main page in the main bar, documentation drop-down visible item Guide or not '''

        navigator_menu.enable_drop_down(faq_item)
        assert navigator_menu.is_element_visible(faq_item) is False, \
            '''Check on the main page in the main bar, documentation drop-down visible item Faq or not '''

        navigator_menu.enable_drop_down(english_docs_item)
        assert navigator_menu.is_element_visible(english_docs_item) is False, \
            '''Check on the main page in the main bar, documentation drop-down visible item English Docs or not '''

        navigator_menu.enable_drop_down(pep_index_item)
        assert navigator_menu.is_element_visible(pep_index_item) is False, \
            '''Check on the main page in the main bar, documentation drop-down visible item Index or not '''

        navigator_menu.enable_drop_down(python_books_item)
        assert navigator_menu.is_element_visible(python_books_item) is False, \
            '''Check visible item Python Books or not '''

        navigator_menu.enable_drop_down(python_essays_item)
        assert navigator_menu.is_element_visible(python_essays_item) is False, \
            '''Check visible item Python Essays or not '''

        success_stories_item = navigator_menu.tab_success_stories_tob_bar
        arts_item = navigator_menu.item_arts_locator
        business_item = navigator_menu.item_business_locator
        education_item = navigator_menu.item_education_locator
        engineering_item = navigator_menu.item_engineering_locator
        government_item = navigator_menu.item_government_locator
        scientific_item = navigator_menu.item_scientific_locator
        development_item = navigator_menu.item_development_locator

        base_page.enable_drop_down(success_stories_item)
        navigator_menu.enable_drop_down(arts_item)
        assert navigator_menu.is_element_visible(arts_item) is False, \
            '''Check visible item Arts or not '''

        navigator_menu.enable_drop_down(business_item)
        assert navigator_menu.is_element_visible(business_item) is False, \
            '''Check visible item Business or not '''

        navigator_menu.enable_drop_down(education_item)
        assert navigator_menu.is_element_visible(education_item) is False, \
            '''Check visible item Education or not '''

        navigator_menu.enable_drop_down(engineering_item)
        assert navigator_menu.is_element_visible(engineering_item) is False, \
            '''Check visible item Engineering or not '''

        navigator_menu.enable_drop_down(government_item)
        assert navigator_menu.is_element_visible(government_item) is False, \
            '''Check visible item Government or not '''

        navigator_menu.enable_drop_down(scientific_item)
        assert navigator_menu.is_element_visible(scientific_item) is False, \
            '''Check visible item Scientific or not '''

        navigator_menu.enable_drop_down(development_item)
        assert navigator_menu.is_element_visible(development_item) is False, \
            '''Check visible item Development or not '''

    def test_navigation_from_main_navigation_bar(self):
        navigator_menu = MainNavigationMenu()
        base_page = BasePage()

        success_stories_item = navigator_menu.tab_success_stories_tob_bar
        arts_item = navigator_menu.item_arts_locator
        business_item = navigator_menu.item_business_locator

        '''Enable drop-down menu'''
        base_page.enable_drop_down(success_stories_item)

        '''Click in item in drop-down menu'''
        item_arts = navigator_menu.enable_drop_down(arts_item)
        item_arts.click()
        text = 'success'
        current_url = base_page.get_current_url()

        assert (text in current_url), \
            '''Check some text in url'''

        '''If element not fount beck in privies pages'''
        base_page.back_to_privies_page(business_item)

        '''Enable drop-down menu'''
        base_page.enable_drop_down(success_stories_item)

        '''Click in item in drop-down menu'''
        item_business = navigator_menu.enable_drop_down(business_item)
        item_business.click()

        text = 'business'
        current_url = base_page.get_current_url()

        assert (text in current_url), \
            '''Check some text in url'''