from selenium.webdriver.common.by import By


# class RegisterPageLocators:


class LoginPageLocators:
    LOGIN_EMAIL = (By.XPATH, '/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]')
    LOGIN_PASSWORD = (By.XPATH, '/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/input[1]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-button')


#class ActualsPageLocators:

class ProjectsPageLocators:
    CREATE_PROJECT_BTN = (By.XPATH, "//body/div[@id='root']/div[2]/div[1]/div[2]/div[2]/div[1]/button[1]/p[1]/div[1]")
    PROJECT_NAME = (By.XPATH, "//input[@id='projectName']")
    PROJECT_SHORT_NAME = (By.XPATH, "//input[@id='projectShortName']")
    CLIENT = (By.XPATH, '//*[@id="tags-outlined"]/div')
    SELECT_CLIENT = (By.ID, 'react-select-3-option-0')
    ESTIMATED_HOURS = (By.XPATH, "//input[@id='estimated']")
    STATUS = (By.XPATH, "//div[4]/div/p[2]/div/div/div")
    SELECT_STATUS = (By.XPATH, '//*[text()="Done"]')
    BILLABLE = (By.XPATH, "//div[@id='selectBillable']")
    MANAGER = (By.XPATH, "//div[3]/div[2]/p[2]/div/div/div")
    SELECT_MANAGER = (By.XPATH, "//div[@id='react-select-5-option-1']")
    BUSINESS_UNIT = (By.XPATH, '//div[4]/div[2]/p[2]/div/div/div/input')
    CHECK_BOX_DEFINE_START_END = (By.XPATH, '//span/input')
    START_DATE_FIELD = (By.XPATH, "//body/div[4]/div[3]/div[1]/div[1]/div[2]/div[6]/div[1]/p[2]/div[1]/div[1]/input[1]")
    END_DATE_FIELD = (By.XPATH, '//body/div[4]/div[3]/div[1]/div[1]/div[2]/div[6]/div[1]/p[2]/div[1]/div[1]/input[1]')
    NOTES_FIELD = (By.CSS_SELECTOR, ".public-DraftEditor-content")
    PROJECT_COLOR = (By.CSS_SELECTOR, '.project-form__project-color')
    SELECT_PROJECT_COLOR = (By.CSS_SELECTOR, 'span:nth-child(8) > div div')
    CREATE_BTN = (By.XPATH, "//button[@id='createProject']")
    CANCEL_BTN = (By.XPATH, '//body/div[4]/div[3]/div[1]/div[2]/button[2]')
    SELECT_PROJECT = (By.CSS_SELECTOR, "#selectProject")
    SEARCH_FIELD = (By.ID, "filterProjects")
    ARCHIVE_PROJECT_ICON = (By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/img[1]")
    ARCHIVE_PROJECT_BTN = (By.XPATH, "//body/div[4]/div[3]/div[1]/div[2]/button[1]")
    FILTER_PROJECTS_BY_ACTIVITY = (By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[1]/div[2]/div/div/div[1]')
    SELECT_ARCHIVE_PROJECTS = (By.XPATH, '//div[text()="Archived"]')
    SELECT_ARCHIVE_PROJECT = (By.ID, 'selectProject')
    SELECT_ARCHIVED_PROJECT_BOX = (By.XPATH, "//input[@id='selectProject']")
    DELETE_PROJECT_ICON = (By.XPATH, '//*[@id="root"]/div[2]/div/div[3]/img[1]')
    CONFIRM_DELETE_PROJECT_BTN = (By.XPATH, '//p[text()="Delete"]')
    ACTIVATE_PROJECT_ICON = (By.XPATH, "//img[@id='activateProject']")
    REACTIVATE_PROJECT_BTN = (By.XPATH, "//p[contains(text(),'Reactivate Project')]")
    MANAGE_CLIENTS_BTN = (By.XPATH, "//body/div[@id='root']/div[2]/div[1]/div[2]/div[2]/button[2]")
    CREATE_CLIENT_BTN = (By.XPATH, "//img[@id='createClient']")
    CLIENT_NAME_FIELD = (By.XPATH, "//input[@id='nameClient']")
    CLIENT_EMAIL_FIELD = (By.XPATH, "//input[@id='emailClient']")
    CLIENT_PHONE_FIELD = (By.XPATH, "//input[@id='phoneNumberClient']")
    CLIENT_SAVE_BTN = (By.XPATH, "//img[@id='saveClient']")







# class UsersPageLocators:

# class PlanningPageLocators:
