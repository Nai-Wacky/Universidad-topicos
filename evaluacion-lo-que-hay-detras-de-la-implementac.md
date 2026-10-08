---
# yaml-language-server: $schema=schemas\page.schema.json
Object type:
    - Page
Creation date: "2026-10-08T14:13:40Z"
Created by:
    - 'Richard '
Emoji: "\U0001F4DC"
id: bafyreigrooyeskle7yvx7tbe5j3vsj2ouzobib7akc27k36sctixgeqd7q
---
# Evaluacion Lo que hay detras de la implementacion- TOPICOS   
Nombre: Ricardo Hernández Urbina   
Matricula: 22121304   
   
## A — Entorno virtual, proyecto y contenedor (15 puntos)   
A1 = Ana: Un docker es necesario si queremos eliminar el "Funciona en mi compu" y también para un entorno de trabajo más limpio y, si bien el usar un docker podría eliminar la necesidad de un venv ya que las dependencias ya estarían dentro del docker estariamos descartando las funciones que no ofrece el venv y que además el venv hace aun más limpio el flujo de trabajo. Luis: Si bien usar el entorno aísla el tener que instalar dependencias en la maquina local, el usar runserver no ayuda en nada para solucionar el problema de que llegue más, ya que este en un servidor local que usa para desarrollo y no esta pensado para producción y, además, el crear más servidores no escala la aplicación, ya que se sigue usando los mismo recursos, en todo caso haría más lento la maquina por que ahora cada servidor puede usar menos recursos.   
   
A2 = a) No perdió código, ya que este esta fuera de la carpeta venv.   
b) Lo único que necesita es crear el entorno de nuevo usando el archivo requirements.txt, este archivo ya tiene escrito las dependencias que ellos necesitan para correr el codigo.   
c) Activar el entorno no instala python en la computadora, lo que hace es modificar la variable de entorno path temporalmente en la sesión de la terminal, es por eso que tiene que activar cada vez que iniciamos una nueva terminal.   
   
A3 = La app/ existe únicamente en el docker y se establece como la carpeta de trabajo por el WORKDIR, y el COPY solo hace una copia del proyecto en dicha carpeta app/.   
VENV: Evita que se generen problemas de incompatibilidad, ya que las dependencias que estan en ese entorno se compilan para la maquina en la que esta corriendo, por lo que si cambiamos de maquina es probable que nos generé errores.   
SQLITE: Esto podría evitar que filtren datos que se usan en las pruebas de desarrollo hacia producción, o en caso de que se use una copia de los datos reales, esto evita que dichos datos  se filtren una vez se suba el codigo a un repositorio.   
   
## B — El backend entrega datos (15 puntos)   
B1 = Al lógica de negocio en el front creara duplicación de código ya que dicha lógica se tendrá que escribir en el lenguaje de la app móvil.    
Si tenemos un buen backend, eso significa que todo lo que necesitamos que la app haga (logica de negocio) esta ahí y solo entrega datos al front que debe reprentar, por lo que podemos cambiarlo sin generar problemas. Lo único que entrega el back son datos que el front solo tiene que representar.   
   
   
