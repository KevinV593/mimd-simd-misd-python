# 🧬 Evaluación de la Función Renal
### Computación Paralela con Arquitecturas MIMD, SIMD y MISD
Grupo 6: Camila Amores & Kevin Vaca


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

---

## 🎯 Descripción del proyecto

Este proyecto implementa diferentes arquitecturas de computación paralela mediante Python para procesar datos relacionados con la evaluación de la función renal.

El sistema contempla el cálculo de indicadores bioquímicos, la conversión de unidades, el almacenamiento de resultados en una base de datos y su posterior visualización mediante un dashboard interactivo.

Se estudian tres modelos de procesamiento: **MIMD, SIMD y MISD**, con el propósito de comprender sus características y analizar su aplicación al procesamiento de datos.

## 🎯 Objetivos

- Implementar las arquitecturas MIMD, SIMD y MISD mediante Python.
- Procesar datos relacionados con la función renal.
- Calcular la tasa de filtración glomerular estimada (TFGe).
- Realizar conversiones de unidades bioquímicas.
- Almacenar los resultados en una base de datos.
- Visualizar la información procesada mediante un dashboard.
- Facilitar la comparación de los resultados de las distintas implementaciones.

---

## 🏗️ Arquitecturas implementadas

### 🔷 MIMD — Multiple Instruction, Multiple Data

Permite ejecutar múltiples instrucciones sobre diferentes conjuntos de datos. Se utiliza para estudiar el procesamiento de tareas o datos mediante flujos de instrucciones independientes.

### 🟣 SIMD — Single Instruction, Multiple Data

Aplica una misma instrucción a múltiples elementos de datos. Este modelo es útil para estudiar operaciones repetitivas sobre conjuntos de datos.

### 🟠 MISD — Multiple Instruction, Single Data

Consiste en aplicar múltiples instrucciones o tratamientos sobre un mismo flujo de datos. Su aplicación depende del diseño concreto de la implementación.

### Comparación conceptual

| Arquitectura | Instrucciones | Datos | Característica principal |
|---|---|---|---|
| MIMD | Múltiples | Múltiples | Procesamiento de tareas y datos independientes |
| SIMD | Una | Múltiples | Una operación aplicada a varios datos |
| MISD | Múltiples | Un flujo | Diferentes tratamientos sobre un mismo flujo de datos |

> La tabla describe los modelos arquitectónicos. El grado real de paralelismo y el rendimiento deben verificarse en el código de cada implementación.

---

## 🧪 Evaluación de la función renal

La función renal puede estudiarse mediante indicadores bioquímicos y estimaciones de la tasa de filtración glomerular.

### Indicadores contemplados

| Indicador | Descripción | Unidad |
|---|---|---|
| TFGe / eGFR | Tasa de filtración glomerular estimada | mL/min/1,73 m² |
| Creatinina sérica | Marcador bioquímico utilizado para estimar la función renal | mg/dL o μmol/L |
| Urea | Parámetro bioquímico relacionado con la evaluación renal | mg/dL o mmol/L |

---

## 📐 Fórmulas y conversiones

### 1. Tasa de filtración glomerular estimada (TFGe)

Para adultos se contempla la ecuación CKD-EPI 2021 basada en creatinina.

📚 **Referencia oficial:** [National Kidney Foundation — Ecuación de creatinina CKD-EPI 2021](https://www.kidney.org/es/ecuacion-de-creatinina-ckd-epi-2021)

#### Ecuación CKD-EPI 2021

La tasa de filtración glomerular estimada se calcula mediante la siguiente expresión:

**TFGe = 142 × min(Scr/K, 1)^α × max(Scr/K, 1)^(-1.200) × 0.9938^Edad × F**

Donde:

- **Scr:** creatinina sérica en mg/dL.
- **K:** constante que depende del sexo utilizado por la ecuación.
- **α:** exponente que depende del sexo.
- **Edad:** edad en años.
- **min(x, 1):** valor mínimo entre x y 1.
- **max(x, 1):** valor máximo entre x y 1.
- **F:** factor de ajuste según el sexo utilizado por la ecuación.

#### Parámetros de la ecuación

| Parámetro | Mujeres | Hombres |
|---|---:|---:|
| K | 0.7 | 0.9 |
| α | -0.241 | -0.302 |
| F | 1.012 | 1 |

**Unidad del resultado:** mL/min/1,73 m².

#### Ecuación pediátrica: bedside Schwartz

Para población pediátrica se contempla la siguiente expresión:

**TFGe = 41.3 × (Talla en metros / Creatinina en mg/dL)**

| Variable | Descripción |
|---|---|
| Talla | Estatura en metros |
| Creatinina | Creatinina sérica en mg/dL |
| Resultado | mL/min/1,73 m² |

La ecuación debe seleccionarse de acuerdo con la población para la que esté indicada.

### 2. Conversión de creatinina: mg/dL a μmol/L

Esta conversión permite expresar la concentración de creatinina en micromoles por litro.

#### Fórmula

**Creatinina en μmol/L = Creatinina en mg/dL × 88.4**

#### Implementación en Python

```python
creatinina_umol = creatinina_mg_dl * 88.4
```

#### Ejemplo

| Concepto | Valor |
|---|---:|
| Creatinina original | 1.0 mg/dL |
| Factor de conversión | 88.4 |
| Resultado convertido | 88.4 μmol/L |

**Cálculo:** 1.0 × 88.4 = 88.4 μmol/L.

### 3. Conversión de urea: mg/dL a mmol/L

Esta conversión permite expresar la concentración de urea en milimoles por litro.

#### Fórmula

**Urea en mmol/L = Urea en mg/dL ÷ 6.006**

#### Implementación en Python

```python
urea_mmol_l = urea_mg_dl / 6.006
```

#### Ejemplo

| Concepto | Valor |
|---|---:|
| Urea original | 30 mg/dL |
| Factor de conversión | 6.006 |
| Resultado convertido | 4.995 mmol/L aproximadamente |

**Cálculo:** 30 ÷ 6.006 ≈ 4.995 mmol/L.

### 📋 Resumen de fórmulas y conversiones

| Operación | Fórmula en texto | Unidad de salida |
|---|---|---|
| TFGe en adultos | Ecuación CKD-EPI 2021 | mL/min/1,73 m² |
| TFGe pediátrica | 41.3 × (talla en m / creatinina en mg/dL) | mL/min/1,73 m² |
| Creatinina | mg/dL × 88.4 | μmol/L |
| Urea | mg/dL ÷ 6.006 | mmol/L |

---

## 🗄️ Base de datos

El proyecto utiliza un conjunto de datos en formato CSV como fuente de información.

📄 **Dataset:** [`dataset_funcion_renal.csv`](dataset_funcion_renal.csv)

La base de datos permite almacenar los resultados del procesamiento para su posterior consulta desde el dashboard.

### Tecnologías de almacenamiento

- **MySQL/MariaDB:** almacenamiento de resultados.
- **XAMPP:** entorno local para gestionar los servicios de base de datos.
- **phpMyAdmin:** administración de la base de datos y sus tablas.

La conexión y el almacenamiento dependen de la configuración implementada en los archivos Python.

---

## 📊 Dashboard interactivo

El proyecto incorpora un dashboard desarrollado con **Streamlit** para visualizar los resultados generados por el procesamiento.

### Ejecutar el dashboard

```bashstreamlit
python -m streamlit run dashboard.py
```

Streamlit mostrará en la terminal la dirección local de acceso a la aplicación.

El contenido visible, los indicadores, las tablas y los gráficos dependerán de las funcionalidades implementadas en `dashboard.py`.



---

## ⚙️ Requisitos previos

Antes de ejecutar el proyecto, verifica que dispones de los siguientes componentes:

| Requisito | Función |
|---|---|
| Python 3 | Ejecución de los programas |
| XAMPP | Entorno local de servicios |
| MySQL/MariaDB | Almacenamiento de resultados |
| Streamlit | Visualización de datos |
| phpMyAdmin | Administración de la base de datos |
| Archivo CSV | Datos de entrada |

También deben estar disponibles los archivos Python, el dataset y las dependencias utilizadas.

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

La salida estándar se guardará en `salida_misd.txt`.

### Paso 3. Ejecutar la arquitectura MIMD

```bash
python mimd.py > salida_mimd.txt
```

La salida estándar se guardará en `salida_mimd.txt`.

### Paso 4. Ejecutar la arquitectura SIMD

```bash
python simd.py > salida_simd.txt
```

La salida estándar se guardará en `salida_simd.txt`.

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

> Los comandos de las tres arquitecturas se ejecutan por separado. El orden exacto dependerá de las dependencias de la implementación.

---

## 🧹 Reiniciar los resultados

Para eliminar los resultados anteriores y reiniciar el contador de registros, accede a phpMyAdmin, selecciona la base de datos del proyecto y ejecuta:

```sql
DELETE FROM resultados_funcion_renal;

ALTER TABLE resultados_funcion_renal AUTO_INCREMENT = 1;
```

**¿Qué hace cada instrucción?**

- `DELETE FROM`: elimina los registros existentes de la tabla.
- `ALTER TABLE ... AUTO_INCREMENT = 1`: intenta restablecer el contador de identificadores automáticos.

⚠️ **Advertencia:** la primera instrucción elimina los registros existentes. Realiza una copia de seguridad si necesitas conservar los resultados. El reinicio del contador depende de la estructura de la tabla y de las condiciones de la base de datos.

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

### Descripción de los archivos

| Archivo | Descripción |
|---|---|
| `README.md` | Documentación del proyecto |
| `dataset_funcion_renal.csv` | Conjunto de datos de entrada |
| `misd.py` | Implementación de la arquitectura MISD |
| `mimd.py` | Implementación de la arquitectura MIMD |
| `simd.py` | Implementación de la arquitectura SIMD |
| `dashboard.py` | Aplicación visual desarrollada con Streamlit |
---


<p align="center">
  <strong>PROYECTO DE COMPUTACIÓN PARALELA · OPCIÓN 4</strong>
  <br>
  Python · MIMD · SIMD · MISD · Evaluación de la función renal
  <br><br>
  <sub>Procesamiento paralelo aplicado al análisis de datos bioquímicos.</sub>
</p>
