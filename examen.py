import streamlit as st

# 1. EL ARCHIVADOR (Base de datos de preguntas)
preguntas = [
    {
        "texto": "¿Cuál es el colegio en el que estamos?",
        "opciones": ["Retamar", "Tajamar", "Santa Maria del Pilar", "Alameda International School"],
        "correcta": "Tajamar"
    },
    {
        "texto": "¿Como se llama el director de el colegio Tajamar?",
        "opciones": ["Jaime Perez", "Daniel Riquelme", "Don Rodrigo"],
        "correcta": "Jaime Perez"
    },
    {
        "texto": "¿En que año se fundo Tajamar?",
        "opciones": ["1973", "1960", "1966", "1958"],
        "correcta": "1958"
    },
    {
        "texto": "¿Cuantos cursos hay en la ESO en Tajamar?",
        "opciones": ["4", "3", "5", "6"],
        "correcta": "4"
    },
    {
        "texto": "¿Tajamar es un colegio catolico?",
        "opciones": ["SI", "NO"],
        "correcta": "SI"
    },
    {
        "texto": "¿Cuantas veces Tajamar ha sido premiado?",
        "opciones": ["12", "8", "10", "NUNCA"],
        "correcta": "10"
    },
    {
        "texto": "¿Donde esta ubicado Tajamar?",
        "opciones": ["Villaverde", "Nueva Numancia", "Ensanche de Vallecas", "Pio Felipe"],
        "correcta": "Pio Felipe"
    },
    {
        "texto": "¿Tajamar tiene comedor?",
        "opciones": ["NO", "SI", "NO LO SE", "PROBABLEMENTE"],
        "correcta": "SI"
    },
    {
        "texto": "¿La comida en Tajamar es buena?",
        "opciones": ["Depende del dia pero no", "MEH", "SI", "Claro que NO"],
        "correcta": "Depende del dia pero no"
    }
]

# Configuración visual
st.title("Mi primer examen en streamlit playground 😎")
st.write("Responde a las preguntas y pulsa el botón al final para saber tu nota.")

with st.form("quiz_form"):

    respuestas_usuario = []

    for pregunta in preguntas:
        st.subheader(pregunta["texto"])
        eleccion = st.radio("Elige una opción:", pregunta["opciones"], key=pregunta["texto"])
        respuestas_usuario.append(eleccion)
        st.write("---")

    boton_enviar = st.form_submit_button("Entregar Examen")

# Corrección
if boton_enviar:
    aciertos = 0
    total = len(preguntas)

    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos += 1

    nota = (aciertos / total) * 10
    nota = round(nota, 2)  # Máximo 2 decimales

    st.divider()
    st.header(f"Resultado final: {nota} / 10")

    if nota < 5:
        st.error(f"Has sacado un {nota}. ¡Toca estudiar un poco más!")

    elif 5 <= nota < 6:
        st.warning(f"Aprobado Has sacado un {nota}.")

    elif 6 <= nota < 7:
        st.success(f"Bien 👍 Has sacado un {nota}.")

    elif 7 <= nota < 9:
        st.success(f"¡Notable! 👏 Has sacado un {nota}.")
        st.balloons()

    elif 9 <= nota < 10:
        st.success(f"SOBRESALIENTE!!! 🔥 Has sacado un {nota}.")
        st.balloons()

    elif nota == 10:
        st.success("ERES INCREIBLE! 🏆🔥")
        st.balloons()
