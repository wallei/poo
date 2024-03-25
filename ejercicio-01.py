'''
Crear una clase llamada "Autobús" que herede de la clase "Vehículo". Agrega
atributos específicos como capacidad de pasajeros, número de puertas, número de
asientos, etc. Implementa métodos para carga y descarga de pasajeros.
'''

class Vehiculo:
    def __init__(self, marca, modelo, tipo, año, puertas, transmision):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.año = año
        self.puertas = puertas
        self.transmision = transmision

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Tipo: {self.tipo}, Año: {self.año}, Puertas: {self.puertas}, Transmisión: {self.transmision}")


class Autobus(Vehiculo):
    def __init__(self, marca, modelo, tipo, año, puertas, transmision, capPasajeros, nroPuertas, nroAsientos):
        super().__init__(marca, modelo, tipo, año, puertas, transmision)
        self.capPasajeros = capPasajeros
        self.nroPuertas = nroPuertas
        self.nroAsientos = nroAsientos


# Crear un objeto vehiculo
vehiculo = Vehiculo("Toyota", "Corolla", "Sedán", 2021, 4, "Automática")

# Mostrar información del vehículo
print("\nInformación del Vehículo:")
vehiculo.mostrar_info()

# Crear un objeto autobus
autobus = Autobus("Mercedes-Benz", "Sprinter", "Transporte público", 2022, 2, "Automática", 50, 2, 30)

# Mostrar información del autobús
print("Información del Autobús:")
autobus.mostrar_info()