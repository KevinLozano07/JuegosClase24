from random import randint

x = ""

while x=="" or x==" ":
 
 opciones = ["Piedra", "Papel", "Tijera"]

 Decision = randint(0, 2)

 Jugada_pc = opciones[Decision]

 print("")
 Jugada_player = input("Elija (Pieda,Papel o Tijera): ").lower()

 if Jugada_player == Jugada_pc.lower():
    print(f"El computador elijio: {Jugada_pc}")
    print("")
    print("Empate")
    print("")
 elif Jugada_player == "Papel" or Jugada_player == "papel":
    if Jugada_pc == "Tijera":    
        print("")
        print(f"El computador elijio: {Jugada_pc}")
        print(f"{Jugada_pc} > {Jugada_player}")
        print("")
        print("Perdiste")
        print("")
    else:
        print("")
        print(f"El computador elijio: {Jugada_pc}")
        print(f"{Jugada_player} > {Jugada_pc}")
        print("")
        print("Ganaste")
        print("")
 elif Jugada_player == "Tijera" or Jugada_player == "tijera":
    if Jugada_pc == "Piedra":
        print("")
        print(f"El computador elijio: {Jugada_pc}")
        print(f"{Jugada_pc} > {Jugada_player}")
        print("")
        print("Perdiste")
        print("")
    else:
        print("")
        print(f"El computador elijio: {Jugada_pc}")
        print(f"{Jugada_player} > {Jugada_pc}")
        print("")
        print("Ganaste")
        print("")
 elif Jugada_player == "Piedra" or Jugada_player == "piedra":
    if Jugada_pc == "Papel":
        print("")
        print(f"El computador elijio: {Jugada_pc}")
        print(f"{Jugada_pc} > {Jugada_player}")
        print("")
        print("Perdiste")
        print("")
    else:
        print("")
        print(f"El computador elijio: {Jugada_pc}")
        print(f"{Jugada_player} > {Jugada_pc}")
        print("")
        print("Ganaste")
        print("")
 else:
    print("")
    print("Palabra no admitida")
    print("")
   
 x = str(input("(¿Desea volera a jugar? presione Enter / ¿Desea salir del juego? ingrese un valor) ")) 
 print("")
 print("#" * 100)