

import time 
import sys 

def slowprint (texto, velocidad=0.03):
    """Imprime el texto letra por letra para dar efecto de transmisión de radar."""
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()
