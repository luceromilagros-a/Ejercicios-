
# CAPTURA GENÉRICA Y MENSAJES DETALLADOS

try:
    resultado = 10 / 0
except Exception as e:
    print("Ocurrió un error:", e)
    print("Tipo de error:", type(e).__name__)
