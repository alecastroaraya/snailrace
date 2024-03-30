def tablero_juego():
    """Esta funcion define las variables string usadas para formar el tablero de la carrera.
    - Entrada: Input del usuario.
    - Salida: El tablero inicial.
    - Restricciones: El usuario debe presionar Enter para avanzar.
    """
    
    global caracol_1
    global caracol_2
    global num_tablero
    global cuenta_tablero
    global conteo_caracol_1
    global conteo_caracol_2
    global caracoles
    
    import random
    num_tablero = 1
    linea_meta = "------------META"
    caracol_1 = "@..1"
    caracol_2 = "@..2"
    caracoles = [caracol_1,caracol_2]
    conteo_caracol_1 = 0
    conteo_caracol_2 = 0
    
    cuenta_tablero = "Tablero "+str(num_tablero)
    print("Tablero 0\n" + caracol_1,"\n" + linea_meta,"\n" + caracol_2,"\n")
    respuesta = input("Presione ENTER para continuar la carrera.\n")
    
    
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
        
        cuenta_tablero = "Tablero "+str(num_tablero)
        casilla = " "
        casillas_avanzadas = casilla*numero_casillas_escogido
        
        
        if caracol_escogido == caracol_1:
            conteo_caracol_1 = conteo_caracol_1 + numero_casillas_escogido
            caracol_1 = casillas_avanzadas + caracol_1
            caracoles = [caracol_1,caracol_2]
            num_tablero = num_tablero + 1
            print(cuenta_tablero,"\n" + caracol_1,"\n" + linea_meta,"\n" + caracol_2,"\n")
            if conteo_caracol_1 >= 12:
                print("Felicidades! El caracol #1 ha ganado la carrera!\nVolviendo al menu principal...")
                return menu_juego()
            respuesta = input("Presione ENTER para continuar la carrera.\n")
            nuevo_tablero = carrera_caracoles(random.choice(caracoles),random.randint(0,3))
            
        elif caracol_escogido == caracol_2:
            conteo_caracol_2 = conteo_caracol_2 + numero_casillas_escogido
            caracol_2 = casillas_avanzadas + caracol_2
            caracoles = [caracol_1,caracol_2]
            num_tablero = num_tablero + 1
            print(cuenta_tablero,"\n" + caracol_1,"\n" + linea_meta,"\n" + caracol_2,"\n")
            if conteo_caracol_2 >= 12:
                print("Felicidades! El caracol #2 ha ganado la carrera!\nVolviendo al menu principal...")
                return menu_juego()
            respuesta = input("Presione ENTER para continuar la carrera.\n")
            nuevo_tablero = carrera_caracoles(random.choice(caracoles),random.randint(0,3))
            
        else:
            carrera_caracoles_aux(random.choice(caracoles),random.randint(0,3))
            
    carrera_caracoles(random.choice(caracoles),random.randint(0,3))

def menu_juego():
    """Muestra el menu principal del juego, y da una diferente salida dependiendo de la opcion escogida.
    - Entrada: Input que sea 1, 2 o 3
    - Salida: Muestra el menu principal, y luego o muestra las instrucciones, o empieza el juego, o termina el programa.
    - Restricciones: La entrada debe ser 1, 2, o 3.
    """
        
    print(""" 
                                                                                                                                                                                            
 ,-----.                                                   ,--.                                                     ,--.                                                                    
'  .--./ ,--,--.,--.--.,--.--. ,---. ,--.--. ,--,--.     ,-|  | ,---.      ,---. ,--,--.,--.--. ,--,--. ,---. ,---. |  | ,---.  ,---.                                                       
|  |    ' ,-.  ||  .--'|  .--'| .-. :|  .--'' ,-.  |    ' .-. || .-. :    | .--'' ,-.  ||  .--'' ,-.  || .--'| .-. ||  || .-. :(  .-'                                                       
'  '--'\\ '-'  ||  |   |  |   \   --.|  |   \ '-'  |    \ `-' |\   --.    \ `--.\ '-'  ||  |   \ '-'  |\ `--.' '-' '|  |\   --..-'  `)                                                      
 `-----' `--`--'`--'   `--'    `----'`--'    `--`--'     `---'  `----'     `---' `--`--'`--'    `--`--' `---' `---' `--' `----'`----'                                                     
""")
    print("\n")
    
    respuesta = input("Bienvenido!\nEscriba el numero de la opcion que quiere:\n\n1.Mostrar las intstrucciones\n2.Jugar\n3.Salir del juego\n")
        
        
    if respuesta == "1":
        print("""\nEste juego consiste en una carrera de caracoles que compiten para llegar a la meta. 
Cada correra consta de dos caracoles en carriles paralelos, y cada uno tiene 12 casillas para recorrer. 
El primer caracol en llegar a la meta gana.""")
        print("\nVolviendo al menu principal...")
        menu_juego()
    
    elif respuesta == "2":
        tablero_juego()
    
    elif respuesta == "3":
        print("\nSaliendo del juego...")
        raise SystemExit
    
    elif respuesta != "1" or respuesta != "2" or respuesta != "3":
        print("Error 01: Por favor escoja una de las tres opciones.")
        menu_juego()
    
def iniciar_juego():
    menu_juego()

iniciar_juego()
