from modelo_granja import BaseDatos
from interfaz import tomar_datos, procesar_datos, entregar_datos

def main():
    bd = BaseDatos()
    while True:
        op = tomar_datos()
        r = procesar_datos(op, bd)
        if r == "salir":
            break
        entregar_datos(r)

if __name__ == "__main__":
    main()
