class PacienteDTO:

    # Constructor
    def __init__(self, nombre, edad, n_historia_clinica, prioridad, riesgo):
        self.__nombre = nombre
        self.__edad = edad
        self.__n_historia_clinica = n_historia_clinica
        self.__prioridad = prioridad
        self.__riesgo = riesgo

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

    def get_prioridad(self):
        return self.__prioridad

    def set_prioridad(self, nueva_prioridad):
        self.__prioridad = nueva_prioridad

    def get_riesgo(self):
        return self.__riesgo

    def set_riesgo(self, nuevo_riesgo):
        self.__riesgo = nuevo_riesgo    