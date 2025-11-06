def tomar_datos():
    print("\n1. Crear animal")
    print("2. Listar animales")
    print("3. Registrar producción semanal")
    print("4. Consultar producción semanal")
    print("5. Consultar producción total")
    print("6. Actualizar animal")
    print("7. Eliminar animal")
    print("8. Salir")
    return input("opcion: ").strip()

def procesar_datos(op, bd):
    match op:
        case "1":
            c = input("codigo: ").strip()
            r = input("raza: ").strip()
            e = int(input("edad: "))
            return bd.crear(c, r, e)
        case "2":
            return bd.listar()
        case "3":
            c = input("codigo: ").strip()
            s = int(input("semana: "))
            h = int(input("huevos: "))
            return bd.reg_prod(c, s, h)
        case "4":
            c = input("codigo: ").strip()
            s = int(input("semana: "))
            return f"{bd.cons_sem(c, s)}"
        case "5":
            c = input("codigo: ").strip()
            return f"{bd.cons_tot(c)}"
        case "6":
            c = input("codigo: ").strip()
            r = input("nueva raza: ").strip()
            e = int(input("nueva edad: "))
            return bd.actualizar(c, r, e)
        case "7":
            c = input("codigo: ").strip()
            return bd.eliminar(c)
        case "8":
            return "salir"
        case _:
            return "invalida"

def entregar_datos(m):
    print("\n-- resultado --")
    print(m)
