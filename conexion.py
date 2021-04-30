from logger_base import logger
import psycopg2 as db
import sys

class Conexion:
    
    __DATABASE = 'test_db'
    __USERNAME = 'postgres'
    __PASSWORD = 'admin'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'
    __conexion = None
    __cursor = None
    
    @classmethod
    def obtenerConexion(cls):
        
        if cls.__conexion is None:
            
            try:
                
                cls.__conexion = db.connect(database=cls.__DATABASE,
                                            user=cls.__USERNAME,
                                            password=cls.__PASSWORD,
                                            port=cls.__DB_PORT,
                                            host=cls.__HOST)
                
                logger.info(f'Conexión exitosa: {cls.__conexion}')
                return cls.__conexion
            except Exception as e:
                logger.error(f'Conexión fallida: {e}')
                sys.exit()
                cls.__conexion.close()
        else: 
            return cls.__conexion
        
    @classmethod
    def obtenerCursor(cls):
        
        if cls.__cursor is None:
            
            try:
                
                cls.__cursor = cls.__conexion.cursor()
                logger.info(f'Cursor exitoso: {cls.__cursor}')
                return cls.__cursor
            
            except Exception as e:
                
                logger.error(f'Cursor fallido: {e}')
                sys.exit()
        else:
            return cls.__cursor
        
    @classmethod
    def cerrar(cls):
        
        if cls.__conexion is not None:
            
            try:
                cls.__conexion.close()
            except Exception as e:
                logger.error(f'Conexión cerrada fallida: {e}')
        
        if cls.__cursor is not None:
            
            try:
                cls.__cursor.close()
            except Exception as e:
                logger.error(f'Cursor cerrada fallida: {e}')
        
if __name__ == '__main__':
    logger.debug(Conexion.obtenerConexion())
    logger.debug(Conexion.cerrar())