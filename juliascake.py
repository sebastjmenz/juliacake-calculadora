import streamlit as st

st.title("🍰 JuliaCake Calculadora")

# --- Datos iniciales ---
nombre_torta = st.text_input("Nombre de la torta")
dolar_bcv = st.number_input("Precio del dólar BCV", min_value=0.0, step=0.01)
dolar_calle = st.number_input("Precio del dólar Calle", min_value=0.0, step=0.01)

ingredientes = ["Harina", "Azúcar", "Leche en polvo", "Mantequilla", "Cacao"]
datos = {}

st.header("🧾 Ingredientes")
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
    for ing, (precio_kilo, gramos) in datos.items():
        costo_total += (precio_kilo / 1000) * gramos

    # huevo
    if carton_huevos > 0:
        costo_huevo_unitario = carton_huevos / 30
        costo_total += costo_huevo_unitario * unidades_huevo

    # gastos adicionales
    costo_total += 1.5

    precio_sugerido = costo_total * 2

    st.success(f"**Costo total en $:** ${costo_total:.2f}")
    st.info(f"💲 Precio sugerido de venta: ${precio_sugerido:.2f}")
    st.write(f"💵 En Bs (BCV): {costo_total * dolar_bcv:.2f}")
    st.write(f"💵 En Bs (Calle): {costo_total * dolar_calle:.2f}")

