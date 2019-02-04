from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from Page.BasePage import BasePage


class MainNavigationMenu(BasePage):

    '''Main navigation bar'''
    main_nav_bar = (By.CSS_SELECTOR, 'nav.main-navigation')

    '''About drop-down menu'''
    tab_about_tob_bar = (By.CSS_SELECTOR, 'ul.navigation.menu a[href="/about/"]')

    item_apps_locator = (By.CSS_SELECTOR, 'li#about li.element-1 a[href="/about/apps/"]')
    item_quotes_locator = (By.CSS_SELECTOR, 'li#about li.element-2 a[href="/about/quotes/"]')
    item_getting_started_locator = (By.CSS_SELECTOR, 'li#about li.element-3 a[href="/about/gettingstarted/"]')
    item_help_locator = (By.CSS_SELECTOR, 'li#about li.element-4 a[href="/about/help/"]')
    item_brochure_locator = (By.CSS_SELECTOR, 'li#about li.element-5 a[href="http://brochure.getpython.info/"]')

    '''Downloads drop-down menu'''
    tab_downloads_tob_bar = (By.CSS_SELECTOR, 'ul.navigation.menu a[href="/downloads/"]')

    item_all_releases_locator = (By.CSS_SELECTOR, 'li#downloads li.element-1 a[href="/downloads/"]')
    item_source_code_locator = (By.CSS_SELECTOR, 'li#downloads li.element-2 a[href="/downloads/source/"]')
    item_windows_locator = (By.CSS_SELECTOR, 'li#downloads li.element-3 a[href="/downloads/windows/"]')
    item_mac_os_x_locator = (By.CSS_SELECTOR, 'li#downloads li.element-4 a[href="/downloads/mac-osx/"]')
    item_other_platforms_locator = (By.CSS_SELECTOR, 'li#downloads li.element-5 a[href="/download/other/"]')
    item_license_locator = (By.CSS_SELECTOR, 'li#downloads li.element-6 a[href="https://docs.python.org/3/license.html"]')
    item_implementations_locator = (By.CSS_SELECTOR, 'li#downloads li.element-7 a[href="/download/alternatives"]')

    '''Documentation drop-down menu'''
    tab_documentation_tob_bar = (By.CSS_SELECTOR, 'ul.navigation.menu a[href="/doc/"]')

    item_docs_locator = (By.CSS_SELECTOR, 'li#documentation li.element-1 a[href="/doc/"]')
    item_talks_locator = (By.CSS_SELECTOR, 'li#documentation li.element-2 a[href="/doc/av"]')
    item_begin_guide_locator = (By.CSS_SELECTOR, 'li#documentation li.element-3 a[href="https://wiki.python.org/moin/BeginnersGuide"]')
    item_develop_guide_locator = (By.CSS_SELECTOR, 'li#documentation li.element-4 a[href="https://devguide.python.org/"]')
    item_faq_locator = (By.CSS_SELECTOR, 'li#documentation li.element-5 a[href="https://docs.python.org/faq/"]')
    item_english_docs_locator = (By.CSS_SELECTOR, 'li#documentation li.element-6 a[href="http://wiki.python.org/moin/Languages"]')
    item_pep_index_locator = (By.CSS_SELECTOR, 'li#documentation li.element-7 a[href="http://python.org/dev/peps/"]')
    item_python_books_locator = (By.CSS_SELECTOR, 'li#documentation li.element-8 a[href="https://wiki.python.org/moin/PythonBooks"]')
    item_python_essays_locator = (By.CSS_SELECTOR, 'li#documentation li.element-9 a[href="/doc/essays/"]')

    '''Community drop-down menu'''
    tab_community_tob_bar = (By.CSS_SELECTOR, 'ul.navigation.menu a[href="/community/"]')

    item_survey_locator = (By.CSS_SELECTOR, 'li#community li.element-1 a[href="/community/survey"]')
    item_diversity_locator = (By.CSS_SELECTOR, 'li#community li.element-2 a[href="/community/diversity/"]')
    item_lists_locator = (By.CSS_SELECTOR, 'li#community li.element-3 a[href="/community/lists/"]')
    item_irc_locator = (By.CSS_SELECTOR, 'li#community li.element-4 a[href="/community/irc/"]')
    item_forums_locator = (By.CSS_SELECTOR, 'li#community li.element-5 a[href="/community/forums/"]')
    item_workshops_locator = (By.CSS_SELECTOR, 'li#community li.element-6 a[href="/community/workshops/"]')
    item_sigs_locator = (By.CSS_SELECTOR, 'li#community li.element-7 a[href="/community/sigs/"]')
    item_logos_locator = (By.CSS_SELECTOR, 'li#community li.element-8 a[href="/community/logos/"]')
    item_moin_locator = (By.CSS_SELECTOR, 'li#community li.element-9 a[href="https://wiki.python.org/moin/"]')
    item_merchandise_locator = (By.CSS_SELECTOR, 'li#community li.element-10 a[href="/community/merchandise/"]')
    item_awards_locator = (By.CSS_SELECTOR, 'li#community li.element-11 a[href="/community/awards"]')
    item_codeofconduct_locator = (
    By.CSS_SELECTOR, 'li#community li.element-12 a[href="https://www.python.org/psf/codeofconduct/"]')

    '''Success stories drop-down menu'''
    tab_success_stories_tob_bar = (By.CSS_SELECTOR, 'ul.navigation.menu a[href="/success-stories/"]')

    item_arts_locator = (By.CSS_SELECTOR, 'li#success-stories li.element-1 a[href*="arts"]')
    item_business_locator = (By.CSS_SELECTOR, 'li#success-stories li.element-2 a[href*="business"]')
    item_education_locator = (By.CSS_SELECTOR, 'li#success-stories li.element-3 a[href*="education"]')
    item_engineering_locator = (By.CSS_SELECTOR, 'li#success-stories li.element-4 a[href*="engineering"]')
    item_government_locator = (By.CSS_SELECTOR, 'li#success-stories li.element-5 a[href*="government"]')
    item_scientific_locator = (By.CSS_SELECTOR, 'li#success-stories li.element-6 a[href*="scientific"]')
    item_development_locator = (By.CSS_SELECTOR, 'li#success-stories li.element-7 a[href*="software-development"]')

    '''News drop-down menu'''
    tab_news_tob_bar = (By.CSS_SELECTOR, 'ul.navigation.menu a[href="/blogs/"]')

    item_blogs_locator = (By.CSS_SELECTOR, 'li#news li.element-1 a[href="/blogs/"]')
    item_planetpython_locator = (By.CSS_SELECTOR, 'li#news li.element-2 a[href="http://planetpython.org/"]')
    item_psf_locator = (By.CSS_SELECTOR, 'li#news li.element-3 a[href="http://pyfound.blogspot.com/"]')
    item_pycon_locator = (By.CSS_SELECTOR, 'li#news li.element-4 a[href="http://pycon.blogspot.com/"]')

    '''Events drop-down menu'''
    tab_events_tob_bar = (By.CSS_SELECTOR, 'ul.navigation.menu a[href="/events/"]')

    item_events_locator = (By.CSS_SELECTOR, 'li#news li.element-1 a[href="/events/python-events""]')
    item_group_locator = (By.CSS_SELECTOR, 'li#news li.element-2 a[href="/events/python-user-group/"]')
    item_archive_locator = (By.CSS_SELECTOR, 'li#news li.element-3 a[href="/events/python-events/past/"]')
    item_user_archive_locator = (By.CSS_SELECTOR, 'li#news li.element-4 a[href="/events/python-user-group/past/"]')
    item_submit_locator = (By.CSS_SELECTOR, 'li#news li.element-5 a[href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event"]')

    main_nav_bar_list_elements = [main_nav_bar, tab_about_tob_bar, tab_downloads_tob_bar, tab_documentation_tob_bar,
                                  tab_success_stories_tob_bar, tab_news_tob_bar, tab_events_tob_bar]

    def is_element_visible(self, element_locator):
        if self.wait.until(EC.visibility_of_element_located(element_locator)) is True:
            return True
        else:
            return False
