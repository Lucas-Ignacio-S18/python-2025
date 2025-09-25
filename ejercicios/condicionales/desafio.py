# Facturación del Servicio de Agua Potable
# El acceso al agua potable es un servicio esencial para hogares, comercios e industrias. Para garantizar un uso eficiente del recurso y establecer una estructura justa de costos, se han definido diferentes tarifas y ajustes según el consumo y el tipo de cliente.
# Este sistema de facturación contempla una tarifa base que incluye un cargo fijo y un costo variable por metro cúbico consumido. Además, se aplican bonificaciones y recargos dependiendo del consumo y la categoría del usuario. En algunos casos especiales, también pueden otorgarse descuentos adicionales.
# A continuación, se detallan las reglas del sistema de facturación y los cálculos necesarios para determinar el monto final a pagar.


# TARIFA BASE:
# Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
# El costo por metro cúbico (m³) de agua es de $200/m³.

# Bonificaciones y Recargos según tipo de cliente:

# Cliente Residencial:
# Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
# Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.

# Cliente Comercial:
# Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
# Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
# Si el consumo es menor a 50 m³, se aplica un recargo del 5%.

# Cliente Industrial:
# Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
# consumo.
# Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
# Si el consumo es menor a 200 m³, se aplica un recargo del 10%.

# Casos especiales:
# Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.

#En todos los casos, se aplica el IVA del 21% sobre el total.

# Requerimientos del programa:

# 1. Solicitar al usuario:
#   Cantidad de metros consumidos
#   Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.

# 2.Calcular:
#   Subtotal de consumo.
#   Bonificaciones, si corresponde
#   Recargos, si corresponde
#   Subtotal, con recargos y bonificaciones.
#   IVA aplicado (21%), si corresponde.
#   Total final a pagar.

# 3.Mostrar en pantalla el desglose de los cálculos.

#--------------------------------------------------------------------------
#1.
cargo_fijo = 7000
metros_cubicos = 200
iva = 0.21

#-------------Ingreso de datos-------------------
metros_consumidos = float(input("Ingrese la cantidad de metros que posee: "))
tipo_cliente = input("Es cliente residencial/comercial/industrial?: ")

#--------------------------------------------------------------------------

#2.
#subtotal de consumo
subtotal_consumo = metros_consumidos * metros_cubicos

#bonificaciones
bonificacion = 0

if tipo_cliente == "residencial":
    if metros_consumidos < 30:
        bonificacion = -(subtotal_consumo * 0.10)
    elif metros_consumidos > 80:
        bonificacion = subtotal_consumo * 0.15

elif tipo_cliente == "comercial":
    if metros_consumidos > 300:
        bonificacion = subtotal_consumo * 0.12
    elif metros_consumidos > 150:
        bonificacion = subtotal_consumo * 0.8
    elif metros_consumidos < 50:
        bonificacion = -(subtotal_consumo * 0.5)

elif tipo_cliente == "industrial":
    if metros_consumidos > 1000:
        bonificacion = subtotal_consumo * 0.30
    elif metros_consumidos > 500:
        bonificacion = subtotal_consumo * 0.20
    elif metros_consumidos < 200:
        bonificacion = -(subtotal_consumo * 0.10)

#CONTINUAR 
#MODIFICAR EL "bonificacion" y cambiar por dos variables,  "bonificacion" si le descuentan y "recargo" si es que le aumenta
#   Bonificaciones, si corresponde
#   Recargos, si corresponde

subtotal_final = subtotal_consumo + bonificacion

# Casos especiales:
if tipo_cliente == "residencial" and subtotal_final <= 35000:
    subtotal_final -= subtotal_final * 0.05

iva_aplicado = subtotal_final * iva

total_pagar = subtotal_final + iva_aplicado


#-----Salida----
#3.
print("\n--- DATOS DEL CLIENTE ---")
print(f"El cliente es {tipo_cliente}")
print(f"Los metros consumidos por el cliente son: {metros_consumidos} m")

print("\n---------------------------")

print("\n--- FACTURA ---")
print(f"Consumo (m³): {metros_consumidos}")
print(f"Subtotal por consumo: ${subtotal_consumo:.2f}")
print(f"Cargo fijo: ${cargo_fijo:.2f}")
print(f"Ajuste (bonificación/recargo): ${bonificacion:.2f}")
print(f"Subtotal con ajustes: ${subtotal_final:.2f}")
print(f"IVA (21%): ${iva_aplicado:.2f}")
print(f"TOTAL A PAGAR: ${total_pagar:.2f}")