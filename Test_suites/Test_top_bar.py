
from Test_suites.BaseTest import BaseTest
from Page.BasePage import BasePage


class TestTopBar(BaseTest):

    def test_button_in_top_bar(self):
        base_page = BasePage()

        button_python_locator = base_page.button_Python_header
        button_psf_locator = base_page.button_psf_header
        button_docs_locator = base_page.button_Docs_header
        button_pypi_locator = base_page.button_PypI_header
        button_jobs_locator = base_page.button_Jobs_header
        button_community_locator = base_page.button_Community_header

        """Checking top-bar menu is worked"""

        assert base_page.is_element_present(button_python_locator) is False, \
            "Check present button Python in top-menu in main page"
        base_page.push(button_python_locator)

        assert base_page.is_element_present(button_psf_locator) is False, \
            "Check present button PSF in top-menu in main page"
        base_page.push(button_psf_locator)

        assert base_page.is_element_present(button_docs_locator) is False, \
            "Check present button Docs in top-menu in main page"
        base_page.push(button_docs_locator)
        base_page.back_to_privies_page(button_docs_locator)

        assert base_page.is_element_present(button_pypi_locator) is False, \
            "Check present button PyPI in top-menu in main page"
        base_page.push(button_pypi_locator)
        base_page.back_to_privies_page(button_pypi_locator)

        assert base_page.is_element_present(button_jobs_locator) is False, \
            "Check present button Jobs in top-menu in main page"
        base_page.push(button_jobs_locator)

        assert base_page.is_element_present(button_community_locator) is False, \
            "Check present button Community in top-menu in main page"
        base_page.push(button_community_locator)








