from Entity.Hospital import *
from Entity.Consulta import *
from Entity.Paciente import *
from Entity.PacienteNinno import *
from Entity.PacienteJoven import *
from Entity.PacienteAnciano import *
from Service.PacienteService import *

# ****************** Datos de prueba para CONSULTAS **************************

lista_consultas = []
lista_pacientes = []
hospital = []

def cargar_consultas():
    lista_consultas.append(Consulta(1,4,'doctor chapatin',2))
    lista_consultas.append(Consulta(2,10,'doctor stranger'))
    lista_consultas.append(Consulta(3,2,'doctor don karft', 1))
    return lista_consultas

# ****************** Datos de prueba para PACIENTES Y HERENCIAS **************************
def cargar_pacientes():
    lista_pacientesNinnos = []
    lista_pacientesJoven = []
    lista_pacientesAnciano = []

    lista_pacientesNinnos.append(PNinno('anais', 8, 18000001, 1))
    lista_pacientesNinnos.append(PNinno('aylen', 4, 18000002, 2))
    lista_pacientesNinnos.append(PNinno('pedro', 12, 18000003, 4))
    lista_pacientesJoven.append(PJoven('paula', 27, 19000001, 0))
    lista_pacientesJoven.append(PJoven('Jose', 28, 19000002, 5))
    lista_pacientesAnciano.append(PAnciano('Ramon', 93, 20000001, True))

    # Union de todos los pacientes un unico listado
    for x in lista_pacientesNinnos:
        lista_pacientes.append(x)
    for x in lista_pacientesJoven:
        lista_pacientes.append(x)
    for x in lista_pacientesAnciano:
        lista_pacientes.append(x)

    return lista_pacientes


# Hospital
def cargar_hospitales():
    hospital.append(Hospital(lista_consultas, lista_pacientes))
    return hospital
