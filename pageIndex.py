from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select



class PageIndex():

    def __init__(self, my_driver):
        self.select_site = (By.ID, 'AR')
        self.driver = my_driver
        self.input_search = 'nav-search-input'
        self.search_button = (By.CLASS_NAME, 'nav-search-btn')
        self.categorias = (By.CLASS_NAME, 'nav-menu-categories-link')
        self.tecno = '//a[contains(text(),"Tecnología")]'
        self.tecno2 = (By.XPATH, '//a[contains(text(),"Tecnología")]')
        self.para_playstation = (By.XPATH, '//a[contains(text(),"Para PlayStation")]')
        self.geek = (By.XPATH, '//button[@class="ui-dropdown__link"]')
        self.de_fiesta = '//button[contains(text(),"De fiesta")]'



    def select_nationality_site(self):
        select_site2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.select_site))
        select_site2.click()

    def nav_search_input(self, item):
        self.driver.find_element_by_class_name(self.input_search).send_keys(item)

    def nav_search_button(self):
        search_button2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.search_button))
        search_button2.click()

    def nav_categ(self):
        categorias2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.categorias))
        action = ActionChains(self.driver)
        categorias3 = self.driver.find_element_by_class_name("nav-menu-categories-link")
        action.move_to_element(categorias3).perform()

    def nav_tecno(self):
        tecno2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.tecno2))
        action = ActionChains(self.driver)
        tecno3 = self.driver.find_element_by_xpath(self.tecno)
        action.move_to_element(tecno3).perform()

    def nav_para_playstation(self):
        para_playstation2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.para_playstation))
        para_playstation2.click()
        #action = ActionChains(self.driver)
        #para_playstation3 = self.driver.find_element_by_xpath(self.para_playstation)
        #action.move_to_element(para_playstation3).perform()

    def colecciones_geek(self):
        geek = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.geek))
        geek.click()

    def colecciones_de_fiesta(self, text):
        de_fiesta = self.driver.find_element_by_xpath(self.de_fiesta)
        de_fiesta.click()


