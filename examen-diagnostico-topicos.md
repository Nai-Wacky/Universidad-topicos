# Examen diagnostico - TOPICOS

Nombre: Ricardo Hernández Urbina  
Fecha: 27/08/2026

Instrucciones: Responde de manera clara y concisa a cada una de las siguientes preguntas abiertas. El propósito de esta evaluación es medir tus conocimientos previos en Ingeniería de Software.

1. Metodologías: ¿Cuál es la diferencia principal entre una metodología de desarrollo tradicional (como Cascada) y una metodología ágil (como Scrum) frente a los cambios en los requisitos?

.

2. Requerimientos: Explica la diferencia entre requerimientos funcionales y no funcionales, dando un ejemplo de cada uno aplicable a una plataforma web

Los requerimientos funcionales son aquellos que el cliente nos pide, y los no funcionales son todo aquello que implica agregarse para que los requerimientos funcionales sean posibles.

3. Arquitectura: Describe el modelo Cliente-Servidor y explica brevemente cómo se comunican el frontend y el backend en una aplicación web moderna

Este modelo es aquel en la que la computadora del cliente ejecuta una parte de la aplicación (El frontend) y a su ves se comunica con otra computadora la cual ejecuta todas operaciones o procesos (El backend), pongamos de ejemplo a youtube, en tu computadora se esta ejecutando el frontend, básicamente procesando como se ve la pagina y recibiendo datos que se solicitan al servidor, ahora bien, el servidor seria aquel que se encarga de enviar y recibir datos, como enviar el video que estas viendo, cargar los comentarios, o mostrar todos las playlist que tienes, a su ves este se encarga de registrar los comentarios que haces, los videos que ves, guardar videos en tus playlist, etc. El servidor ejecuta la app, y tu, el como se ve.

4. Bases de Datos: ¿En qué escenarios recomendarías utilizar una base de datos relacional (SQL) frente a una no relacional (NoSQL) para el almacenamiento de datos en una aplicación?

La base de datos relacional la recomendaría cuando los datos están etiquetados (por ejemplo, ID, fecha, nombre, monto, cantidad, etc), y la relacional cuando no lo están.

5. APIs: ¿Qué es una API REST y qué papel fundamental juega en la integración entre una aplicación móvil y los servidores (backend)?

Una API es aquella a la que nosotros nos comunicamos, a la que solicitamos datos y nosotros recibimos, su papal es fundamental, ya que, sin ella no habría forma de comunicarnos de forma segura con el servidor (si es que se crear correctamente).

6. Control de Versiones: Explica la importancia de utilizar Git en un equipo de desarrollo de software y describe brevemente qué es un "merge conflict" (conflicto de fusión).

Git es una herramienta fundamental para control de versiones, con ella no solo sabemos quien hizo los cambios, pero también que cambio, si bien esto lo podrías rastrear nosotros mismo, el tener un sistema que ya lo haga vuelve las cosas mucho más fáciles.

Un merge conflict sucede cuando alguien hace un cambio en el código en el tu estas trabajando, por ejemplo, digamos que trabajas en la version 1.0 del código en el archivo home.js, y otro persona hace cambios a ese archivo y en la misma versión que tu; el sube sus cambios como la version 1.1 , y ahora tu quieres los tuyos, pero no puedes; esto sucede porque hay un merge conflict, el sucede por que ahora tu estas trabajando en una version anterior (version 1.0) a la más actual (version 1.1), y para arreglar esto debes descargar la version más reciente y hacer tus cambios ahí.

7. Pruebas: ¿Qué son las pruebas unitarias (unit testing) y por qué son cruciales para asegurar la calidad del software antes de su paso a producción?

Las pruebas unitarias son aquellas en las que pones a prueba una pequeña parte del código, esto es crucial, ya que permite evaluar si esa parte del código funciona correctamente

8. POO: Define los conceptos de encapsulamiento y polimorfismo de la Programación Orientada a Objetos, y menciona cómo ayudan a crear un código más mantenible

El polimorfismo lo podemos definir como aquellas variables las cuales se pueden comportar como varias variables de diferentes tipos, esto ayuda a ahorrar líneas de código, por lo que hace más fácil la tarea de encontrar errores.

9. Patrones de Diseño: ¿Qué es el patrón de arquitectura Modelo-Vista-Controlador (MVC) y cómo ayuda a organizar el código en el desarrollo de software?

.

10. Seguridad: Explica la diferencia técnica entre "autenticación" y"autorización" en el contexto de seguridad de una aplicación

Autenticación: verificar que el usuarios es quien dice ser  
Autorización: verificar que el usuario tiene los permisos que dice tener
