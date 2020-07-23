from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PageItem():

    def __init__(self, my_driver):
        self.driver = my_driver
        self.capacidad_256gb = (By.XPATH, '//p[@class="ui-pdp-thumbnail__label"][contains(text(),"256 GB")]')
        self.image_2nd = (By.XPATH, '//div[@class="ui-pdp-gallery__column"]/span[5]/label[1]/div[1]/div[1]/img[1]')
        self.color_oro = (By.XPATH, 'img[contains(alt(),"Oro")]')
        self.assert_text_liberado = '//li[contains(text(),"Liberado.")]'
        self.mas_info = (By.XPATH, '//a[contains(text(),"Más información")]')
        self.comprar_ahora = (By.XPATH, '//span[@class="andes-button__content"][contains(text(),"Comprar ahora")]')

    def item_capacidad_256gb(self):
        capacidad_256gb2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.capacidad_256gb))
        capacidad_256gb2.click()

    def item_image_2nd(self):
        image_2do2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.image_2nd))
        image_2do2.click()

    def item_color_oro(self):
        color_oro2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.color_oro))
        color_oro2.click()

    def item_assert_text_liberado(self):
        return self.driver.find_element_by_xpath(self.assert_text_liberado).text

    def item_mas_info(self):
        mas_info2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.mas_info))
        mas_info2.click()

    def item_comprar_ahora(self):
        comprar_ahora2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.comprar_ahora))
        comprar_ahora2.click()