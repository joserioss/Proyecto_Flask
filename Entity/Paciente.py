class Paciente():
    # Constructor
    def __init__(self, nombre, edad, n_historia_clinica):
        self.__nombre = nombre
        self.__edad = edad
        self.__n_historia_clinica = n_historia_clinica

    # Getters and Setters para encapsulación
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad

    def get_n_historia_clinica(self):
        return self.__n_historia_clinica

    def set_n_historia_clinica(self, nuevo_numero_historia_clinica):
        self.__n_historia_clinica = nuevo_numero_historia_clinica
