class Paciente:
    def __init__(self, nom, edad, fecha, dom):
        self.Nombre = nom
        self.Edad = edad
        self.FechaDeIngreso = fecha
        self.Domicilio = dom

    def __str__(self):
        return f"""Nombre: {self.Nombre}
Edad: {self.Edad}
Fecha de Ingreso: {self.FechaDeIngreso}
Domicilio: {self.Domicilio}
"""

class ListaDePacientes:
    def __init__(self):
        self.listaPacientes = []

    def agregarPaciente(self, paciente):
        self.listaPacientes.append(paciente)

    def numeroPacientes(self):
        suma = 0
        contador = 0
        for pac in self.listaPacientes:
            if pac.Edad >=20 and pac.Edad <=30:
                suma += pac.Edad
                contador += 1
                print(pac)
        promedio = suma/contador
        print("El número de personas en ese ranfgo de edad es de: ", contador)
        print("El promedio es de: ", promedio)

    def imprimirInverso(self, final):
        final = len(self.listaPacientes)-1
        if self.listaPacientes[final] == self.listaPacientes[0]:
            print(self.listaPacientes[final])
        else:
            print(self.listaPacientes[final])
            self.imprimirInverso(final-1)