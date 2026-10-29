# 🧬 Evaluación de la Función Renal
### Computación Paralela con Arquitecturas MIMD, SIMD y MISD

<p align="center">
  <img src="https://github.com/user-attachments/assets/cf8193a4-f0bb-416d-8419-9b7f541cadd0" alt="Presentación del proyecto" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/Parallel_Computing-MIMD%20%7C%20SIMD%20%7C%20MISD-6C63FF?style=for-the-badge" alt="Computación paralela">
</p>

<p align="center">
  <strong>OPCIÓN 4 · PROYECTO ACADÉMICO</strong><br>
  Implementación y comparación de arquitecturas de computación paralela aplicadas al procesamiento de datos de función renal.
</p>

---

## 📑 Tabla de contenidos

- [🎯 Descripción del proyecto](#-descripción-del-proyecto)
- [🏗️ Arquitecturas implementadas](#️-arquitecturas-implementadas)
- [🧪 Evaluación de la función renal](#-evaluación-de-la-función-renal)
- [📐 Fórmulas y conversiones](#-fórmulas-y-conversiones)
- [🗄️ Base de datos](#️-base-de-datos)
- [📊 Dashboard](#-dashboard)
- [⚙️ Requisitos previos](#️-requisitos-previos)
- [🚀 Instalación y ejecución](#-instalación-y-ejecución)
- [🧹 Reiniciar los resultados](#-reiniciar-los-resultados)
- [📁 Estructura del proyecto](#-estructura-del-proyecto)
- [⚠️ Consideraciones](#️-consideraciones)

---

## 🎯 Descripción del proyecto

Este proyecto desarrolla una solución de **computación paralela aplicada a la evaluación de la función renal**, utilizando Python para procesar información y calcular indicadores bioquímicos a partir de datos de pacientes.

Se implementan tres enfoques arquitectónicos:

- **MIMD:** Multiple Instruction, Multiple Data.
- **SIMD:** Single Instruction, Multiple Data.
- **MISD:** Multiple Instruction, Single Data.

El sistema contempla el procesamiento de datos, la aplicación de fórmulas matemáticas, el almacenamiento de resultados y su visualización mediante un dashboard interactivo.

### 🎯 Objetivos

- Implementar tres arquitecturas de computación paralela.
- Calcular indicadores relacionados con la función renal.
- Realizar conversiones entre unidades bioquímicas.
- Almacenar los resultados procesados en una base de datos.
- Visualizar los resultados mediante un dashboard.
- Facilitar el análisis y la comparación de los resultados obtenidos.

---

## 🏗️ Arquitecturas implementadas

<table>
  <tr>
    <th>Arquitectura</th>
    <th>Modelo de procesamiento</th>
    <th>Descripción</th>
  </tr>
  <tr>
    <td><strong>🔷 MIMD</strong></td>
    <td>Múltiples instrucciones · Múltiples datos</td>
    <td>Permite ejecutar diferentes instrucciones sobre distintos conjuntos de datos.</td>
  </tr>
  <tr>
    <td><strong>🟣 SIMD</strong></td>
    <td>Una instrucción · Múltiples datos</td>
    <td>Aplica una misma operación a varios elementos de datos.</td>
  </tr>
  <tr>
    <td><strong>🟠 MISD</strong></td>
    <td>Múltiples instrucciones · Un flujo de datos</td>
    <td>Utiliza distintos tratamientos o instrucciones sobre un mismo flujo de datos, según la implementación del proyecto.</td>
  </tr>
</table>

> **Propósito:** estudiar cómo se organiza el procesamiento de los datos en cada arquitectura y comparar los resultados obtenidos mediante la implementación.

---

## 🧪 Evaluación de la función renal

La función renal se estudia mediante indicadores que permiten estimar la capacidad de filtración de los riñones y procesar parámetros bioquímicos relevantes.

### Indicadores contemplados

| Indicador | Descripción | Unidad |
|---|---|---|
| TFGe / eGFR | Tasa de filtración glomerular estimada | mL/min/1,73 m² |
| Creatinina sérica | Marcador bioquímico utilizado en la estimación renal | mg/dL o μmol/L |
| Urea | Parámetro bioquímico utilizado en la evaluación renal | mg/dL o mmol/L |

---

## 📐 Fórmulas y conversiones

### 1. Tasa de filtración glomerular estimada (TFGe)

Se contempla la ecuación **CKD-EPI 2021 basada en creatinina** para adultos.

📚 Referencia oficial: [National Kidney Foundation — Ecuación CKD-EPI 2021](https://www.kidney.org/es/ecuacion-de-creatinina-ckd-epi-2021)

#### Ecuación CKD-EPI 2021

\[
\begin{aligned}
\mathrm{TFGe} ={}& 142 \times \\
&\min(Scr/K,1)^\alpha \times\\
&\max(Scr/K,1)^{-1.200} \times\\
&0.9938^{\mathrm{Edad}} \times\\
&1.012 \quad \text{(si es mujer)}
\end{aligned}
\]

**Parámetros de la ecuación:**

| Parámetro | Mujeres | Hombres |
|---|---:|---:|
| \(K\) | 0.7 | 0.9 |
| \(\alpha\) | -0.241 | -0.302 |

**Variables:**

- \(Scr\): creatinina sérica en mg/dL.
- \(K\): constante dependiente del sexo utilizado por la ecuación.
- \(\alpha\): exponente dependiente del sexo.
- \(\min\): valor mínimo entre \(Scr/K\) y 1.
- \(\max\): valor máximo entre \(Scr/K\) y 1.
- Edad: edad en años.
- Resultado: mL/min/1,73 m².

#### Ecuación pediátrica: bedside Schwartz

Para población pediátrica, se contempla la ecuación bedside Schwartz:

\[
\boxed{
\mathrm{TFGe} = 41.3 \times
\frac{\mathrm{Talla\ (m)}}{\mathrm{Creatinina\ (mg/dL)}}
}
\]

**Variables:**

- Talla: estatura en metros.
- Creatinina: creatinina sérica en mg/dL.
- Resultado: mL/min/1,73 m².

### 2. Conversión de creatinina

Para convertir creatinina de mg/dL a μmol/L:

\[
\boxed{
\mathrm{Creatinina}_{\mu mol/L}
=
\mathrm{Creatinina}_{mg/dL}\times 88.4
}
\]

**Implementación en Python:**

```python
creatinina_umol = creatinina_mg_dl * 88.4
```

### 3. Conversión de urea

Para convertir urea de mg/dL a mmol/L:

\[
\boxed{
\mathrm{Urea}_{mmol/L}
=
\frac{\mathrm{Urea}_{mg/dL}}{6.006}
}
\]

**Implementación en Python:**

```python
urea_mmol_l = urea_mg_dl / 6.006
```

> **Nota científica:** la implementación de CKD-EPI debe respetar exactamente los exponentes y las constantes de la ecuación original. En particular, el término de creatinina elevada a la potencia negativa corresponde a \(\max(Scr/K,1)^{-1.200}\). Verifica que el código utilice esa expresión y que aplique el factor 1.012 únicamente cuando corresponda. Las ecuaciones de adultos y pediátricas deben seleccionarse según la población a la que se destinen.

---

## 🗄️ Base de datos

Los datos de entrada se encuentran en el archivo CSV del proyecto:

📄 **Dataset:** [`dataset_funcion_renal.csv`](dataset_funcion_renal.csv)

La base de datos se utiliza para almacenar los resultados generados durante el procesamiento, que posteriormente pueden consultarse desde el dashboard.

**Tecnología de almacenamiento:** MySQL/MariaDB mediante el entorno XAMPP, según la configuración del proyecto.

---

## 📊 Dashboard

El proyecto incluye una interfaz visual desarrollada con **Streamlit** para consultar los resultados del procesamiento.

El dashboard se inicia con:

```bash
python -m streamlit run dashboard.py
```

Desde la interfaz se pueden visualizar los datos y resultados que el código haya implementado. La disponibilidad de tablas, gráficos, métricas y comparaciones dependerá de las funcionalidades programadas en `dashboard.py`.

---

## ⚙️ Requisitos previos

Antes de ejecutar el proyecto, asegúrate de disponer de:

- Python 3 instalado.
- XAMPP con MySQL o MariaDB configurado.
- Las dependencias de Python utilizadas por el proyecto.
- El archivo `dataset_funcion_renal.csv`.
- Los archivos `misd.py`, `mimd.py`, `simd.py` y `dashboard.py`.

> Si el proyecto dispone de un archivo `requirements.txt`, instala sus dependencias con `pip install -r requirements.txt`.

---

## 🚀 Instalación y ejecución

### Paso 1. Iniciar XAMPP

En una terminal Linux, ejecuta:

```bash
sudo /opt/lampp/lampp start
```

Para comprobar el estado de los servicios:

```bash
sudo /opt/lampp/lampp status
```

Verifica que el servicio de base de datos esté disponible y que las credenciales coincidan con las configuradas en el proyecto.

### Paso 2. Ejecutar la arquitectura MISD

```bash
python misd.py > salida_misd.txt
```

La salida estándar se guarda en `salida_misd.txt`.

### Paso 3. Ejecutar la arquitectura MIMD

```bash
python mimd.py > salida_mimd.txt
```

La salida estándar se guarda en `salida_mimd.txt`.

### Paso 4. Ejecutar la arquitectura SIMD

```bash
python simd.py > salida_simd.txt
```

La salida estándar se guarda en `salida_simd.txt`.

> **Importante:** los tres comandos anteriores se ejecutan por separado. Si los scripts necesitan acceder a MySQL, comprueba que la base de datos esté activa y configurada antes de iniciarlos.

### Paso 5. Iniciar el dashboard

```bash
python -m streamlit run dashboard.py
```

Streamlit mostrará en la terminal la dirección local desde la que se puede abrir la aplicación en el navegador.

---

## 🧹 Reiniciar los resultados

Si necesitas vaciar la tabla de resultados antes de una nueva ejecución, abre **phpMyAdmin**, selecciona la base de datos correcta y ejecuta:

```sql
DELETE FROM resultados_funcion_renal;

ALTER TABLE resultados_funcion_renal AUTO_INCREMENT = 1;
```

⚠️ **Advertencia:** esta operación elimina los registros existentes de `resultados_funcion_renal`. Realiza una copia de seguridad si necesitas conservarlos.

El reinicio del contador `AUTO_INCREMENT` depende de que la tabla y su estructura admitan esa operación. Ejecuta estas instrucciones únicamente sobre la base de datos del proyecto.

---

## 📁 Estructura del proyecto

```text
.
├── README.md
├── dataset_funcion_renal.csv
├── misd.py
├── mimd.py
├── simd.py
└── dashboard.py
```

Esta estructura representa los archivos identificados en la documentación. Si el repositorio contiene módulos, carpetas o archivos adicionales, inclúyelos en el árbol definitivo.

---

## ⚠️ Consideraciones

- Los resultados deben verificarse con las ecuaciones y unidades correspondientes.
- La selección de la ecuación de TFGe depende de la población y de las condiciones de uso.
- Los datos utilizados deben tratarse de forma responsable, especialmente si contienen información personal o clínica.
- Este proyecto tiene una finalidad académica y de computación paralela. Sus resultados no sustituyen la valoración de un profesional sanitario.

---

<p align="center">
  <strong>Proyecto de Computación Paralela · Opción 4</strong><br>
  <sub>Python · MIMD · SIMD · MISD · Evaluación de la función renal</sub>
</p>
