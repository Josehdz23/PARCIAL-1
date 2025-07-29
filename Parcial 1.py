empleados = {}

def menu():
    print("\n= = = = MENÚ = = = =\n1. Registrar empleados. \n2. Mostrar empleados. \n3. Buscar empleados. \n4. Mostrar empleados con mejores evaluaciones. \n5. Empleado con mejor promedio\n6. Salir")

def main():
    while True:
        try:
            menu()
            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 1:
                    print()
                case 2:
                    print()
                case 3:
                    print()
                case 4:
                    print()
                case 5:
                    print()
                case 6:
                    print("SALIENDO . . .")
                    break
                case _:
                    print("Esa opción no existe, reintente")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")
menu()