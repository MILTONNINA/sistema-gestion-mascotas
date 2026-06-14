# Sistema de Gestión de Mascotas

### Datos del Estudiante
Nombre: Milton Camilo Ninasunta Oña
Asignatura: Programación orientada a objetos / POO

Descripción de los Programas Desarrollados

Este proyecto resuelve el mismo problema (registrar y mostrar los datos básicos de una mascota: Nombre, Especie y Edad) utilizando dos enfoques de desarrollo distintos:

1. Programa 1: Programación Tradicional (programacion_tradicional/tradicional.py)
   Funcionamiento: Se diseñó una solución estructurada que interactúa directamente con el usuario mediante la consola. Utiliza variables independientes para almacenar los datos capturados por teclado (input) y funciones específicas (registrar_mascota y mostrar_mascota) encargadas de procesar y estructurar la información sin la intervención de moldes lógicos o entidades abstractas.
   
2. Programa 2: Programación Orientada a Objetos (programacion_poo/)
   Funcionamiento: Se aplicó un enfoque modular dividido en dos archivos. En mascota.py se construyó la clase Mascota (molde abstracto) definiendo los atributos esenciales y comportamientos (mostrar_informacion y hacer_sonido). En main.py se importó esta clase para instanciar múltiples objetos independientes (mascota1 y mascota2), demostrando el control individual de los estados de cada objeto.

Reflexión: Diferencias entre la Programación Tradicional y la POO

Tras el desarrollo de ambas soluciones, se identificaron las siguientes diferencias conceptuales y prácticas fundamentales entre ambos paradigmas:

Organización y Acoplamiento: En la programación tradicional, los datos (variables) y las acciones (funciones) están separados; las funciones reciben los datos de forma externa, lo que puede volver el código difícil de mantener a gran escala. En cambio, la POO une de forma natural los datos y el comportamiento dentro de un mismo contenedor (el objeto), logrando un código más limpio, ordenado y fácil de entender.
Abstracción y Reutilización: La programación tradicional nos obliga a pensar en términos de "pasos a seguir" y procedimientos secuenciales. Por el contrario, la POO nos permite usar la abstracción para modelar conceptos del mundo real como entidades de software. Una vez que la clase Mascota está definida, crear diez o cien mascotas diferentes es sumamente sencillo y no requiere duplicar código, lo que eleva drásticamente la reutilización del software.
Modularidad: El enfoque de la POO facilita la separación de responsabilidades. Al aislar la clase en su propio archivo (mascota.py), cualquier cambio en la estructura interna de una mascota no altera el flujo principal del programa en main.py, una ventaja crítica que no se logra con la misma facilidad en el desarrollo tradicional estructurado.
