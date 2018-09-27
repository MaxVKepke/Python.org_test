from selenium.webdriver.common.by import By


from Page.BasePage import BasePage


class GettingStarted(BasePage):


    '''Main content'''
    main_content = (By.CSS_SELECTOR, 'section.main-content.with-left-sidebar')
    navigation_menu = (By.CSS_SELECTOR, 'ul.breadcrumbs.menu')
    text_content = (By.CSS_SELECTOR, 'article.text')

    '''Tweets panel'''
    left_sidebar = (By.CSS_SELECTOR, 'aside.left-sidebar')
    twitter_widget = (By.CSS_SELECTOR, 'div.twitter-widget.sidebar-widget')
    psf_widget = (By.CSS_SELECTOR, 'div.psf-sidebar-widget.sidebar-widget')

    getting_started_element_list = [main_content, navigation_menu, text_content, left_sidebar, twitter_widget, psf_widget]

