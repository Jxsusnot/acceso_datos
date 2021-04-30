from conexion import Conexion
from logger_base import logger

class Persona:
    
    def __init__(self, id_persona = None, nombre = None, apellido = None, email = None):
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getNombre(self):
        return self.__nombre
    
    def setApellido(self, apellido):
        self.__apellido = apellido
        
    def getApellido(self):
        return self.__apellido
    
    def setEmail(self, email):
        self.__email = email
        
    def getEmail(self):
        return self.__email
    
    def __str__(self):
        
        return f'Id: {self.__id_persona}\n Nombre: {self.__nombre}\n Apellido: {self.__apellido}\n Email: {self.__email}'
    
if __name__ == '__main__':
    persona = Persona(nombre='Juan',apellido='Coliseo',email='Juanito20@gmail.com')
    logger.debug(persona)