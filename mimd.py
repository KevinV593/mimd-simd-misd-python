# LIBRERÍAS
import csv
import threading
import time
# BD
import mysql.connector
from conexion import conectar_mysql

# ARREGLOS PARA EXTRAER DATASET
id = []
nombre = []
apellido = []
edad = []
sexo = []
altura_cm = []
creatinina_mg_dl = []
urea_mg_dl = []

# LEER DATASET
with open("dataset_funcion_renal.csv", "r", # -> Permisos de Lectura
          encoding="utf-8-sig", newline="") as archivo:
    lector = csv.reader(archivo)
    next(lector)    # Salta encabezado
    for fila in lector:
        id.append(int (fila[0]))
        nombre.append(str (fila[1]))
        apellido.append(str (fila[2]))
        edad.append(int (fila[3]))
        sexo.append(str (fila[4]))
        altura_cm.append(float (fila[5]))
        creatinina_mg_dl.append(float (fila[6]))
        urea_mg_dl.append(float (fila[7]))
        
if len(id) != 6000:
    raise ValueError(
        f"Se esperaban 6000 registros, pero se cargaron {len(id)}."
    )
    
print("Datos Cargados Correctamente")
print(f"Número de elementos cargados: {len(id)}")

# ARREGLOS PARA RESULTADOS
arquitectura = "MIMD"
tfge_ml_min_1_73_m2 = [0.0] * len(id)
creatinina_umol_l = [0.0] * len(id)
urea_mmol_l = [0.0] * len(id)

# FUNCIONES CON RANGOS
def calcular_tfge(inicio, fin):
    for i in range(inicio, fin):
        altura_m = altura_cm[i] / 100
        
        #FÓRMULA PEDIÁTRICA (Ecuación de Schwartz)
        if edad[i] <= 17:   
            tfge_ml_min_1_73_m2[i] = (
                41.3 * altura_m / creatinina_mg_dl[i]
            )
        
        #FÓRMULA PARA ADULTOS (CKD-EPI 2021)
        else:
            if sexo[i] == "F":
                k = 0.7
                alfa = -0.241
                factor_sexo = 1.012
                
            elif sexo[i] == "M":
                k = 0.9
                alfa = -0.302
                factor_sexo = 1
            
            relacion = creatinina_mg_dl[i] / k
            
            tfge_ml_min_1_73_m2[i] = (
                142
                * min(relacion, 1) ** alfa
                * max (relacion, 1) ** (-1.200)
                * 0.9938 ** edad[i] * factor_sexo
            )

def convertir_creatinina(inicio,fin):
    for i in range(inicio,fin):
        creatinina_umol_l[i] = (
            creatinina_mg_dl[i] * 88.4
        )

def convertir_urea(inicio,fin):
    for i in range(inicio, fin):
        urea_mmol_l[i] = (
            urea_mg_dl[i] / 6.006
        )
        
# HILOS
hilo1 = threading.Thread(
    target = calcular_tfge,
    args = (0, 2000)
)
hilo2 = threading.Thread(
    target=convertir_creatinina,
    args= (2000, 4000)
)
hilo3 = threading.Thread(
    target=convertir_urea,
    args=(4000, 6000)    
)

tiempo_inicio = time.perf_counter_ns()

hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()

tiempo_fin = time.perf_counter_ns()
tiempo_total = (tiempo_fin - tiempo_inicio) / 1000 # microsegundos

print("===================================================")
print("ARQUITECTURA MIMD")
print("===================================================\n")
print(f"RESULTADOS HILO 1 (1 - 2000)\n")
for i in range(0, 2000):
    print("===================================================")
    print(f"Registro Nro. {id[i]}:")
    print(f"Nombre y Apellido: {nombre[i]} {apellido[i]}")
    print(f"Edad: {edad[i]}")
    print(f"Sexo: {sexo[i]}")
    print(f"Altura: {altura_cm[i]}cm")
    print(f"Creatina: {creatinina_mg_dl[i]}mg/dL")
    print(f"Urea: {urea_mg_dl[i]}mg/dL")
    print(f"\n \t Función Renal => TFGe: {tfge_ml_min_1_73_m2[i]:.3f} ml/min/1.73 m2")

print("===================================================\n")
print(f"RESULTADOS HILO 2 (2001 - 4000)\n")
for i in range(2000, 4000):
    print("===================================================")
    print(f"Registro Nro. {id[i]}:")
    print(f"Nombre y Apellido: {nombre[i]} {apellido[i]}")
    print(f"Edad: {edad[i]}")
    print(f"Sexo: {sexo[i]}")
    print(f"Altura: {altura_cm[i]}cm")
    print(f"Creatina: {creatinina_mg_dl[i]}mg/dL")
    print(f"Urea: {urea_mg_dl[i]}mg/dL")
    print(f"\n \t Función Renal => Creatinina: {creatinina_umol_l[i]:.3f} umol/L ")
    
print("===================================================\n")
print(f"RESULTADOS HILO 3 (4001 - 6000)\n")
for i in range(4000, 6000):
    print("===================================================")
    print(f"Registro Nro. {id[i]}:")
    print(f"Nombre y Apellido: {nombre[i]} {apellido[i]}")
    print(f"Edad: {edad[i]} ")
    print(f"Sexo: {sexo[i]} ")
    print(f"Altura: {altura_cm[i]}cm")
    print(f"Creatina: {creatinina_mg_dl[i]}mg/dL")
    print(f"Urea: {urea_mg_dl[i]}mg/dL")
    print(f"\n \t Función Renal => Urea: {urea_mmol_l[i]}mmol/L")
    
print("===================================================")
print("\n \t PRIMER REGISTRO:", id[0] )
print("\t ULTIMO REGISTRO:", id[-1] )
print("\t TOTAL REGISTROS:", len(id))

print(f"\t TIEMPO: {tiempo_total:.4f} microsegundos.")
print("===================================================")

# SUBIR A BD
conexion = None
cursor = None

try:
    conexion = conectar_mysql()
    cursor = conexion.cursor()
    print(f"Conexión Exitosa a la BD")
    # SQL SCRIPTS
    sql_original= """
        INSERT INTO registros_pacientes (
            id,
            nombre,
            apellido,
            edad,
            sexo,
            altura_cm,
            creatinina_mg_dl,
            urea_mg_dl
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            nombre = VALUES(nombre),
            apellido = VALUES(apellido),
            edad = VALUES(edad),
            sexo = VALUES(sexo),
            altura_cm = VALUES(altura_cm),
            creatinina_mg_dl = VALUES(creatinina_mg_dl),
            urea_mg_dl = VALUES(urea_mg_dl);
    """
    sql_resultado="""
        INSERT INTO resultados_funcion_renal (
            registro_id,
            arquitectura,
            tfge_ml_min_1_73_m2,
            creatinina_umol_l,
            urea_mmol_l,
            tiempo_microsegundos
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    # INSERTAR REGISTROS Y RESULTADOS
    for i in range(len(id)):
        cursor.execute(sql_original, (
            id[i],
            nombre[i],
            apellido[i],
            edad[i],
            sexo[i],
            altura_cm[i],
            creatinina_mg_dl[i],
            urea_mg_dl[i]
        ))
        cursor.execute(sql_resultado, (
            id[i],
            arquitectura,
            tfge_ml_min_1_73_m2[i],
            creatinina_umol_l[i],
            urea_mmol_l[i],
            tiempo_total
        ))
        
    # ALMACENAMIENTO DE DATOS
    conexion.commit()

    print("\n¡Datos guardados!")
    print(f"Registros procesados: {len(id)}")
    print(f"Arquitectura: {arquitectura}")

# VALIDACIONES
except mysql.connector.Error as error:
    if conexion is not None and conexion.is_connected():
        conexion.rollback()

    print(f"Error al guardar datos: {error}")

finally:
    if cursor is not None:
        cursor.close()

    if conexion is not None and conexion.is_connected():
        conexion.close()