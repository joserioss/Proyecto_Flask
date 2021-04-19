class Consulta:

    # Tupla tipo consulta
    __listado_tipos_consultas = ['','Pediatria', 'Urgencia', 'CGI']

    # Constructor
    def __init__(self, id_consulta, cantidad_pacientes_max, nombre_especialista, tipo_consulta = 3):
        self.__id_consulta = id_consulta
        self.__cantidad_pacientes_max = cantidad_pacientes_max
        self.__nombre_especialista = nombre_especialista
        self.__tipo_consulta = tipo_consulta
    
    # Getters and Setters para encapsulación
    def get_id_consulta(self):
        return self.__id_consulta

    def set_id_consulta(self, nuevo_id_consulta):
        self.__id_consulta = nueva_id_consulta

    def get_cantidad_pacientes_max(self):
        return self.__cantidad_pacientes_max

    def set_cantidad_pacientes_max(self, nueva_cantidad_pacientes_max):
        self.__cantidad_pacientes_max = nueva_cantidad_pacientes_max
    
    def get_nombre_especialista(self):
        return self.__nombre_especialista

    def set_nombre_especialista(self, nuevo_nombre_especialista):
        self.__nombre_especialista = nuevo_nombre_especialista
    
    def get_tipo_consulta(self):
        return self.__tipo_consulta

    def get_tipo_consulta_valor(self):
        return self.__listado_tipos_consultas[self.get_tipo_consulta()]

    def set_tipo_consulta(self, nuevo_tipo_consulta):
        self.__tipo_consulta = nuevo_tipo_consulta
