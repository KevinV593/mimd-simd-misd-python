# LIBRERÍA & BD
import mysql.connector
BASE_DATOS = "prueba_funcion_renal"

# FUNCIÓN DE CONEXIÓN
def conectar_mysql():
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database=BASE_DATOS
    )
    return conexion

# PROGRAMA
if __name__ == "__main__":
    conexion = None

# VALIDACIÓN
    try:
        conexion = conectar_mysql()
        if conexion.is_connected():
            print(f"Conexión Exitosa a: {BASE_DATOS}")
        
    except mysql.connector.Error as error:
        print(f"Error de conexión: {error}")
    
    finally:
        if conexion is not None and conexion.is_connected():
            conexion.close()
            print("Conexión cerrada.")