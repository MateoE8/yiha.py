import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Salud 3º ESO", page_icon="🏥")

# Título y Descripción
st.title(" Calculadora de Rebajas Profesional 🤑💵💶")
st.markdown("Bienvenido. Introduce tus datos para calcular tu rebaja.")
st.write("---") # Línea separadora

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")
precio_original = st.sidebar.number_input(" Tu dinero ($)", min_value=0, max_value=200, value=50)
porcentaje = st.sidebar.slider("Tu descuento (%)", 1, 100, 50)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular ahora"):
    
    # Fórmula Matemática: Peso entre altura al cuadrado
    precio_final=precio_original-precio_original*porcentaje/100
    
    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)
    
    with col1:
        # Usamos metric para que el número se vea grande
        st.metric(label="Tu valor final es:", value=f"{precio_final:.2f}")
        
    with col2:
        # Usamos condicionales (if/elif/else) para el diagnóstico
        if porcentaje < 15:
            st.warning("Meh✖✖✖")
            st.write("No es muy buena oferta no es recomendable.")
    
        elif 30 <= porcentaje < 15:
            st.success("Bien👍👍")
            st.write("Bien")
            st.balloons() # ¡Premio!
        elif 50 <= porcentaje < 30:
            st.warning("!!!GENIAL!!!")
            st.write("Esta muy bien✅✅.")
            st.balloons()
        else:
            st.error("🔥🔥🔥CHOLLAZO🔥🔥🔥")
            st.write("Que oferta tan brutal!!!.")
            st.balloons()
            
   
   
