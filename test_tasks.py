from base_page import BasePage
from conftest import base_url
import pytest


@pytest.mark.usefixtures('setup')
class TestTasks(BasePage):
    def test_task_one(self):
        self.open_url(base_url)
        self.open_link("frames")
        self.open_link("nested_frames")
        bottom_text = self.get_frame_text("bottom")
        left_text = self.get_frame_text("top", "left")
        right_text = self.get_frame_text("top", "right")
        middle_text = self.get_frame_text("top", "middle")
        print(middle_text)
        print(bottom_text)
        print(left_text)
        print(right_text)

    def test_task_two(self):
        self.open_url(base_url + "dynamic_loading/1")
        self.click_start()
        self.check_loader_is_displayed_and_then_disappear()
        finish_text = self.get_finish_text()
        print(finish_text)

    def test_task_three(self):
        """The problem is in the incorrect range start. Actual 1, but expected 0. The correct method is below"""
        a_list = [1, 2, 3, 5, 7, 9]
        for i in range(0, len(a_list)):
            print('Element {} = {}'.format(str(i), str(a_list[i])))

    def test_task_four(self):
        self.open_url(base_url + "challenging_dom")
        third_row_diceret_col = self.get_element_by_row_and_column(3, 6)
        delete_link_apeirian7_row = self.get_element_by_row_and_column(8, 7, delete_link=True)
        edit_link_apeirian2_row = self.get_element_by_row_and_column(3, 7, edit_link=True)
        definiebase7 = self.get_element_by_row_and_column(8, 4)
        luvaret7 = self.get_element_by_row_and_column(8, 1)
        elements = [third_row_diceret_col, delete_link_apeirian7_row, edit_link_apeirian2_row, definiebase7, luvaret7]
        for element in elements:
            self.highlight_element(element)
        self.click_green_button()
