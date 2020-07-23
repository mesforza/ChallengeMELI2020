import unittest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from pageIndex import PageIndex
from pageItems import PageItems
from pageItem import PageItem


class SearchCases(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument("start-maximized")
        option.add_argument("incognito")
        # option.add_argument("--headless")
        self.driver = webdriver.Chrome("drivers\chromedriver.exe", chrome_options=option)
        self.driver.get("https://www.mercadolibre.com/")
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)
        self.itemPage = PageItem(self.driver)

    #@unittest.skip("Not needed now")
    def test_search_product(self):
        self.indexPage.select_nationality_site()
        self.indexPage.nav_search_input('iPhone 11 Pro')
        self.indexPage.nav_search_button()

        #self.itemsPage.items_page_mayor_precio()

        try:
            self.itemsPage.items_11pro()
            self.itemsPage.items_11pro_capacidad()
            self.itemsPage.items_price_from('300000')
            self.itemsPage.items_to_price('340000')
            self.itemsPage.items_button_price()
            self.itemsPage.items_search_results()
        except:
            self.driver.save_screenshot('error_itemsPage.jpg')

        try:
            self.itemPage.item_capacidad_256gb()
            #self.itemPage.item_image_2nd()
            #self.itemPage.item_color_oro()
            self.assertEqual(self.itemPage.item_assert_text_liberado(), 'Liberado.')
            self.itemPage.item_comprar_ahora()
            time.sleep(2)
        except:
            self.driver.save_screenshot('error_itemPage.jpg')

    #@unittest.skip("Not needed now")
    def test_nav_categorias_tecnologia_celulares(self):
        try:
            self.indexPage.select_nationality_site()
            self.indexPage.nav_categ()
            self.indexPage.nav_tecno()
            self.indexPage.nav_para_playstation()
            self.itemsPage.items_price_from('10000')
            self.itemsPage.items_to_price('40000')
            self.itemsPage.items_button_price()
            self.itemsPage.items_tienda_oficiales()
            self.itemsPage.items_play_station_4()
            self.itemsPage.items_tienda_oficial_Thrustmaster()
            self.assertEqual(self.itemsPage.items_assert_tienda_oficial_Thrustmaster(),'Thrustmaster Tienda oficial')
            time.sleep(2)
        except:
            self.driver.save_screenshot('error_tecnologia_tienda_oficial_thrustmaster.jpg')









