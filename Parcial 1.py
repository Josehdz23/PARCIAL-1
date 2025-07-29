empleados = {}

def menu():
    print("\n= = = = MENÚ = = = =\n1. Registrar empleados. \n2. Mostrar empleados. \n3. Buscar empleados. \n4. Mostrar empleados con mejores evaluaciones. \n5. Empleado con mejor promedio\n6. Salir")

def registroEmpleados():
    while True:
        try:
            codigo = int(input("Codigo del empleado: "))
            if codigo in empleados:
                print("El codigo de empleado ya existe, reintente")
            else:
                if codigo > 0:
                    break
                else:
                    print("El codigo de empleado no es válido, reintente")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")

    while True:
        nombre = input("\nIngrese el nombre del empleado: ")
        if nombre or nombre.isnumeric():
            break
        else:
            print("Nombre inválido, reintente")
    while True:
        departamento = input("\nIngrese el departamento del empleado: ")
        if departamento or departamento.isspace():
            break
        else:
            print("Departamento inválido, reintente")
    while True:
        try:
            años = int(input("\nIngrese los años que lleva el empleado en la empresa: "))
            if años > 0:
                break
            else:
                print("El dato de año no es válido, reintente")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")

def main():
    while True:
        try:
            menu()
            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 1:
                    registroEmpleados()
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
main()