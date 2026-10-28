import streamlit as st
import pandas as pd
import plotly.express as px
from conexion import conectar_mysql


# ============================================================
# 1. CONFIGURACIÓN Y ESTILO
# ============================================================

st.set_page_config(
    page_title="Dashboard | Función renal",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1.7rem;
            padding-bottom: 2rem;
        }
        [data-testid="stMetric"] {
            background: rgba(128, 128, 128, 0.08);
            border: 1px solid rgba(128, 128, 128, 0.18);
            padding: 1rem 1.1rem;
            border-radius: 0.8rem;
        }
        .section-note {
            color: #777;
            font-size: 0.9rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🧬 Dashboard de procesamiento de función renal")
st.caption(
    "Computación paralela · Comparación de arquitecturas SIMD, MISD y MIMD"
)

st.info(
    "Este dashboard presenta resultados de una simulación académica. "
    "No constituye una herramienta de diagnóstico médico."
)


# ============================================================
# 2. CONSULTA DE LA BASE DE DATOS
# ============================================================

@st.cache_data(ttl=30, show_spinner="Consultando la base de datos...")
def cargar_datos():
    """Carga los registros de pacientes junto con sus resultados almacenados."""
    conexion = conectar_mysql()

    consulta = """
        SELECT
            rfr.id AS id_resultado,
            rp.id AS registro,
            rp.nombre,
            rp.apellido,
            rp.edad,
            rp.sexo,
            rp.altura_cm,
            rp.creatinina_mg_dl,
            rp.urea_mg_dl,
            rfr.arquitectura,
            rfr.tfge_ml_min_1_73_m2,
            rfr.creatinina_umol_l,
            rfr.urea_mmol_l,
            rfr.tiempo_microsegundos,
            rfr.fecha_procesamiento
        FROM registros_pacientes AS rp
        INNER JOIN resultados_funcion_renal AS rfr
            ON rp.id = rfr.registro_id
        ORDER BY rfr.fecha_procesamiento DESC, rfr.id DESC
    """

    try:
        cursor = conexion.cursor(dictionary=True)
        try:
            cursor.execute(consulta)
            filas = cursor.fetchall()
        finally:
            cursor.close()
    finally:
        conexion.close()

    df = pd.DataFrame(filas)
    if not df.empty:
        df["fecha_procesamiento"] = pd.to_datetime(
            df["fecha_procesamiento"], errors="coerce"
        )
        for columna in [
            "registro",
            "edad",
            "altura_cm",
            "creatinina_mg_dl",
            "urea_mg_dl",
            "tfge_ml_min_1_73_m2",
            "creatinina_umol_l",
            "urea_mmol_l",
            "tiempo_microsegundos",
        ]:
            df[columna] = pd.to_numeric(df[columna], errors="coerce")

    return df


try:
    datos = cargar_datos()
except Exception as error:
    st.error(f"No se pudieron cargar los datos desde MariaDB/MySQL: {error}")
    st.stop()

if datos.empty:
    st.warning(
        "La consulta no devolvió resultados. Comprueba que existan filas en "
        "`resultados_funcion_renal` y que estén relacionadas con "
        "`registros_pacientes`."
    )
    st.stop()


# ============================================================
# 3. FILTROS
# ============================================================

st.sidebar.title("Filtros")
st.sidebar.caption("Los filtros afectan a las métricas, los gráficos y la tabla.")

arquitecturas_disponibles = sorted(
    datos["arquitectura"].dropna().astype(str).unique().tolist()
)
arquitecturas_seleccionadas = st.sidebar.multiselect(
    "Arquitectura",
    options=arquitecturas_disponibles,
    default=arquitecturas_disponibles,
    help="Selecciona una o varias arquitecturas para comparar.",
)

ids_validos = datos["registro"].dropna()
if ids_validos.empty:
    st.error("No hay identificadores de paciente válidos en la consulta.")
    st.stop()

id_min = int(ids_validos.min())
id_max = int(ids_validos.max())

if id_min < id_max:
    rango_ids = st.sidebar.slider(
        "Rango de ID de paciente",
        min_value=id_min,
        max_value=id_max,
        value=(id_min, id_max),
    )
else:
    rango_ids = (id_min, id_max)
    st.sidebar.caption(f"ID de paciente disponible: {id_min}")

metricas = {
    "TFGe (mL/min/1.73 m²)": "tfge_ml_min_1_73_m2",
    "Creatinina (µmol/L)": "creatinina_umol_l",
    "Urea (mmol/L)": "urea_mmol_l",
}
metrica_elegida = st.sidebar.selectbox(
    "Resultado que se visualizará",
    options=list(metricas.keys()),
)
columna_metrica = metricas[metrica_elegida]

filtrados = datos[
    datos["arquitectura"].astype(str).isin(arquitecturas_seleccionadas)
    & datos["registro"].between(rango_ids[0], rango_ids[1], inclusive="both")
].copy()

if filtrados.empty:
    st.warning("No hay filas que coincidan con los filtros seleccionados.")
    st.stop()


# ============================================================
# 4. PREPARAR LOS RESULTADOS PARA VISUALIZACIÓN
# ============================================================

# En este proyecto, 0.0 puede indicar que una operación no se ejecutó
# para ese paciente. Se trata como valor no calculado en los gráficos.
# No se modifica ningún dato almacenado en la base de datos.
columnas_calculadas = [
    "tfge_ml_min_1_73_m2",
    "creatinina_umol_l",
    "urea_mmol_l",
]

datos_grafico = filtrados.copy()
for columna in columnas_calculadas:
    datos_grafico[columna] = datos_grafico[columna].where(
        datos_grafico[columna] > 0
    )

nombres_columnas = {
    "id_resultado": "ID resultado",
    "registro": "ID paciente",
    "nombre": "Nombre",
    "apellido": "Apellido",
    "edad": "Edad",
    "sexo": "Sexo",
    "altura_cm": "Altura (cm)",
    "creatinina_mg_dl": "Creatinina original (mg/dL)",
    "urea_mg_dl": "Urea original (mg/dL)",
    "arquitectura": "Arquitectura",
    "tfge_ml_min_1_73_m2": "TFGe (mL/min/1.73 m²)",
    "creatinina_umol_l": "Creatinina (µmol/L)",
    "urea_mmol_l": "Urea (mmol/L)",
    "tiempo_microsegundos": "Tiempo almacenado (µs)",
    "fecha_procesamiento": "Fecha de procesamiento",
}


# ============================================================
# 5. INDICADORES GENERALES
# ============================================================

pacientes_unicos = filtrados["registro"].nunique()
filas_resultado = len(filtrados)
arquitecturas_activas = filtrados["arquitectura"].nunique()
ultima_fecha = filtrados["fecha_procesamiento"].max()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Pacientes en el filtro", f"{pacientes_unicos:,}")
c2.metric("Filas de resultados", f"{filas_resultado:,}")
c3.metric("Arquitecturas", f"{arquitecturas_activas}")
c4.metric(
    "Última fecha registrada",
    ultima_fecha.strftime("%d/%m/%Y %H:%M")
    if pd.notna(ultima_fecha)
    else "No disponible",
)

st.divider()


# ============================================================
# 6. GRÁFICO DEL RESULTADO SELECCIONADO
# ============================================================

st.subheader(f"Resultados por paciente · {metrica_elegida}")

# Si hay varias ejecuciones para un mismo paciente y arquitectura,
# se resume la métrica calculada para evitar barras duplicadas.
resumen_metrica = datos_grafico[
    ["registro", "arquitectura", columna_metrica]
].dropna(subset=[columna_metrica])

resumen_metrica = resumen_metrica.groupby(
    ["registro", "arquitectura"], as_index=False
)[columna_metrica].mean()

if resumen_metrica.empty:
    st.warning(
        "No hay valores calculados positivos para la métrica seleccionada "
        "en los filtros actuales. Los valores 0.0 se omiten del gráfico "
        "porque pueden representar operaciones no ejecutadas."
    )
else:
    max_puntos = st.slider(
        "Máximo de pacientes mostrados en el gráfico",
        min_value=50,
        max_value=1000,
        value=300,
        step=50,
    )
    resumen_metrica = resumen_metrica.sort_values("registro").head(max_puntos)

    fig_resultados = px.bar(
        resumen_metrica,
        x="registro",
        y=columna_metrica,
        color="arquitectura",
        barmode="group",
        labels={
            "registro": "ID del paciente",
            columna_metrica: metrica_elegida,
            "arquitectura": "Arquitectura",
        },
        title=f"{metrica_elegida} por paciente y arquitectura",
        hover_data={columna_metrica: ":.4f"},
    )
    fig_resultados.update_layout(
        legend_title_text="Arquitectura",
        xaxis_title="ID del paciente",
        yaxis_title=metrica_elegida,
        hovermode="x unified",
        margin=dict(l=20, r=20, t=60, b=20),
    )
    st.plotly_chart(fig_resultados, use_container_width=True)

    st.caption(
        "Cuando hay varias filas para el mismo paciente y arquitectura, "
        "el gráfico muestra la media de los valores positivos almacenados. "
        "Los ceros se excluyen de la visualización porque pueden indicar "
        "una operación no realizada; la base de datos no se modifica."
    )


# ============================================================
# 7. PERFIL DE LOS PACIENTES
# ============================================================

st.subheader("Perfil de los pacientes")
col_edad, col_sexo = st.columns(2)

# Se usa una fila por paciente para que las ejecuciones repetidas no
# multipliquen artificialmente los conteos demográficos.
pacientes = filtrados.sort_values(
    ["fecha_procesamiento", "id_resultado"],
    ascending=[False, False],
).drop_duplicates(subset=["registro"])

with col_edad:
    edades = pacientes.dropna(subset=["edad"]).copy()
    if not edades.empty:
        edades["grupo_edad"] = pd.cut(
            edades["edad"],
            bins=[0, 17, 29, 44, 59, 120],
            labels=["0–17", "18–29", "30–44", "45–59", "60+"],
            include_lowest=True,
        )
        conteo_edades = (
            edades["grupo_edad"]
            .value_counts(sort=False)
            .rename_axis("Grupo de edad")
            .reset_index(name="Pacientes")
        )
        fig_edad = px.bar(
            conteo_edades,
            x="Grupo de edad",
            y="Pacientes",
            title="Distribución por grupo de edad",
            labels={"Pacientes": "Número de pacientes"},
        )
        fig_edad.update_layout(margin=dict(l=10, r=10, t=60, b=10))
        st.plotly_chart(fig_edad, use_container_width=True)
    else:
        st.info("No hay edades disponibles para los filtros actuales.")

with col_sexo:
    sexos = pacientes["sexo"].fillna("No especificado").astype(str).value_counts()
    if not sexos.empty:
        conteo_sexo = sexos.rename_axis("Sexo").reset_index(name="Pacientes")
        fig_sexo = px.pie(
            conteo_sexo,
            names="Sexo",
            values="Pacientes",
            hole=0.55,
            title="Distribución por sexo registrado",
        )
        fig_sexo.update_layout(margin=dict(l=10, r=10, t=60, b=10))
        st.plotly_chart(fig_sexo, use_container_width=True)
    else:
        st.info("No hay datos de sexo disponibles.")


# ============================================================
# 8. ANÁLISIS DE TIEMPOS
# ============================================================

st.subheader("Tiempos de procesamiento por arquitectura")

tiempos = filtrados[
    ["arquitectura", "tiempo_microsegundos"]
].dropna()

tiempos["tiempo_microsegundos"] = pd.to_numeric(
    tiempos["tiempo_microsegundos"], errors="coerce"
)
tiempos = tiempos[
    tiempos["tiempo_microsegundos"] >= 0
].drop_duplicates(
    subset=["arquitectura", "tiempo_microsegundos"]
)

if tiempos.empty:
    st.info("No hay tiempos válidos almacenados para los filtros actuales.")
else:
    fig_tiempos = px.box(
        tiempos,
        x="arquitectura",
        y="tiempo_microsegundos",
        color="arquitectura",
        points="all",
        labels={
            "arquitectura": "Arquitectura",
            "tiempo_microsegundos": "Tiempo almacenado (µs)",
        },
        title="Distribución de los valores de tiempo distintos guardados",
    )
    fig_tiempos.update_layout(
        showlegend=False,
        xaxis_title="Arquitectura",
        yaxis_title="Tiempo (microsegundos)",
        margin=dict(l=20, r=20, t=60, b=20),
    )
    st.plotly_chart(fig_tiempos, use_container_width=True)

st.warning(
    "Limitación de la base de datos: el tiempo total de una ejecución se "
    "guarda repetido en las filas de resultados y no existe una columna "
    "identificadora de ejecución. El gráfico elimina tiempos exactamente "
    "repetidos por arquitectura para reducir duplicaciones, pero no puede "
    "reconstruir con certeza cada ejecución ni sustituye una medición "
    "experimental registrada por separado."
)


# ============================================================
# 9. TABLA Y DESCARGA
# ============================================================

st.subheader("Resultados almacenados")
st.caption(
    "La tabla conserva las filas consultadas. Los valores originales de la "
    "base de datos no se alteran por los filtros ni por los gráficos."
)

columnas_tabla = [
    "id_resultado",
    "registro",
    "nombre",
    "apellido",
    "edad",
    "sexo",
    "altura_cm",
    "creatinina_mg_dl",
    "urea_mg_dl",
    "arquitectura",
    "tfge_ml_min_1_73_m2",
    "creatinina_umol_l",
    "urea_mmol_l",
    "tiempo_microsegundos",
    "fecha_procesamiento",
]

tabla = filtrados[columnas_tabla].rename(columns=nombres_columnas)

st.dataframe(
    tabla,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Fecha de procesamiento": st.column_config.DatetimeColumn(
            "Fecha de procesamiento",
            format="DD/MM/YYYY HH:mm:ss",
        ),
        "Tiempo almacenado (µs)": st.column_config.NumberColumn(
            "Tiempo almacenado (µs)",
            format="%.2f",
        ),
        "TFGe (mL/min/1.73 m²)": st.column_config.NumberColumn(
            "TFGe (mL/min/1.73 m²)",
            format="%.4f",
        ),
        "Creatinina (µmol/L)": st.column_config.NumberColumn(
            "Creatinina (µmol/L)",
            format="%.4f",
        ),
        "Urea (mmol/L)": st.column_config.NumberColumn(
            "Urea (mmol/L)",
            format="%.4f",
        ),
    },
)

csv_bytes = tabla.to_csv(index=False).encode("utf-8-sig")
st.download_button(
    label="⬇️ Descargar resultados filtrados (CSV)",
    data=csv_bytes,
    file_name="resultados_funcion_renal.csv",
    mime="text/csv",
)

st.caption(
    "Nota: este dashboard es una herramienta de visualización académica. "
    "Los resultados no deben utilizarse por sí solos para tomar decisiones clínicas."
)
