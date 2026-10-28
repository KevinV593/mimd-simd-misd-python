# Arquitecturas MIMD, SIMD y MISD con Python

Proyecto de Computación Paralela

### Opción 4
<img width="1206" height="129" alt="image" src="https://github.com/user-attachments/assets/cf8193a4-f0bb-416d-8419-9b7f541cadd0" />

## Presentación del tema

### Evauación de Función Renal


## Fórmulas

### 1. Tasa de filtración glomerular estimada (TFGe)

Ecuación de creatinina CKD-EPI (2021): https://www.kidney.org/es/ecuacion-de-creatinina-ckd-epi-2021

#### Fórmula:

Calcular la taza de filtración glomerular (eGFR, por sus siglas en inglés) =
142 * min(Scr/K estandarizado, 1)α * max(Scr/K estandarizado, 1) - 1.200 * 0.9938 × Edad * 1.012 [si es mujer]

K = 0.7 (mujeres) o 0.9 (hombres)
α = -0.241 (mujeres) o -0.302 (hombres)

Ecuación pediátrica bedside Schwartz
\[
\mathrm{TFGe} = 41.3 \times \frac{\text{talla (m)}}{\text{creatinina (mg/dL)}}
\]

#### Abreviaturas / Unidades
eGFR (taza de filtración glomerular estimada) = ml/min/1.73 m²

Scr (creatinina sérica) = mg/dL

K = 0.7 (mujeres) o 0.9 (hombres)

α = -0.241 (mujeres) o -0.302 (hombres)

min = indica el mínimo entre Scr/K o 1

max = indica el máximo de Scr/K o 1

### 2. Convertir creatinina de mg/dL a μmol/L

creatinina_umol = creatinina_mg_dl * 88.4;

- Objetivo del proyecto

- Dashboard

### 3. Convertir urea de mg/dL a mmol/L

urea_mmol_l = urea_mg_dl / 6.006;


## Base de Datos
Ver: [dataset_funcion_renal.csv](dataset_funcion_renal.csv)


# EJECTUAR
python mimd.py > salida_mimd.txt
sudo /opt/lampp/lampp start
python -m streamlit run dashboard_funcion_renal_mejorado.py

# Limpiar Base
DELETE FROM resultados_funcion_renal;
ALTER TABLE resultados_funcion_renal AUTO_INCREMENT = 1;
