from selenium import webdriver
from selenium.webdriver.common.keys import Keys
nombreTienda = "HRK"

def buscarHrk(juego):
    navegador = webdriver.Chrome("driver/chromedriver.exe")
    ##navegador.minimize_window()
    navegador.get("https://www.hrkgame.com/es/")
    elem = navegador.find_element_by_name("ui black deny button")
    elem.click()
    elem = navegador.find_element_by_name("search")
    elem.clear()
    elem.send_keys(juego)
    elem.send_keys(Keys.RETURN)
    precio = navegador.find_element_by_class_name("price")
    print("Precio en", nombreTienda,"de", juego, "es", precio.text)
    #navegador.close()

buscarHrk("GTAV")