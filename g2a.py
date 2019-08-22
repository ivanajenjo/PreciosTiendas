from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def buscarG2A(juego):
    navegador = webdriver.Chrome("driver/chromedriver.exe")
    #navegador.minimize_window()
    navegador.get("https://www.g2a.com/")
    try:
        elem = navegadir.find_element_by_class_name("close")
        elem.click()
    except:
        print("La jodiste")
    elem = navegador.find_element_by_class_name("button button--size-large button--type-transparent")
    elem.click()
    elem = navegador.find_element_by_name("query")
    elem.clear()
    elem.send_keys(juego)
    elem.send_keys(Keys.RETURN)
    elem = navegador.find_element_by_class_name("Card__price-cost price")
    precio = elem.text
    print("Precio en G2A de ", juego, " es ", elem.text)
    navegador.close()
    return precio

buscarG2A("GTAV")