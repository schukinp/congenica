from selene.api import *
from time import sleep


class BasePage:
    """Helper class for all pages"""
    def open_url(self, url):
        """Open url"""
        browser.open_url(url)

    def open_link(self, link):
        """Open provided link"""
        link = s(f"a[href='/{link}']")
        link.click()

    def click_green_button(self):
        """Click green button"""
        button = s(".button.success")
        button.click()

    def get_frame_text(self, position, alignment=None):
        """Get iframe text depending on position and alignment"""
        if position == 'top':
            top_frame = browser.driver().find_element_by_css_selector("frame[src='/frame_top']")
            browser.driver().switch_to.frame(top_frame)
            if alignment == 'left':
                left_frame = browser.driver().find_element_by_css_selector("frame[src='/frame_left']")
                return self.switch_to_frame_and_get_text(left_frame)
            elif alignment == 'middle':
                middle_frame = browser.driver().find_element_by_css_selector("frame[src='/frame_middle']")
                return self.switch_to_frame_and_get_text(middle_frame)
            elif alignment == 'right':
                right_frame = browser.driver().find_element_by_css_selector("frame[src='/frame_right']")
                return self.switch_to_frame_and_get_text(right_frame)
        elif position == 'bottom':
            bottom_frame = browser.driver().find_element_by_css_selector("frame[src='/frame_bottom']")
            return self.switch_to_frame_and_get_text(bottom_frame)

    def switch_to_frame_and_get_text(self, frame):
        """Switch to nested frame and extract text"""
        browser.driver().switch_to.frame(frame)
        iframe_text = s('html > body').text
        browser.driver().switch_to.parent_frame()
        browser.driver().switch_to.parent_frame()
        return iframe_text

    def click_start(self):
        """Click start"""
        start_button = s("#start > button")
        start_button.click()

    def check_loader_is_displayed_and_then_disappear(self):
        """Check loader is visible and then not"""
        loader = s("#loading")
        loader.should(be.visible)
        loader.should_not(be.visible, 10)

    def get_finish_text(self):
        """Get finish text"""
        finish_element = s("#finish")
        return finish_element.text

    def get_element_by_row_and_column(self, row, column, edit_link=None, delete_link=None):
        """Find element by row and column"""
        if edit_link:
            column_in_row = browser.driver().find_element_by_xpath(f"//tr[{row}]/td[{column}]/a[1]")
        elif delete_link:
            column_in_row = browser.driver().find_element_by_xpath(f"//tr[{row}]/td[{column}]/a[2]")
        else:
            column_in_row = browser.driver().find_element_by_xpath(f"//tr[{row}]/td[{column}]")
        return column_in_row

    def highlight_element(self, element):
        """Highlight element with yellow color"""
        origin_style = element.get_attribute('style')
        new_style = "background: yellow"
        browser.driver().execute_script("arguments[0].setAttribute('style', arguments[1]);", element, new_style)
        sleep(2)
        browser.driver().execute_script("arguments[0].setAttribute('style', arguments[1]);", element, origin_style)
