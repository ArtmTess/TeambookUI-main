import time
from utils.login import login
from pages.projects_page import ProjectsPage
from pages.settings import url_projects_page


def test_create_project(browser):
    """ Function for create project with required fields"""
    login(browser)
    time.sleep(3)
    link = url_projects_page
    page = ProjectsPage(browser, link)
    page.open()
    page.click_create_project_btn()
    page.fill_project_name_req()
    page.fill_project_short_name_req()
    page.click_create_button()


def test_create_full_project(browser):
    """ Function for create project with all fields"""
    login(browser)
    time.sleep(3)
    link = url_projects_page
    page = ProjectsPage(browser, link)
    page.open()
    page.click_create_project_btn()
    page.fill_project_name()
    page.fill_project_short_name()
    page.click_client_field()
    page.click_billable_project()
    page.fill_estimated_hours()
    page.select_manager()
    page.select_status()
    page.fill_business_unit()
    page.click_define_start_end_dates_checkbox()
    page.select_project_color()
    page.click_create_button()


def test_archive_project(browser):
    """ Function for archive project """
    login(browser)
    time.sleep(3)
    link = url_projects_page
    page = ProjectsPage(browser, link)
    page.open()
    page.fill_project_search_field('Test_Project_N1')
    time.sleep(1)
    page.select_project()
    page.archive_project()


def test_delete_project(browser):
    """ Function for delete project """
    login(browser)
    time.sleep(3)
    link = url_projects_page
    page = ProjectsPage(browser, link)
    page.open()
    page.filter_project_by_activity()
    page.click_archive_project()
    page.fill_project_search_field('Test1')
    page.select_archived_project_checkbox()
    page.click_delete_project_icon()
    page.click_delete_project_btn()


def test_create_client(browser):
    """ Function for activate project """
    login(browser)
    time.sleep(3)
    link = url_projects_page
    page = ProjectsPage(browser, link)
    page.open()
    page.click_manage_clients_btn()
    page.create_clients_btn()
    page.fill_new_client()
    page.save_clients_icon()


#@pytest.mark.xfail(reason='Not able to Activate project. Fixed Feb 28 2022')
def test_activate_project(browser):
    """ Function for activate project """
    login(browser)
    time.sleep(3)
    link = url_projects_page
    page = ProjectsPage(browser, link)
    page.open()
    page.filter_project_by_activity()
    page.click_archive_project()
    page.fill_project_search_field('Test_Project5')
    page.select_archived_project_checkbox()
    page.click_activate_project_icon()
    page.reactivate_project_btn()













