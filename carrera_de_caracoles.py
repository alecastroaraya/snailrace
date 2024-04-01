import os
import pyfiglet

global language
language = "english"

def tablero_juego():
    """Esta funcion define las variables string usadas para formar el tablero de la carrera.
    - Entrada: Input del usuario.
    - Salida: El tablero inicial.
    - Restricciones: El usuario debe presionar Enter para avanzar.
    """

    global language
    global caracol_1
    global caracol_2
    global num_tablero
    global cuenta_tablero
    global conteo_caracol_1
    global conteo_caracol_2
    global caracoles
    
    import random
    num_tablero = 1

    match language:
        case "english":
            linea_meta = "----------------------------------------------------------------------------GOAL"
        case "spanish":
            linea_meta = "----------------------------------------------------------------------------META"
        case "french":
            linea_meta = "----------------------------------------------------------------------------BUT"

    caracol_1 = "@..1"
    caracol_2 = "@..2"
    caracoles = [caracol_1,caracol_2]
    conteo_caracol_1 = 0
    conteo_caracol_2 = 0

    match language:
        case "english":
            cuenta_tablero = "Iteration "+str(num_tablero)
        case "spanish":
            cuenta_tablero = "Iteración "+str(num_tablero)
        case "french":
            cuenta_tablero = "Iteration "+str(num_tablero)

    print(cuenta_tablero+"\n" + caracol_1,"\n" + linea_meta,"\n" + caracol_2,"\n")
    match language:
        case "english":
            respuesta = input("Press ENTER to continue the race.\n")
        case "spanish":
            respuesta = input("Presione ENTER para continuar la carrera.\n")
        case "french":
            respuesta = input("Appuyez sur ENTER pour continuer la course.\n")
    
    def carrera_caracoles(caracol_escogido,numero_casillas_escogido):
        """ Esta funcion avanza la carrera de caracoles hasta que uno de los dos haya llegado a la meta.
        - Entrada: Un caracol escogido al azar y un numero entero de casillas que moverse escogido al azar.
        - Salida: El tablero actualizado con el movimiento de los caracoles.
        - Restricciones: El caracol escogido debe ser un string, el numero escogido debe ser un numero entero del 0 al 3.
        """
        
        if type(caracol_escogido) != str:

            print("Error 01: El caracol escogido no es un string.")
            return
        
        if type(numero_casillas_escogido) != int:
            print("Error 02: El numero de casillas escogido no es un entero.")
            return
        
        else:
            carrera_caracoles_aux(random.choice(caracoles),random.randint(0,3))
        
    def carrera_caracoles_aux(caracol_escogido,numero_casillas_escogido):
        """ Esta funcion avanza la carrera de caracoles hasta que uno de los dos haya llegado a la meta.
        - Entrada: Un caracol escogido al azar y un numero entero de casillas que moverse escogido al azar.
        - Salida: El tablero actualizado con el movimiento de los caracoles.
        - Restricciones: El caracol escogido debe ser un string, el numero escogido debe ser un numero entero del 0 al 3.
        """
        
        global caracol_1
        global caracol_2
        global num_tablero
        global cuenta_tablero
        global conteo_caracol_1
        global conteo_caracol_2
        global caracoles

        match language:
            case "english":
                cuenta_tablero = "Iteration "+str(num_tablero)
            case "spanish":
                cuenta_tablero = "Iteración "+str(num_tablero)
            case "french":
                cuenta_tablero = "Iteration "+str(num_tablero)
        casilla = " "
        casillas_avanzadas = casilla*numero_casillas_escogido

        if caracol_escogido == caracol_1:
            conteo_caracol_1 = conteo_caracol_1 + numero_casillas_escogido
            caracol_1 = casillas_avanzadas + caracol_1
            caracoles = [caracol_1,caracol_2]
            num_tablero = num_tablero + 1
            print("\n",cuenta_tablero,"\n" + caracol_1,"\n" + linea_meta,"\n" + caracol_2,"\n")
            if conteo_caracol_1 >= 72:
                match language:
                    case "english":
                        input("\nCONGRATULATIONS!!! Snail #1 won the race and is officially the fastest snail on the planet!!!\nWinner: Snail #1\n\nPress ENTER to return to the main menu!\n")
                    case "spanish":
                        input("\nFELICIDADES!!! El caracol #1 ha ganado la carrera y es oficialmente el caracol mas veloz del planeta!!!\nGanador: Caracol #1\n\nPresione ENTER para volver al menu principal!\n")
                    case "french":
                        input("\nFELICITATIONS!!! L'escargot #1 a gagné la course et c'est officiellement l'escargot le plus rapide du monde!!!\nVainqueur: Escargot #1\n\nAppuyez sur ENTER pour revenir au menu principal!\n")

                return menu_juego()

            match language:
                case "english":
                    respuesta = input("Press ENTER to continue the race.\n")
                case "spanish":
                    respuesta = input("Presione ENTER para continuar la carrera.\n")
                case "french":
                    respuesta = input("Appuyez sur ENTER pour continuer la course.\n")

            nuevo_tablero = carrera_caracoles(random.choice(caracoles),random.randint(0,3))

        elif caracol_escogido == caracol_2:
            conteo_caracol_2 = conteo_caracol_2 + numero_casillas_escogido
            caracol_2 = casillas_avanzadas + caracol_2
            caracoles = [caracol_1,caracol_2]
            num_tablero = num_tablero + 1
            print(cuenta_tablero,"\n" + caracol_1,"\n" + linea_meta,"\n" + caracol_2,"\n")
            if conteo_caracol_2 >= 72:
                match language:
                    case "english":
                        input("\nCONGRATULATIONS!!! A WINNER IS YOU!!! Snail #2 won the race and is officially the fastest snail on the planet!!!\nWinner: Snail #2\n\nPress ENTER to return to the main menu!\n")
                    case "spanish":
                        input("\nFELICIDADES!!! El caracol #2 ha ganado la carrera y es oficialmente el caracol mas veloz del planeta!!!\nGanador: Caracol #2\n\nPresione ENTER para volver al menu principal!\n")
                    case "french":
                        input("\nFELICITATIONS!!! L'escargot #2 a gagné la course et c'est officiellement l'escargot le plus rapide du monde!!!\nVainqueur: Escargot #2\n\nAppuyez sur ENTER pour revenir au menu principal!\n")
                return menu_juego()

            match language:
                case "english":
                    respuesta = input("Press ENTER to continue the race.\n")
                case "spanish":
                    respuesta = input("Presione ENTER para continuar la carrera.\n")
                case "french":
                    respuesta = input("Appuyez sur ENTER pour continuer la course.\n")

            nuevo_tablero = carrera_caracoles(random.choice(caracoles),random.randint(0,3))

        else:
            carrera_caracoles_aux(random.choice(caracoles),random.randint(0,3))

    carrera_caracoles(random.choice(caracoles),random.randint(0,3))

def limpiar_pantalla():
    """Limpia la pantalla de la terminal
    - Entrada: Ninguna
    - Salida: Limpia la pantalla
    - Restricciones: Ninguna
    """

    match os.name:
        case "posix":
            os.system('clear')
        case "nt":
            os.system("cls")
        case _:
            print('\n' * 100)

def menu_juego():
    """Muestra el menu principal del juego, y da una diferente salida dependiendo de la opcion escogida.
    - Entrada: Input que sea 1, 2 o 3
    - Salida: Muestra el menu principal, y luego o muestra las instrucciones, o empieza el juego, o termina el programa.
    - Restricciones: La entrada debe ser 1, 2, o 3.
    """

    global language
    limpiar_pantalla()
    logo_juego = pyfiglet.figlet_format("SnailRace", font="banner")
    print(logo_juego)
    print("\n")

    match language:
        case "english":
            respuesta = input("Welcome to SnailRace, the most epic snail race in the planet!\nInput an option:\n\n1.Instructions\n2.New game\n3.Switch language\n4.Exit\n\n")
        case "french":
            respuesta = input("Bienvenue à SnailRace, la course d'escargots la plus epique au monde !\nVeuillez choisir une option:\n\n1.Instructions\n2.Nouvelle partie\n3.Changer la langue\n4.Sortir\n\n")
        case "spanish":
            respuesta = input("Bienvenido a SnailRace, la carrera de caracoles mas epica del planeta!\nEscriba el numero de la opcion que quiere:\n\n1.Instrucciones\n2.Nueva partida\n3.Cambiar lenguaje\n4.Salir del juego\n\n")

    if respuesta == "1":
        limpiar_pantalla()

        match language:
            case "english":
                print("""\nIn this game, two snails race to get to the finish line. 
Each race consists of two snails running in parallel, and each one must traverse 72 fields. 
The first snail to get to the finish line wins.\n""")
                input("Press ENTER to return to the main menu.\n")
                print("\nReturning to main menu...")
            case "spanish":
                print("""\nEste juego consiste en una carrera de caracoles que compiten para llegar a la meta. 
Cada carrera consta de dos caracoles en carriles paralelos, y cada uno tiene 72 casillas para recorrer. 
El primer caracol en llegar a la meta gana.\n""")
                input("Presione ENTER para volver al menu principal.\n")
                print("\nVolviendo al menu principal...")
            case "french":
                print("""\nDans ce jeu, deux escargots s'affrontent dans une course epique. 
Chaque escargot doit traverser 72 champs en total pour pouvoir gagner la course.
L'escargot qui finit en premier gagnera la course.\n""")
                input("Appuyez sur ENTER pour revenir au menu principal.\n")
                print("\nRetour au menu principal en cours...")
        menu_juego()
    
    elif respuesta == "2":
        print("\n")
        tablero_juego()
    
    elif respuesta == "3":
        limpiar_pantalla()

        match language:
            case "english":
                language = "spanish"
            case "spanish":
                language = "french"
            case "french":
                language = "english"

        menu_juego()

    elif respuesta == "4":
        match language:
            case "english":
                print("\nExiting the game...")
            case "spanish":
                print("\nSaliendo del juego...")
            case "french":
                print("\nSortie en cours...")

        raise SystemExit
    
    elif respuesta != "1" or respuesta != "2" or respuesta != "3" or respuesta != "4":
        match language:
            case "english":
                print("\nError 01: Please pick a valid option.\n")
            case "spanish":
                print("\nError 01: Por favor escoja una opción valida.\n")
            case "french":
                print("\nError 01: Veuillez choisir une option valide.\n")

        menu_juego()
    
def iniciar_juego():
    menu_juego()

iniciar_juego()
