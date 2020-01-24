from selenium.webdriver.common.by import By

from Page.BasePage import BasePage


class HomePage(BasePage):

    '''
     Widget locators
     '''
    launch_interactive_shell = (By.CSS_SELECTOR, 'div.header-banner')

    launch_interactive_shell_button = (By.CSS_SELECTOR, 'ul.launch-shell.menu a.button.prompt')
    paginate_under_main_menu = (By.CSS_SELECTOR, 'ol.flex-control-nav a.flex-active')
    learn_more = (By.CSS_SELECTOR, 'div.introduction a.readmore')

    launch_interactive_shell_list = [launch_interactive_shell]

    '''--------------------------------------------------------------------------------------------------------------'''

    '''Widgets'''
    widget_get_started = (By.CSS_SELECTOR, 'div.get-started-widget')
    start_with_our_guide = (By.CSS_SELECTOR, 'div.get-started-widget a[href="/about/gettingstarted/"]')

    widget_download = (By.CSS_SELECTOR, 'div.download-widget')
    download_latest = (By.CSS_SELECTOR, 'div.download-widget a[href="/downloads/release/python-370/"]')

    widget_docs = (By.CSS_SELECTOR, 'div.documentation-widget')
    documentation = (By.CSS_SELECTOR, 'div.documentation-widget a[href="https://docs.python.org"]')

    widget_jobs = (By.CSS_SELECTOR, 'div.jobs-widget.last')
    jobs_python_org = (By.CSS_SELECTOR, 'div.jobs-widget a[href="//jobs.python.org"]')

    first_part_widget_list = [widget_get_started, widget_download, widget_docs, widget_jobs]

    '''--------------------------------------------------------------------------------------------------------------'''

    '''Latest News'''
    latest_news_widget = (By.CSS_SELECTOR, 'div.medium-widget.blog-widget')
    news = (By.CSS_SELECTOR, 'div.blog-widget ul.menu a')
    more_news_link = (By.CSS_SELECTOR, 'div.blog-widget a[href="http://blog.python.org"]')

    '''Upcoming Events'''
    upcoming_events = (By.CSS_SELECTOR, 'div.medium-widget.event-widget.last')
    events = (By.CSS_SELECTOR, 'div.event-widget ul.menu a')
    more_events_link = (By.CSS_SELECTOR, 'div.event-widget  a[href="/events/calendars/"]')

    second_part_widget_list = [latest_news_widget, upcoming_events]

    '''--------------------------------------------------------------------------------------------------------------'''

    '''Success Stories'''
    success_stories_widget = (By.CSS_SELECTOR, 'div.medium-widget.success-stories-widget')
    more_stories_link = (By.CSS_SELECTOR, 'div.success-stories-widget a[href="/success-stories/"]')
    industrial_light = (By.CSS_SELECTOR, 'div.success-stories-widget a[href="/success-stories/industrial-light-magic-runs-python/"]')

    '''Use Python for...'''
    use_python_for = (By.CSS_SELECTOR, 'div.medium-widget.applications-widget.last')

    '''Web Development'''
    django_link = (By.CSS_SELECTOR, 'span.tag-wrapper a[href="http://www.djangoproject.com/"]')
    pyramid_link = (By.CSS_SELECTOR, 'span.tag-wrapper a.[href="http://www.pylonsproject.org/"]')
    bottle_link = (By.CSS_SELECTOR, 'span.tag-wrapper a.[href="http://bottlepy.org"]')
    tornado_link = (By.CSS_SELECTOR, 'span.tag-wrapper a.[href="http://tornadoweb.org"]')
    flask_link = (By.CSS_SELECTOR, 'span.tag-wrapper a.[href="http://flask.pocoo.org/"]')
    web2py_link = (By.CSS_SELECTOR, 'span.tag-wrapper a.[href="http://www.web2py.com/"]')

    '''GUI Development'''
    tklter_link = (By.CSS_SELECTOR, 'span.tag-wrapper a.[href="http://wiki.python.org/moin/TkInter"]')
    PyGObject_link = (By.CSS_SELECTOR, 'span.tag-wrapper a.[href="https://wiki.gnome.org/Projects/PyGObject"]')
    PyQt_link = (By.CSS_SELECTOR, 'span.tag-wrapper a.[href="http://www.riverbankcomputing.co.uk/software/pyqt/intro"]')
    PySide_link = (By.CSS_SELECTOR, 'span.tag-wrapper a.[href="https://wiki.qt.io/PySide"]')
    Kivy_link = (By.CSS_SELECTOR, 'span.tag-wrapper a.[href="https://kivy.org/"]')
    wxPython_link = (By.CSS_SELECTOR, 'span.tag-wrapper a.[href="http://www.wxpython.org/"]')

    third_part_widget_list = [success_stories_widget, use_python_for]

    '''--------------------------------------------------------------------------------------------------------------'''

    '''Python Enhancement Proposals'''
    python_enhancement_proposals = (By.CSS_SELECTOR, 'div.pep-widget')
    python_proposals_link = (By.CSS_SELECTOR, 'a[href = "/dev/peps/"]')
    rss_button = (By.CSS_SELECTOR, 'a.rss-link')

    '''Python Software Foundation'''
    python_software_foundation_widget = (By.CSS_SELECTOR, 'div.psf-widget')
    python_software_foundation_link = (By.CSS_SELECTOR, 'div.psf-widget a[href="/psf/"]')
    become_a_member_button = (By.CSS_SELECTOR, 'div.psf-widget a[href="/users/membership/"]')
    donate_to_the_PSF_button = (By.CSS_SELECTOR, 'div.psf-widget a[href="/psf/donations/"]')

    fourth_part_widget_list = [python_enhancement_proposals, python_software_foundation_widget]

    '''--------------------------------------------------------------------------------------------------------------'''


