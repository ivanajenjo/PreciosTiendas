from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def buscarG2A(juego):
    navegador = webdriver.Chrome("driver/chromedriver.exe")
    #navegador.minimize_window()
    navegador.get("https://www.g2a.com/")
    elem = navegador.find_element_by_class_name("btn btn-primary")
    elem.click()
    elem = navegador.find_element_by_name("query")
    elem.clear()
    elem.send_keys(juego)
    elem.send_keys(Keys.RETURN)
    elem = navegador.find_element_by_class_name("Card__price-cost price")
    print("Precio en G2A de ", juego, " es ", elem.text)
    navegador.close()

#buscarG2A("GTAV")