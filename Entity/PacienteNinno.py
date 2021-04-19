from Entity.Paciente import *

class PNinno(Paciente):

    def __init__(self, nombre, edad, n_historia_clinica, peso_estatura):
        super().__init__(nombre,edad,n_historia_clinica)
        self.__peso_estatura = peso_estatura

    # Getters and Setters para encapsulación
    def get_peso_estatura(self):
        return self.__peso_estatura

    def set_peso_estatura(self, nuevo_relacion_peso_estatura):
        self.__peso_estatura = nuevo_relacion_peso_estatura