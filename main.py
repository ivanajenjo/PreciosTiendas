import instantGaming
import g2a
import kinguin
import threading

print("Que juego quiere buscar ?")
juego = input()
#instantGaming.buscarInstant(juego)
#g2a.buscarG2A(juego)
#kinguin.buscarKinguin(juego)
hilos = list()
hilo1 = threading.Thread(target=instantGaming.buscarInstant(juego))
hilos.append(hilo1)
hilo2 = threading.Thread(target=kinguin.buscarKinguin(juego))
hilos.append(hilo2)
hilos.start()