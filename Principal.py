from Clases import Paciente as pac, ListaDePacientes as lst

listaPac = lst()

def menu():
    print("1. Agregar Paciente")
    print("2. Promedio Paciente")
    print("3. Imprimir Inverso de edades")
    print("4. Salir")
    op = int(input("Digite la opcion: "))
    return op

def agregarPaciente():
    fecha = []
    nombre = input("Digite su nombre: ")
    edad = int(input("Digite su edad: "))
    fecha = [int(input("Día de ingreso: ")), int(input("Mes de ingreso: ")), int(input("Año de ingreso: "))]
    direccion = input("Digite su dirección: ")
    paciente = pac(nombre, edad, fecha, direccion)
    listaPac.agregarPaciente(paciente)

def numeropaciente():
    listaPac.numeroPacientes()

def imprimirInverso():
    final = 0
    listaPac.imprimirInverso(final)

def principal():
    print("Bienvenido al hospital")
    op = 0
    while op != 4:
        op = menu()
        if op == 1: agregarPaciente()
        elif op == 2: numeropaciente()
        elif op == 3: imprimirInverso()
        elif op == 4: print("Adios")
        else:
            print("Opción inválida")
principal()