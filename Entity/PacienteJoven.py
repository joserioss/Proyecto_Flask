from Entity.Paciente import *

class PJoven(Paciente):

    def __init__(self, nombre, edad, n_historia_clinica, fumador = 0):
        super().__init__(nombre,edad,n_historia_clinica)
        self.__fumador = fumador

    def get_fumador(self):
        return self.__fumador

    def set_fumador(self, fumador):
        self.__fumador = fumador