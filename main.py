import instantGaming
import g2a
import kinguin
import cdkeys
import hrk


print("Que juego quiere buscar ?")
juego = input()
precioInstant = instantGaming.buscarInstant(juego)
#g2a.buscarG2A(juego)
precioKinguin = kinguin.buscarKinguin(juego)