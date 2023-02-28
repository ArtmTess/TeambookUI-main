import time
from selenium.webdriver.support.select import Select
from .base_page import BasePage
from .locators import ProjectsPageLocators


class ProjectsPage(BasePage):

    def click_create_project_btn(self):
        create_project_btn = self.browser.find_element(*ProjectsPageLocators.CREATE_PROJECT_BTN)
        create_project_btn.click()

    def fill_project_name_req(self):
        project_name_field = self.browser.find_element(*ProjectsPageLocators.PROJECT_NAME)
        project_name_field.send_keys("Test_Project_R1")
        time.sleep(3)

    def fill_project_short_name_req(self):
        project_short_name_field = self.browser.find_element(*ProjectsPageLocators.PROJECT_SHORT_NAME)
        project_short_name_field.send_keys("TestR1")
        time.sleep(3)

    def fill_project_name(self):
        project_name_field = self.browser.find_element(*ProjectsPageLocators.PROJECT_NAME)
        project_name_field.send_keys("Test_Project_F1")
        time.sleep(3)

    def fill_project_short_name(self):
        project_short_name_field = self.browser.find_element(*ProjectsPageLocators.PROJECT_SHORT_NAME)
        project_short_name_field.send_keys("TestF1")
        time.sleep(3)

    def click_client_field(self):
        client_field = self.browser.find_element(*ProjectsPageLocators.CLIENT)
        client_field.click()
        select_client = self.browser.find_element(*ProjectsPageLocators.SELECT_CLIENT)
        select_client.click()
        time.sleep(3)

    def click_billable_project(self):
        project_billable = self.browser.find_element(*ProjectsPageLocators.BILLABLE)
        project_billable.click()
        time.sleep(3)

    def fill_estimated_hours(self):
        estimated_hours = self.browser.find_element(*ProjectsPageLocators.ESTIMATED_HOURS)
        estimated_hours.send_keys('80')
        time.sleep(3)

    def select_status(self):
        select_status = self.browser.find_element(*ProjectsPageLocators.STATUS)
        select_status.click()
        select_status = self.browser.find_element(*ProjectsPageLocators.SELECT_STATUS)
        select_status.click()
        time.sleep(3)

    def select_manager(self):
        select_manager = self.browser.find_element(*ProjectsPageLocators.MANAGER)
        select_manager.click()
        select_manager = self.browser.find_element(*ProjectsPageLocators.SELECT_MANAGER)
        select_manager.click()
        time.sleep(3)

    def fill_business_unit(self):
        business_unit = self.browser.find_element(*ProjectsPageLocators.BUSINESS_UNIT)
        business_unit.send_keys('TEST business_unit')
        time.sleep(3)

    def click_define_start_end_dates_checkbox(self):
        start_end_dates_checkbox = self.browser.find_element(*ProjectsPageLocators.CHECK_BOX_DEFINE_START_END)
        start_end_dates_checkbox.click()
        time.sleep(3)

    def select_project_color(self):
        project_color = self.browser.find_element(*ProjectsPageLocators.PROJECT_COLOR)
        project_color.click()
        select_project_color = self.browser.find_element(*ProjectsPageLocators.SELECT_PROJECT_COLOR)
        select_project_color.click()
        time.sleep(3)

    def click_create_button(self):
        create_project_btn = self.browser.find_element(*ProjectsPageLocators.CREATE_BTN)
        create_project_btn.click()

    def select_project(self):
        select_project = self.browser.find_element(*ProjectsPageLocators.SELECT_PROJECT)
        select_project.click()

    def fill_project_search_field(self, project_name):
        project_search_field = self.browser.find_element(*ProjectsPageLocators.SEARCH_FIELD)
        project_search_field.send_keys(project_name)

    def archive_project(self):
        archive_project_checkbox = self.browser.find_element(*ProjectsPageLocators.ARCHIVE_PROJECT_ICON)
        archive_project_checkbox.click()
        archive_project_btn = self.browser.find_element(*ProjectsPageLocators.ARCHIVE_PROJECT_BTN)
        archive_project_btn.click()

    def filter_project_by_activity(self):
        filter_project_by_activity = self.browser.find_element(*ProjectsPageLocators.FILTER_PROJECTS_BY_ACTIVITY)
        filter_project_by_activity.click()
        time.sleep(3)

    def click_archive_project(self):
        select_archive_projects = self.browser.find_element(*ProjectsPageLocators.SELECT_ARCHIVE_PROJECTS)
        select_archive_projects.click()
        time.sleep(3)

    def select_archived_project_checkbox(self):
        select_archived_project_checkbox = self.browser.find_element(*ProjectsPageLocators.SELECT_ARCHIVED_PROJECT_BOX)
        select_archived_project_checkbox.click()
        time.sleep(3)

    def click_delete_project_icon(self):
        delete_archive_project_icon = self.browser.find_element(*ProjectsPageLocators.DELETE_PROJECT_ICON)
        delete_archive_project_icon.click()
        time.sleep(3)

    def click_delete_project_btn(self):
        delete_project_button = self.browser.find_element(*ProjectsPageLocators.CONFIRM_DELETE_PROJECT_BTN)
        delete_project_button.click()
        time.sleep(3)

    def click_activate_project_icon(self):
        delete_activate_project_icon = self.browser.find_element(*ProjectsPageLocators.ACTIVATE_PROJECT_ICON)
        delete_activate_project_icon.click()
        time.sleep(3)

    def reactivate_project_btn(self):
        reactivate_project = self.browser.find_element(*ProjectsPageLocators.REACTIVATE_PROJECT_BTN)
        reactivate_project.click()
        time.sleep(3)

    def click_manage_clients_btn(self):
        manage_clients_btn = self.browser.find_element(*ProjectsPageLocators.MANAGE_CLIENTS_BTN)
        manage_clients_btn.click()
        time.sleep(3)

    def create_clients_btn(self):
        create_clients_btn = self.browser.find_element(*ProjectsPageLocators.CREATE_CLIENT_BTN)
        create_clients_btn.click()
        time.sleep(3)

    def fill_new_client(self):
        fill_client_name = self.browser.find_element(*ProjectsPageLocators.CLIENT_NAME_FIELD)
        fill_client_name.send_keys('TEST Client2')
        time.sleep(2)
        fill_client_email = self.browser.find_element(*ProjectsPageLocators.CLIENT_EMAIL_FIELD)
        fill_client_email.send_keys('123test@gmail.com')
        time.sleep(2)
        fill_client_phone = self.browser.find_element(*ProjectsPageLocators.CLIENT_PHONE_FIELD)
        fill_client_phone.send_keys('1235555555')
        time.sleep(2)

    def save_clients_icon(self):
        save_clients_icon = self.browser.find_element(*ProjectsPageLocators.CLIENT_SAVE_BTN)
        save_clients_icon.click()
        time.sleep(3)







