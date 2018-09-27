import time

from Page.BasePage import BasePage
from Page.BaseTest import BaseTest


class TestFooter(BaseTest):

    def test_navigation_menu_in_footer(self):
        base_page = BasePage()
        getting_started_in_footer_locator = base_page.getting_started_in_footer
        mac_os_x_in_footer_locator = base_page.mac_os_x_in_footer
        audio_visual_talks_part_footer_locator = base_page.audio_visual_talks_part_footer
        diversity_footer_locator = base_page.diversity_footer
        arts_footer_locator = base_page.arts_footer
        psf_news_footer_locator = base_page.psf_news_footer
        core_mentorship_footer_locator = base_page.core_mentorship_footer
        python_events_footer_locator = base_page.python_events_footer

        footer_locator = base_page.top_part_footer

        base_page.scroll_into_view(footer_locator)
        time.sleep(0.5)
        base_page.push(getting_started_in_footer_locator)
        current_url = base_page.get_current_url()

        text = 'gettingstarted'
        assert (text in current_url), \
            ''''''

        '''---------------------------------------------------------------------------------------'''

        base_page.scroll_into_view(footer_locator)
        time.sleep(0.5)
        base_page.push(mac_os_x_in_footer_locator)
        current_url = base_page.get_current_url()

        text = 'mac-osx'
        assert (text in current_url), \
            ''''''

        '''---------------------------------------------------------------------------------------'''

        base_page.scroll_into_view(footer_locator)
        time.sleep(0.5)
        base_page.push(audio_visual_talks_part_footer_locator)
        current_url = base_page.get_current_url()

        text = 'av'
        assert (text in current_url), \
            ''''''

        '''---------------------------------------------------------------------------------------'''

        base_page.scroll_into_view(footer_locator)
        time.sleep(0.5)
        base_page.push(diversity_footer_locator)
        current_url = base_page.get_current_url()

        text = 'diversity'
        assert (text in current_url), \
            ''''''

        '''---------------------------------------------------------------------------------------'''

        base_page.scroll_into_view(footer_locator)
        time.sleep(0.5)
        base_page.push(arts_footer_locator)
        current_url = base_page.get_current_url()

        text = 'arts'
        assert (text in current_url), \
            ''''''

        '''---------------------------------------------------------------------------------------'''

        base_page.scroll_into_view(footer_locator)
        time.sleep(0.5)
        base_page.push(psf_news_footer_locator)
        current_url = base_page.get_current_url()

        text = 'blogspot'
        assert (text in current_url), \
            ''''''

        '''---------------------------------------------------------------------------------------'''

        base_page.back_to_privies_page(core_mentorship_footer_locator)
        base_page.scroll_into_view(footer_locator)
        time.sleep(0.5)
        base_page.push(core_mentorship_footer_locator)
        current_url = base_page.get_current_url()

        text = 'mentorship'
        assert (text in current_url), \
            ''''''

        '''---------------------------------------------------------------------------------------'''

        base_page.scroll_into_view(footer_locator)
        time.sleep(0.5)
        base_page.push(python_events_footer_locator)
        current_url = base_page.get_current_url()

        text = 'events'
        assert (text in current_url), \
            ''''''

        '''---------------------------------------------------------------------------------------'''