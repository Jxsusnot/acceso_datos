from conexion import Conexion
from persona import Persona
from logger_base import logger
import sys

class PersonaDao:
    
    __SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    __INSERTAR = 'INSERT persona(nombre,apellido,email) VALUES (%s,%s,%s)'
    __ACTUALIZAR = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    __ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'
    
    @classmethod
    def seleccionar(cls):
        
        try:
            Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            
            logger.debug(f'Datos: {cursor.mogrify(cls.__SELECCIONAR)}')
            cursor.execute(cls.__SELECCIONAR)
            datos = cursor.fetchall()
            logger.debug(datos)
            
        except Exception as e:
            
            logger.error(f'Error de consulta: {e}')
            sys.exit()
        finally:
            Conexion.cerrar()
            
    @classmethod
    def insertar(self,persona):
        
        try:
            Conexion.obtenerConexion()
            cursor = Conexion.obtenerConexion()
            
            logger.debug(f'Datos: {cursor.mogrify(cls.__INSERTAR)}')
            datos = (persona[0],persona[1],persona[2])
            cursor.execute(cls.__INSERTAR,datos)
            logger.debug(f'Conexión exitosa')

        except Exception as e:
            
            logger.error(f'Error de consulta: {e}')
            sys.exit()
    
        finally:
            conexion.commit()
            Conexion.cerrar()
            
if __name__ == '__main__':
    
    persona = Persona(nombre="Jose",apellido="Antoino",email="lumart@gmail.com")
    PersonaDao.insertar(persona)