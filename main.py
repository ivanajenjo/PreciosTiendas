import instantGaming
import g2a
import kinguin
import cdkeys
import hrk


print("Que juego quiere buscar ?")
juego = input()
precioInstant = instantGaming.buscarInstant(juego)
precioG2a = g2a.buscarG2A(juego)
precioKinguin = kinguin.buscarKinguin(juego)
precioHrk = hrk.buscarHrk(juego)
precioCdkeys = cdkeys.buscarCDKeys(juego)

preciosTotal = [precioInstant,precioCdkeys,precioG2a,precioHrk,precioKinguin]