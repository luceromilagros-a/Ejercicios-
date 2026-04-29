
# MALA PRÁCTICA: "Swallowing Exceptions"

# ❌ Evita esto:
try:
    resultado = 10 / 0
except:
    pass  # Silencia el error sin manejarlo

# ✅ Buena práctica: capturar excepción específica y manejarla
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print("Se detectó un error de división:", e)
