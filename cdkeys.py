from selenium import webdriver
from selenium.webdriver.common.keys import Keys
nombreTienda = "CDKeys"

def buscarCDKeys(juego):
    navegador = webdriver.Chrome("driver/chromedriver.exe")
    ##navegador.minimize_window()
    navegador.get("https://www.cdkeys.com/es_es/")
    elem = navegador.find_element_by_name("q")
    elem.clear()
    elem.send_keys(juego)
    elem.send_keys(Keys.RETURN)
    elem = navegador.find_element_by_class_name("actual-price")
    precio = elem.text
    print("Precio en", nombreTienda,"de", juego, "es", elem.text)
    navegador.close()
    return precio

#buscarKinguin("GTAV")