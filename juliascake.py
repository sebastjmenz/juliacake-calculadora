import streamlit as st

st.title("🍰 JuliaCake - Calculadora de Costos")

# --- Datos iniciales ---
nombre_torta = st.text_input("Nombre de la torta")
dolar_bcv = st.number_input("💵 Precio del dólar BCV", min_value=0.0, step=0.01)
dolar_calle = st.number_input("💵 Precio del dólar Calle", min_value=0.0, step=0.01)

ingredientes = ["Harina", "Azúcar", "Leche en polvo", "Mantequilla", "Cacao"]
datos = {}

st.header("🧾 Ingredientes principales")
for ing in ingredientes:
    precio = st.number_input(f"Precio por kilo de {ing} ($)", min_value=0.0, step=0.01, key=f"{ing}_precio")
    gramos = st.number_input(f"Gramos usados de {ing}", min_value=0.0, step=1.0, key=f"{ing}_gramos")
    datos[ing] = (precio, gramos)

# Huevo
st.header("🥚 Huevo")
carton_huevos = st.number_input("Precio del cartón de 30 huevos ($)", min_value=0.0, step=0.01)
unidades_huevo = st.number_input("Unidades de huevo usadas", min_value=0, step=1)

# --- Cálculo ---
if st.button("Calcular costos"):
    costo_total = 0

    # Ingredientes
    for ing, (precio_kilo, gramos) in datos.items():
        costo_total += (precio_kilo / 1000) * gramos

    # Huevo
    if carton_huevos > 0:
        costo_huevo_unitario = carton_huevos / 30
        costo_total += costo_huevo_unitario * unidades_huevo

    # Gastos adicionales
    costo_total += 1.5

    # Precio sugerido
    precio_sugerido = costo_total * 2

    # Conversiones
    costo_bcv = costo_total * dolar_bcv
    costo_calle = costo_total * dolar_calle
    sugerido_bcv = precio_sugerido * dolar_bcv
    sugerido_calle = precio_sugerido * dolar_calle

    # --- Resultados ---
    st.subheader(f"📊 Resultados para la torta: {nombre_torta}")

    st.info(f"💲 **Costo total en dólares:** ${costo_total:.2f}")
    st.write(f"💵 **Costo total en Bs (BCV):** {costo_bcv:,.2f}")
    st.write(f"💵 **Costo total en Bs (Calle):** {costo_calle:,.2f}")

    st.success(f"🏷️ **Precio sugerido de venta en dólares:** ${precio_sugerido:.2f}")
    st.write(f"🏷️ **Precio sugerido en Bs (BCV):** {sugerido_bcv:,.2f}")
    st.write(f"🏷️ **Precio sugerido en Bs (Calle):** {sugerido_calle:,.2f}")

