from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PageItems():

    def __init__(self, my_driver):
        self.driver = my_driver
        #self.mayor_precio = (By.XPATH, '//span[contains(@class, "ui-list__item-option")]')  #//div[contains(@class,"sort-by")]//li[2]//a
        self.modelo11pro = (By.XPATH, '//dl[@id="id_MODEL"]/dd[2]/a[1]/span[1]')
        self.capacidad_11pro = (By.XPATH, '//span[contains(text(),"256 a 511 GB")]')
        self.price_from = 'fromPrice'
        self.price_from_wait = (By.ID, 'fromPrice')
        self.to_price = 'toPrice'
        self.button_price = (By.XPATH, '//button[contains(@tabindex,"95")]')
        self.search_result_1st = (By.XPATH, '//ol[@id="searchResults"]/li[1]/div[1]/div[1]/div[1]')
        self.tiendas_oficiales = (By.XPATH, '//a[contains(@title, "Solo tiendas oficiales")]')
        self.play_station_4 = (By.XPATH, '//a[contains(@title, "PS4 - PlayStation 4")]')
        self.tienda_oficial_Thrustmaster = (By.XPATH, '//a[contains(@aria-label, "Thrustmaster")]')
        self.assert_text_thrustmaster = '//h1[contains(text(),"Thrustmaster Tienda oficial")]'



        #def items_page_mayor_precio(self):
     #   mayor_precio2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.mayor_precio))
      #  mayor_precio2.click()

    def items_11pro(self):
        modelo11pro2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.modelo11pro))
        modelo11pro2.click()

    def items_11pro_capacidad(self):
        capacidad_11pro2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.capacidad_11pro))
        capacidad_11pro2.click()

    def items_price_from(self, item):
        price_from2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.price_from_wait))
        self.driver.find_element_by_id(self.price_from).send_keys(item)

    def items_to_price(self, item):
        self.driver.find_element_by_id(self.to_price).send_keys(item)

    def items_button_price(self):
        button_price2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.button_price))
        button_price2.click()

    def items_search_results(self):
        search_results2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.search_result_1st))
        search_results2.click()

    def items_tienda_oficiales(self):
        solo_tiendas_oficiales2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.tiendas_oficiales))
        solo_tiendas_oficiales2.click()

    def items_play_station_4(self):
        play_station_4 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.play_station_4))
        play_station_4.click()

    def items_tienda_oficial_Thrustmaster(self):
        tienda_oficial_Thrustmaster2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.tienda_oficial_Thrustmaster))
        tienda_oficial_Thrustmaster2.click()

    def items_assert_tienda_oficial_Thrustmaster(self):
        return self.driver.find_element_by_xpath(self.assert_text_thrustmaster).text

