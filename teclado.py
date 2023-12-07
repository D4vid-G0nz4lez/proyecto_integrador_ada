# Importando libreria readkey y key 
from readchar import readkey, key 
# Pedirr al jugador que precione una tecla 
# Indicar con que tecla se detiene el bucle 

print(input("Ingrese una tecla, si desea detener el programa oprima la tecla flecha arriba "))

while True:
    k = readkey()

    if k == key.UP:
        print( "Haz precinado flecha arriba para detener")
        break
    else:
        print(f"Presionaste (k)")

     
print("--------------------------------------------------")

import os

number = 0

while True:
    os.system('cls' if os.name=='nt' else 'clear')
    print(number)

    key = input()

    if key == 'n':
        number += 1
    if number == 50:
        break     
