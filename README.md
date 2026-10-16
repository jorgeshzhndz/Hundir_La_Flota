# ⚓ Hundir la Flota en Python

Un clásico juego de **Hundir la Flota** para la terminal de comandos desarrollado en Python. Enfréntate a una Inteligencia Artificial con múltiples niveles de dificultad, lógica de disparo adaptativa y efectos visuales de radar.

## 🎮 Características principales

* **Niveles de dificultad de la CPU**:
  * **Easy (Fácil):** Disparos completamente aleatorios por todo el tablero.
  * **Medium (Medio):** Dispara de forma aleatoria, pero si detecta un barco enemigo (`❎`), busca estratégicamente en las casillas adyacentes para hundirlo.
  * **Hard (Difícil):** Aplica un algoritmo de patrón en ajedrez (par/impar) para cubrir el tablero de forma óptima en menos movimientos y persigue los barcos adyacentes cuando impacta. Debido a que el barco más pequeño ocupa 2 casillas, la CPU optimiza sus disparos aplicando una máscara de paridad `(fila + columna) % 2 == paridad`. Esto le permite encontrar barcos reduciendo casi a la mitad las casillas a explorar antes de pasar al modo de rastreo adyacente.
---
* **Generación de tablero inteligente:** Posicionamiento aleatorio de flotas garantizando una distancia de seguridad alrededor de cada barco (evita barcos pegados).
* **Interfaz en terminal mejorada:**
  * Impresión progresiva estilo radar con retardos temporales.
  * Representación visual del estado del tablero mediante emojis.
  * Resumen de vidas de ambas flotas en tiempo real.

## Leyenda del Tablero

| Icono | Descripción | 
| ----- | ----- | 
| ⬜ | Casilla de agua no descubierta | 
| ⛵ | Tu barco (solo visible en tu tablero) | 
| 💧 | Disparo fallido (Agua) | 
| ❎ | Impacto en un barco (Tocado) | 
| 💀 | Barco completamente destruido (Hundido) | 

## 📁 Estructura del Proyecto

```text
.
├── main.py     # Flujo principal del juego y bucle de turnos
├── bot.py      # Lógica e inteligencia artificial de la CPU (Easy, Medium, Hard)
├── utils.py    # Generación de tableros, colocación de barcos, disparos y reglas
└── visual.py   # Efectos de impresión progresiva (slowprint) y formateo en consola
```
### Instalación

1. Clona este repositorio en tu equipo local:
   ```bash
   git clone [https://github.com/tu-usuario/hundir-la-flota.git](https://github.com/tu-usuario/hundir-la-flota.git)
   cd hundir-la-flota
   ```

2. Instala la dependencia requerida (`numpy`):
   ```bash
   pip install numpy
   ```

---

## 🕹️ Cómo Jugar

Ejecuta el archivo principal desde tu terminal:

```bash
python main.py
```

1. **Selecciona la dificultad:** Elige entre `easy`, `medium` o `hard`.
2. **Realiza tu disparo:** Introduce la **fila** (0 a 9) y la **columna** (0 a 9) donde quieras apuntar.
3. **Turno de la CPU:** La máquina responderá con su disparo según el nivel elegido.
4. **Victoria:** ¡El primer jugador en reducir las 16 vidas de la flota enemiga a 0 gana la batalla!



