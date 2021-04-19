from Entity.Consulta import *
from Entity.Paciente import *

class Hospital:

    def __init__(self, lista_consultas, lista_pacientes):
        self.__lista_consultas = lista_consultas
        self.__lista_pacientes = lista_pacientes

    def get_lista_consultas(self):
        return self.__lista_consultas

    def set_lista_consultas(self, nueva_lista_consultas):
        self.__lista_consultas = nueva_lista_consultas

    def get_lista_pacientes(self):
        return self.__lista_pacientes

    def set_lista_pacientes(self, nueva_lista_pacientes):
        self.__lista_pacientes = nueva_lista_pacientes

    def ver_lista_de_consultas(self):
        lista_consultas = []
        for con in self.get_lista_consultas():
            lista_consultas.append(Consulta(con.get_id_consulta(), con.get_cantidad_pacientes_max(), con.get_nombre_especialista(), con.get_tipo_consulta_valor()))
            print('Consulta tipo: ' + con.get_tipo_consulta_valor())
        return lista_consultas
    
    def ver_lista_de_pacientes(self):
        lista_pacientes = []
        for pac in self.get_lista_pacientes():
            lista_pacientes.append(Paciente(pac.get_nombre(), pac.get_edad(), pac.get_n_historia_clinica()))
            print('Paciente: ' + pac.get_nombre())
        return lista_pacientes