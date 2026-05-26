# Nombre del estudiante: Gerardo Alonso Herrera de Avila
# Grupo: 213022_1022
# Programa: Ingenieria de Telecomunicaciones
# Codigo fuente: autoria propia
# ------------------------------------------------------------
# Universidad Nacional Abierta y a Distancia - UNAD
# Curso: Fundamentos de Programación
# Fase 5 - Evaluación Final POA
# Problema 1: Evaluación del nivel de compromiso de sesiones
# ------------------------------------------------------------

def clasificar_compromiso(duracion, clics):
    """
    Clasifica el nivel de compromiso de una sesión según la
    duración en segundos y la cantidad de eventos clics.
    """
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


def generar_informe(sesiones):
    """
    Recorre la matriz de sesiones y presenta el informe final
    con el ID del cliente y su clasificación de compromiso.
    """
    print("INFORME DE NIVEL DE COMPROMISO DE CLIENTES")
    print("-" * 60)
    print("ID Cliente\tDuración\tClics\tClasificación")
    print("-" * 60)

    for sesion in sesiones:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]

        clasificacion = clasificar_compromiso(duracion, clics)
        print(f"{id_cliente}\t\t{duracion}s\t\t{clics}\t{clasificacion}")


def main():
    """
    Función principal del programa. Define la matriz inicial con
    los datos de las sesiones de clientes y genera el informe.
    """
    sesiones_clientes = [
        ["C001", 220, 12],
        ["C002", 45, 5],
        ["C003", 150, 7],
        ["C004", 300, 10],
        ["C005", 80, 2],
        ["C006", 190, 6]
    ]

    generar_informe(sesiones_clientes)


main()