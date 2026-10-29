# 🧬 Evaluación de la Función Renal
### Computación Paralela con Arquitecturas MIMD, SIMD y MISD

<p align="center">
  <img src="https://github.com/user-attachments/assets/cf8193a4-f0bb-416d-8419-9b7f541cadd0" alt="Presentación del proyecto" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/Computación%20Paralela-MIMD%20%7C%20SIMD%20%7C%20MISD-6C63FF?style=for-the-badge" alt="Computación paralela">
</p>

<p align="center">
  <strong>PROYECTO DE COMPUTACIÓN PARALELA · OPCIÓN 4</strong>
  <br>
  Procesamiento, cálculo y visualización de indicadores de función renal mediante arquitecturas de computación paralela.
</p>

---

## 📑 Tabla de contenidos

- [🎯 Descripción del proyecto](#-descripción-del-proyecto)
- [🎯 Objetivos](#-objetivos)
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

Este proyecto implementa diferentes arquitecturas de computación paralela mediante Python para procesar datos relacionados con la evaluación de la función renal.

El sistema contempla el cálculo de indicadores bioquímicos, la conversión de unidades, el almacenamiento de resultados en una base de datos y su posterior visualización mediante un dashboard interactivo.

La solución se centra en el estudio y la implementación de tres modelos de procesamiento: **MIMD, SIMD y MISD**, con el propósito de comprender sus características y analizar su aplicación al procesamiento de datos.

## 🎯 Objetivos

- Implementar las arquitecturas MIMD, SIMD y MISD mediante Python.
- Procesar datos relacionados con la función renal.
- Calcular la tasa de filtración glomerular estimada (TFGe).
- Realizar conversiones de unidades bioquímicas.
- Almacenar los resultados en una base de datos.
- Visualizar la información procesada mediante un dashboard.
- Facilitar la comparación de los resultados generados por las distintas implementaciones.

---

## 🏗️ Arquitecturas implementadas

### 🔷 MIMD — Multiple Instruction, Multiple Data

Permite ejecutar múltiples instrucciones sobre diferentes conjuntos de datos. Se utiliza para estudiar el procesamiento de tareas o datos mediante flujos de instrucciones independientes.

### 🟣 SIMD — Single Instruction, Multiple Data

Aplica una misma instrucción a múltiples elementos de datos. Este modelo es útil para estudiar operaciones repetitivas y procesamiento de conjuntos de datos.

### 🟠 MISD — Multiple Instruction, Single Data

Consiste en aplicar múltiples instrucciones o tratamientos sobre un mismo flujo de datos. Su aplicación depende del diseño concreto de la implementación.

### Comparación conceptual

| Arquitectura | Instrucciones | Datos | Característica principal |
|---|---|---|---|
| MIMD | Múltiples | Múltiples | Procesamiento independiente de tareas y datos |
| SIMD | Una | Múltiples | Aplicación de una operación sobre varios datos |
| MISD | Múltiples | Un flujo | Distintos tratamientos sobre un mismo flujo de datos |

> **Nota:** la tabla describe los modelos arquitectónicos. El grado real de paralelismo, la estrategia de ejecución y el rendimiento deben verificarse en el código de cada implementación.

---

## 🧪 Evaluación de la función renal

La función renal puede evaluarse mediante indicadores bioquímicos y estimaciones de la tasa de filtración glomerular.

### Indicadores contemplados

| Indicador | Descripción | Unidad |
|---|---|---|
| TFGe / eGFR | Tasa de filtración glomerular estimada | mL/min/1,73 m² |
| Creatinina sérica | Marcador bioquímico empleado en la estimación de la función renal | mg/dL o μmol/L |
| Urea | Parámetro bioquímico relacionado con la evaluación renal | mg/dL o mmol/L |

Los cálculos y las conversiones deben realizarse utilizando las unidades correctas para garantizar la coherencia de los resultados.

---

## 📐 Fórmulas y conversiones

### 1. Tasa de filtración glomerular estimada (TFGe)

Para adultos se contempla la ecuación CKD-EPI 2021 basada en creatinina.

📚 **Referencia oficial:** [National Kidney Foundation — Ecuación de creatinina CKD-EPI 2021](https://www.kidney.org/es/ecuacion-de-creatinina-ckd-epi-2021)

#### Ecuación CKD-EPI 2021

La ecuación se expresa de la siguiente manera:

$$
\mathrm{TFGe} =
142 \times
\min\left(\frac{Scr}{K},1\right)^{\alpha}
\times
\max\left(\frac{Scr}{K},1\right)^{-1.200}
\times
0.9938^{\mathrm{Edad}}
\times F
$$

Donde el factor correspondiente al sexo utilizado por la ecuación es:

$$
F =
\begin{cases}
1.012 & \text{si es mujer} \\
1 & \text{si es hombre}
\end{cases}
$$

**Parámetros de la ecuación:**

| Parámetro | Mujeres | Hombres |
|---|---:|---:|
| K | 0.7 | 0.9 |
| α | -0.241 | -0.302 |

**Variables y abreviaturas:**

- `Scr`: creatinina sérica expresada en mg/dL.
- `K`: constante utilizada por la ecuación según el sexo.
- `α`: exponente utilizado por la ecuación según el sexo.
- `Edad`: edad en años.
- `min(x, 1)`: valor mínimo entre `x` y 1.
- `max(x, 1)`: valor máximo entre `x` y 1.
- `F`: factor de ajuste de 1.012 para mujeres y 1 para hombres.
- **Resultado:** mL/min/1,73 m².

#### Ecuación pediátrica: bedside Schwartz

Para población pediátrica se contempla la ecuación bedside Schwartz:

$$
\mathrm{TFGe} =
41.3 \times
\frac{\mathrm{Talla\ (m)}}{\mathrm{Creatinina\ (mg/dL)}}
$$

**Variables:**

- Talla: estatura en metros.
- Creatinina: creatinina sérica en mg/dL.
- Resultado: mL/min/1,73 m².

La ecuación que debe utilizarse depende de la población y de las condiciones clínicas para las que esté validada.

### 2. Conversión de creatinina

Para convertir creatinina de mg/dL a μmol/L, se multiplica el valor por el factor de conversión 88.4.

**Fórmula matemática:**

$$
\mathrm{Creatinina}_{\mu mol/L}
=
\mathrm{Creatinina}_{mg/dL}
\times 88.4
$$

**Implementación en Python:**

```python
creatinina_umol = creatinina_mg_dl * 88.4
```

**Ejemplo de conversión:**

Si la creatinina es de 1.0 mg/dL:

$$
1.0 \times 88.4 = 88.4\ \mu mol/L
$$

### 3. Conversión de urea

Para convertir urea de mg/dL a mmol/L, se divide el valor por el factor de conversión 6.006.

**Fórmula matemática:**

$$
\mathrm{Urea}_{mmol/L}
=
\frac{\mathrm{Urea}_{mg/dL}}{6.006}
$$

**Implementación en Python:**

```python
urea_mmol_l = urea_mg_dl / 6.006
```

**Ejemplo de conversión:**

Si la urea es de 30 mg/dL:

$$
\frac{30}{6.006}
\approx 4.995\ \mathrm{mmol/L}
$$

### 📋 Resumen de fórmulas

| Operación | Fórmula | Unidad de salida |
|---|---|---|
| TFGe en adultos | Ecuación CKD-EPI 2021 | mL/min/1,73 m² |
| TFGe pediátrica | Ecuación bedside Schwartz | mL/min/1,73 m² |
| Conversión de creatinina | mg/dL × 88.4 | μmol/L |
| Conversión de urea | mg/dL ÷ 6.006 | mmol/L |

> **Importante:** la implementación de las ecuaciones debe respetar sus constantes, exponentes, unidades y población de aplicación. La TFGe es una estimación y no sustituye la valoración de un profesional sanitario.

---

## 🗄️ Base de datos

El proyecto utiliza un conjunto de datos en formato CSV como fuente de información.

**Archivo de datos:**

📄 [`dataset_funcion_renal.csv`](dataset_funcion_renal.csv)

La base de datos permite almacenar los resultados del procesamiento para su posterior consulta desde el dashboard.

### Tecnologías de almacenamiento

- **MySQL/MariaDB:** almacenamiento de los resultados.
- **XAMPP:** entorno local para gestionar los servicios de base de datos.
- **phpMyAdmin:** interfaz para administrar y consultar las tablas.

La conexión y el almacenamiento dependen de la configuración implementada en los archivos Python del proyecto.

---

## 📊 Dashboard interactivo

El proyecto incorpora un dashboard desarrollado con Streamlit para visualizar los resultados generados por el procesamiento.

### Ejecutar el dashboard

```bash
python -m streamlit run dashboard.py
```

Al iniciar el servidor, Streamlit mostrará en la terminal la dirección local de acceso a la aplicación.

El contenido visible, los indicadores, las tablas y los gráficos dependerán de las funcionalidades implementadas en `dashboard.py`.

> **Recomendación visual:** añade aquí una captura real de tu dashboard para mostrar los resultados y mejorar la presentación del repositorio.

<!-- Sustituye la línea siguiente por una captura real cuando esté disponible. -->

---

## ⚙️ Requisitos previos

Antes de ejecutar el proyecto, verifica que tienes instalados y configurados los siguientes componentes:

| Requisito | Función |
|---|---|
| Python 3 | Ejecución de los programas |
| XAMPP | Gestión del entorno local de base de datos |
| MySQL/MariaDB | Almacenamiento de resultados |
| Streamlit | Visualización de datos |
| phpMyAdmin | Administración de la base de datos |
| Archivo CSV | Datos de entrada del proyecto |

También deben estar disponibles los archivos Python, el dataset y las dependencias utilizadas por la implementación.

Si el repositorio contiene un archivo `requirements.txt`, puedes instalar las dependencias con:

```bash
pip install -r requirements.txt
```

---

## 🚀 Instalación y ejecución

### Paso 1. Iniciar XAMPP

Abre una terminal en Linux y ejecuta:

```bash
sudo /opt/lampp/lampp start
```

Para comprobar el estado de los servicios:

```bash
sudo /opt/lampp/lampp status
```

Verifica que el servicio de base de datos esté disponible y que las credenciales configuradas en el proyecto sean correctas.

### Paso 2. Ejecutar la arquitectura MISD

```bash
python misd.py > salida_misd.txt
```

La salida estándar del programa se guardará en `salida_misd.txt`.

### Paso 3. Ejecutar la arquitectura MIMD

```bash
python mimd.py > salida_mimd.txt
```

La salida estándar del programa se guardará en `salida_mimd.txt`.

### Paso 4. Ejecutar la arquitectura SIMD

```bash
python simd.py > salida_simd.txt
```

La salida estándar del programa se guardará en `salida_simd.txt`.

### Paso 5. Iniciar el dashboard

```bash
python -m streamlit run dashboard.py
```

Abre en el navegador la dirección local que Streamlit muestre en la terminal.

### Orden recomendado de ejecución

1. Iniciar XAMPP y comprobar la conexión con la base de datos.
2. Verificar que el dataset esté disponible.
3. Ejecutar los programas de las arquitecturas.
4. Comprobar que los resultados se hayan almacenado correctamente.
5. Iniciar el dashboard y revisar la información presentada.

> **Nota:** los comandos de las tres arquitecturas se ejecutan por separado. El orden anterior es una recomendación operativa; el orden exacto dependerá de las dependencias y del flujo de datos de tu implementación.

---

## 🧹 Reiniciar los resultados

Para eliminar los resultados anteriores y reiniciar el contador de registros, accede a phpMyAdmin, selecciona la base de datos del proyecto y ejecuta las siguientes instrucciones SQL:

```sql
DELETE FROM resultados_funcion_renal;

ALTER TABLE resultados_funcion_renal AUTO_INCREMENT = 1;
```

**¿Qué hace cada instrucción?**

- `DELETE FROM`: elimina los registros existentes de la tabla.
- `ALTER TABLE ... AUTO_INCREMENT = 1`: intenta restablecer el contador de identificadores automáticos.

⚠️ **Advertencia:** la primera instrucción elimina los registros existentes. Realiza una copia de seguridad antes de ejecutarla si necesitas conservar los resultados. El reinicio del contador depende de la estructura de la tabla y de las condiciones de la base de datos.

---

## 📁 Estructura del proyecto

La estructura básica documentada del repositorio es la siguiente:

```text
.
├── README.md
├── dataset_funcion_renal.csv
├── misd.py
├── mimd.py
├── simd.py
└── dashboard.py
```

**Descripción de los archivos:**

| Archivo | Descripción |
|---|---|
| `README.md` | Documentación del proyecto |
| `dataset_funcion_renal.csv` | Conjunto de datos de entrada |
| `misd.py` | Implementación de la arquitectura MISD |
| `mimd.py` | Implementación de la arquitectura MIMD |
| `simd.py` | Implementación de la arquitectura SIMD |
| `dashboard.py` | Aplicación visual desarrollada con Streamlit |

Este árbol debe actualizarse si el repositorio contiene otros módulos, archivos de configuración o carpetas adicionales.

---

## ⚠️ Consideraciones importantes

- **Precisión matemática:** verifica que las fórmulas se implementen con las constantes y los exponentes correctos.
- **Unidades:** asegúrate de que los valores de entrada y salida utilicen las unidades correspondientes.
- **Población:** selecciona las ecuaciones de TFGe según la población para la que estén indicadas.
- **Base de datos:** comprueba la conexión, los permisos y la estructura de las tablas.
- **Resultados:** contrasta los resultados calculados con ejemplos de prueba conocidos.
- **Privacidad:** no publiques datos personales o clínicos identificables en el repositorio.
- **Finalidad:** este proyecto tiene un propósito académico y no sustituye el diagnóstico ni la valoración de un profesional sanitario.

---

<p align="center">
  <strong>PROYECTO DE COMPUTACIÓN PARALELA · OPCIÓN 4</strong>
  <br>
  Python · MIMD · SIMD · MISD · Evaluación de la función renal
  <br><br>
  <sub>Procesamiento paralelo aplicado al análisis de datos bioquímicos.</sub>
</p>
