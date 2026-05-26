#-------------------------------------------------------------------------------
#Nombre del estudiante: Gerardo Alonso Herrera de Avila
#Grupo: 213022_1022
#Pograma: Ingenieria de Telecomunicaciones
#Codigo fuente: autoria propia
#--------------------------------------------------------------------------------
#Universidad nacional abierta y a distancia-UNAD
#Fase 5 - Evaluacion final POA
#Problema 1: Evaluacion del nivel de compromiso de sesiones
#--------------------------------------------------------------------------------

def clasificar_compromiso(duracion, clics):
    """ 
    clasificar el nivel de compromiso de una sesión segun la duracion en segundos y la cantidad de eventos clics.
    """
    if duracion >180 and clics >8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"
    
def generar_informe(sesiones):
    """ 
    recorre la matriz de sesiones y presenta el informe final con el ID del cliente y su clasificacion de copmromiso.
    """
    print("INFORME DE NIVEL DE COMPROMISO DE CLIENTES")
    print("_"*60)
    print("ID Cliente\tDuracion\tClics\tClasificacion")                                                              
    print("-"*60)

    for sesion in sesiones:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]

        clasificacion = clasificar_compromiso(duracion, clics)
        print(f"{id_cliente:<15}\t\t{duracion:<15}s\t\t{clics:<10}\t{clasificacion}")

def main():
    """ 
    funcion principal del programa. define la matriz inicial con los datos de las sesiones de clientes y genera el informe.
    """
    sesiones = [
        ("C001", 200,12),
        ("C002",45, 5),
        ("C003", 150,7),
        ("C004", 300,10),
        ("C005",80,2),
        ("C006", 190,6)
     ]
    
    generar_informe(sesiones)

main()
