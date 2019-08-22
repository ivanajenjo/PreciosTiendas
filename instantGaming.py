from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def buscarInstant(juego):
    navegador = webdriver.Chrome("driver/chromedriver.exe")
    navegador.minimize_window()
    navegador.get("https://www.instant-gaming.com/es/")
    elem = navegador.find_element_by_name("q")
    elem.clear()
    elem.send_keys(juego)
    elem.send_keys(Keys.RETURN)
    elem = navegador.find_element_by_class_name("price")
    precio = elem.text
    print("Precio en Instant Gaming de ", juego, " es ", elem.text)
    navegador.close()
    return precio