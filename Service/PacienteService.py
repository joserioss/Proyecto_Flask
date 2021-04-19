from Entity.Hospital import *
from Entity.Consulta import *
from Entity.Paciente import *
from Entity.PacienteNinno import *
from Entity.PacienteJoven import *
from Entity.PacienteAnciano import *

from DTO.PacienteDTO import *

from Service.PacienteService import *

# Falta DAO para consultar a DDBB la lista de pacientes

def buscarPacienteMayor(listaPacientes):
    print('Buscando al paciente Mayor...')
    pacMayor = Paciente('prueba', 0, 0)
    for pac in listaPacientes:
        if(pac.get_edad() > pacMayor.get_edad()):
            pacMayor.set_nombre(pac.get_nombre())
            pacMayor.set_edad(pac.get_edad())
            pacMayor.set_n_historia_clinica(pac.get_n_historia_clinica())
    return pacMayor

def prioridad_pacientes(listaPacientes):
    print('Calculando priodidad de pacientes...')
    lista_pacientes_prioridad = []
    # Calculo prioridad de pacientes segun rango de edad
    for pac in listaPacientes:
        # Pacientes niños
        if(1 <= pac.get_edad() <= 5 ):
            prioridad = pac.get_peso_estatura() + 3
        elif(6 <= pac.get_edad() <= 12 ):
            prioridad = pac.get_peso_estatura() + 2
        elif(13 <= pac.get_edad() <= 15 ):
            prioridad = pac.get_peso_estatura() + 1
        # Pacientes jovenes fumadores y no fumadores
        elif(16 <= pac.get_edad() <= 40 ):
            if(pac.get_fumador() != 0):
                prioridad = (pac.get_fumador()/4) + 2
            else:
                prioridad = 2      
        # Pacientes ancianos con y sin dietas.
        else:
            if(pac.get_dieta() and (60 <= pac.get_edad() <= 100) ):
                prioridad = (pac.get_edad()/20) + 4
            else:
                prioridad = (pac.get_edad()/30) + 3
        # Calculo del riesgo
        if(pac.get_edad() >= 41):
            riesgo = (((pac.get_edad() * prioridad)/100) + 5.3)
        else:    
            riesgo = ((pac.get_edad() * prioridad)/100)
        pac_dto = PacienteDTO(pac.get_nombre(), pac.get_edad(), pac.get_n_historia_clinica(), prioridad, riesgo)
        lista_pacientes_prioridad.append(pac_dto)
    return lista_pacientes_prioridad

def listarPacientesMayorRiesgo(listaPacientes, numero_historia_clinica):
    print('Buscando a pacientes con mayor riesgo...')
    lista_pacientes_riesgo = prioridad_pacientes(listaPacientes)
    lista_mayores = []
    pacActual = PacienteDTO('', 0, 0, 0, 0)
    for pac in lista_pacientes_riesgo:
        if(pac.get_n_historia_clinica() == numero_historia_clinica):
            pacActual.set_nombre(pac.get_nombre())
            pacActual.set_edad(pac.get_edad())
            pacActual.set_n_historia_clinica(pac.get_n_historia_clinica())
            pacActual.set_prioridad(pac.get_prioridad())
            pacActual.set_riesgo(pac.get_riesgo())
    for pac in lista_pacientes_riesgo:
        pacMayorRiesgo = PacienteDTO('', 0, 0, 0, 0)
        if(pac.get_riesgo() > pacActual.get_riesgo()):
            print(pac.get_nombre())
            pacMayorRiesgo.set_nombre(pac.get_nombre())
            pacMayorRiesgo.set_edad(pac.get_edad())
            pacMayorRiesgo.set_n_historia_clinica(pac.get_n_historia_clinica())
            pacMayorRiesgo.set_prioridad(pac.get_prioridad())
            pacMayorRiesgo.set_riesgo(pac.get_riesgo())
            lista_mayores.append(pacMayorRiesgo)
    return lista_mayores
