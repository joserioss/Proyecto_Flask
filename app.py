from Entity.Hospital import *
from Entity.Consulta import *
from Entity.Paciente import *
from Entity.PacienteNinno import *
from Entity.PacienteJoven import *
from Entity.PacienteAnciano import *

from Service.PacienteService import *

from Utility.CargaDatos import *

from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

lista_consultas = cargar_consultas()
lista_pacientes = cargar_pacientes()
lista_hospitales = cargar_hospitales()



# ****************** Ruteo pagina principal **************************
@app.route('/')
def index(): 
    return render_template('base.html')


@app.route('/hospital')
def verHospital():   
    for hos in hospital:
        hos.ver_lista_de_consultas()
        hos.ver_lista_de_pacientes()
    return render_template('hospital.html', lista_pacientes = lista_pacientes, lista_consultas = lista_consultas)

@app.route('/hospital/mayor-riesgo/')
@app.route('/hospital/mayor-riesgo/<int:n_historia>/')
def verMayoresRiesgos(n_historia = None):  
    lista_riesgos = listarPacientesMayorRiesgo(lista_pacientes, n_historia)
    return render_template('hospital.html', lista_pacientes = lista_riesgos)

@app.route('/prioridad')
def verPrioridad():   
    for hos in hospital:
        lista_pacientes_prioridad = prioridad_pacientes(lista_pacientes)
        return render_template('prioridad.html', lista_pacientes_DTO = lista_pacientes_prioridad)

@app.route('/consultas')
def verConsultas():   
    for con in lista_consultas:
        print(con.get_tipo_consulta())
        return render_template('tabla.html', nombre=con.get_tipo_consulta_valor())

@app.route('/mayor')
def buscarMayor():   
    x = buscarPacienteMayor(lista_pacientes)
    print('Paciente mayor encontrado: '+ x.get_nombre())
    return render_template('tabla.html', nombre=x.get_nombre())
