# Sistema de Gestión de Mascotas

Este repositorio contiene la resolución de la actividad académica diseñada para comparar y analizar las diferencias prácticas entre dos paradigmas de desarrollo de software: la **Programación Tradicional** y la **Programación Orientada a Objetos (POO)** utilizando Python.

## Estructura del Repositorio

* `programacion_tradicional/`: Contiene la solución estructurada mediante funciones y variables globales/locales, donde los datos se ingresan de forma dinámica por consola (`tradicional.py`).
* `programacion_poo/`: Contiene la solución modular en POO separada en la definición del molde (`mascota.py`) y la ejecución/creación de instancias (`main.py`).

## Conceptos de POO Evidenciados
1. **Clase:** Plantilla base (`Mascota`) que define la estructura común que compartirán todas las mascotas creadas.
2. **Atributos:** Características integradas en el objeto (`nombre`, `especie`, `edad`).
3. **Métodos:** Acciones integradas que los objetos pueden realizar (`mostrar_informacion()`, `hacer_sonido()`).
4. **Abstracción:** Reducción del concepto del mundo real de una mascota a solo las propiedades críticas necesarias para este software específico.
5. **Objeto/Instancia:** Elementos individuales con sus propios valores únicos generados a partir de la clase (`mascota1` y `mascota2`).