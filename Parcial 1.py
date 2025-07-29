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
    while True:
        try:
            puntualidad = int(input("\nIngrese en puntos la puntualidad del empleado (0 - 10): "))
            if puntualidad >= 0 and puntualidad <= 10:
                break
            else:
                print("Dato incorrecto, reintente")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")
    while True:
        try:
            equipo = int(input("\nIngrese en puntos el trabajo en equipo del empleado (0 - 10): "))
            if equipo >= 0 and equipo <= 10:
                break
            else:
                print("Dato incorrecto, reintente")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")
    while True:
        try:
            productividad = int(input("\nIngrese en puntos la productividad del empleado (0 - 10): "))
            if productividad >= 0 and productividad <= 10:
                break
            else:
                print("Dato incorrecto, reintente")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")
    while True:
        observaciones = input("Ingrese alguna observación del empleado: ")
        if observaciones or observaciones.isspace():
            break
        else:
            print("Dato incorrecto, reintente")
    sum = puntualidad + productividad + equipo
    promedio = sum/3
    if promedio >= 7:
        estado = "Satisfactorio"
    else:
        estado = "Debe Mejorar!"
    while True:
        try:
            telefono = int(input("\nIngrese el telefono del empleado: "))
            if telefono > 0:
                telefonoaux = str(telefono)
                if len(telefonoaux) == 8:
                    break
                else:
                    print("Número de telefono incompleto o inválido, reintente")
            else:
                print("Número de telefono incompleto o inválido, reintente")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")
    while True:
        correo = input("\nIngrese correo del empleado: ")
        if correo or correo.isspace():
            if "@gmail.com" in correo:
                break
            elif "@hotmail.com" in correo:
                break
            else:
                print("Correo inválido, reintente")
        else:
            print("Correo inválido, reintente")
    empleados[codigo] = {
        "nombre": nombre,
        "departamento": departamento,
        "antigüedad": años,
        "evaluacion": {
            "puntualidad": puntualidad,
            "productividad": productividad,
            "equipo": equipo,
            "observaciones": observaciones,
            "estado": estado,
            "promedio": promedio,
        },
        "contacto": {
            "telefono": telefono,
            "correo": correo,
        }
    }
    print("Se ha agregado un empleado en la empresa!")


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