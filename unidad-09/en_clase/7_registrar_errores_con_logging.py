
# REGISTRO DE ERRORES CON EL MÓDULO logging

import logging

# Configuración básica del logging
logging.basicConfig(filename='app.log', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    logging.error(f"ZeroDivisionError: {e}", exc_info=True)
    print("Un error ha sido registrado en app.log")
