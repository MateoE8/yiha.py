import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Calculadora de Rebajas", page_icon="🤑")

# Título y Descripción
st.title("Calculadora de Rebajas Profesional 🤑💵💶")
st.markdown("Bienvenido. Introduce tus datos para calcular tu rebaja.")
st.write("---")

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")
precio_original = st.sidebar.number_input(
    "Tu dinero ($)", 
    min_value=0.0, 
    max_value=1000.0, 
    value=50.0
)

porcentaje = st.sidebar.slider(
    "Tu descuento (%)", 
    min_value=1, 
    max_value=100, 
    value=50
)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular ahora"):
    
    # Cálculo del precio final
    precio_final = precio_original - (precio_original * porcentaje / 100)

    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="Tu valor final es:", value=f"${precio_final:.2f}")

    with col2:
        # Condiciones corregidas
        if porcentaje < 15:
            st.warning("Meh ✖✖✖")
            st.write("No es muy buena oferta. No es recomendable.")

        elif 15 <= porcentaje < 30:
            st.info("Bien 👍👍")
            st.write("Está bastante bien.")

        elif 30 <= porcentaje < 50:
            st.success("¡¡¡GENIAL!!! ✅✅")
            st.write("Muy buena oferta.")
            st.balloons()

        else:  # 50 o más
            st.error("🔥🔥🔥 CHOLLAZO 🔥🔥🔥")
            st.write("¡Qué oferta tan brutal!")
            st.balloons()
   
   
