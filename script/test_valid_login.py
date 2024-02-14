from generic.base_file import BaseTest
from page.login_page import LoginPage
from page.home_page import HomePage

class Test_ValidLogin(BaseTest):

    def test_valid_login(self):
        # 1. enter valid username
            login_page=LoginPage(self.driver)
            login_page.enter_username('admin')
        # 2. enter valid password
            login_page.enter_password('pointofsale')
        # 3. click go
            login_page.click_go_button()
        # 4. verify that homepage is displayed
            home_page=HomePage(self.driver)
            result = home_page.verify_home_page_is_displayed(self.wait)
            assert result