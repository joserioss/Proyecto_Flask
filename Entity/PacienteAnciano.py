from Entity.Paciente import *

class PAnciano(Paciente):

    def __init__(self, nombre, edad, n_historia_clinica, dieta = False):
        super().__init__(nombre,edad,n_historia_clinica)
        self.__dieta = dieta
    
    def get_dieta(self):
        return self.__dieta

    def set_dieta(self, dieta):
        self.__dieta = dieta