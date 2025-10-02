# ==========================================
# Sistema de cálculo de costos Julia's Cake
# Con gastos variables y precio sugerido
# ==========================================

# Paso 1: Datos generales
nombre_torta = input("Ingrese el nombre de la torta: ")

# Tasas de cambio
dolar_bcv = float(input("Ingrese el precio actual del dólar (BCV): "))
dolar_calle = float(input("Ingrese el precio actual del dólar (calle): "))

# Lista de ingredientes (excepto huevos que es especial)
ingredientes = ["Harina", "Azúcar", "Leche en polvo", "Mantequilla", "Cacao"]

# Diccionarios para almacenar datos
precios = {}
cantidades_g = {}
costos_usd = {}

print("\n--- INGRESO DE DATOS DE INGREDIENTES ---")
print("Para cada ingrediente indique el precio en USD por kilo y luego los gramos utilizados.\n")

# Paso 2: Recolección de datos con bucle
for ing in ingredientes:
    precio = float(input(f"Precio de {ing} (USD/Kg): "))
    gramos = float(input(f"Cantidad de {ing} utilizada (gramos): "))
    
    precios[ing] = precio
    cantidades_g[ing] = gramos
    
    # Calcular costo en USD
    costo = (gramos / 1000) * precio
    costos_usd[ing] = costo
    print(f"--> Costo de {ing}: ${costo:.2f}\n")

# Paso 3: Huevos (manejo especial)
print("\n--- DATOS DE HUEVOS ---")
precio_carton = float(input("Precio del cartón de huevos (30 unidades) en USD: "))
cantidad_huevos = int(input("Cantidad de huevos utilizados: "))

precio_unitario_huevo = precio_carton / 30
costo_huevos = cantidad_huevos * precio_unitario_huevo
costos_usd["Huevos"] = costo_huevos

print(f"--> Costo de huevos: ${costo_huevos:.2f}")

# Paso 4: Gastos variables
gastos_variables = 1.5
print(f"\nSe agregan ${gastos_variables:.2f} de gastos variables (bicarbonato, vainilla, cartón, velas, etc.)")
costos_usd["Gastos Variables"] = gastos_variables

# Paso 5: Cálculo total con gastos
costo_total_usd = sum(costos_usd.values())

# Precio sugerido de venta (doble del costo)
precio_sugerido_usd = costo_total_usd * 2

# Conversión a bolívares
costo_total_bcv = costo_total_usd * dolar_bcv
costo_total_calle = costo_total_usd * dolar_calle

precio_sugerido_bcv = precio_sugerido_usd * dolar_bcv
precio_sugerido_calle = precio_sugerido_usd * dolar_calle

# Paso 6: Resultados finales
print("\n==========================================")
print(f"     COSTO DE FABRICACIÓN - {nombre_torta}")
print("==========================================")

for ing, costo in costos_usd.items():
    print(f"{ing}: ${costo:.2f}")

print("------------------------------------------")
print(f"Costo total (incluyendo gastos variables) en USD: ${costo_total_usd:.2f}")
print(f"Costo total en Bs (BCV): Bs {costo_total_bcv:.2f}")
print(f"Costo total en Bs (Calle): Bs {costo_total_calle:.2f}")

print("\n******** PRECIO SUGERIDO DE VENTA ********")
print(f"Precio sugerido de venta en USD: ${precio_sugerido_usd:.2f}")
print(f"Precio sugerido de venta en Bs (BCV): Bs {precio_sugerido_bcv:.2f}")
print(f"Precio sugerido de venta en Bs (Calle): Bs {precio_sugerido_calle:.2f}")
print("==========================================")
