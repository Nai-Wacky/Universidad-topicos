---
# yaml-language-server: $schema=schemas\materias.schema.json
Object type:
    - Materias
Tag:
    - Semestre-8
Creation date: "2026-08-24T14:03:05Z"
Created by:
    - 'Richard '
Emoji: "\U0001F468‍\U0001F4BB"
id: bafyreierznw74hxjxzuqn5hkmn3ntq7jorbgiylww33jylxm4vwonmirvm
---
# Topicos   
Juan Eduardo Alcaraz    
# Evaluación    
Examen 50% (Pueden ser sorpresa)   
Proyectos 50% (En caso de no haber examen, el proyecto valdrá 100%)   
   
Crear un repositorio donde subiremos los proyectos/trabajos/practicas.   
Hará preguntas sobre el proyecto, y si no sabemos "ya caminamos".   
Tenemos un plazo de un mes para entregar el proyecto, la fecha de inicio es la misma fecha en la que dejo el proyecto. Después de ese plazo, la máxima calificación será de 70.   
   
26/08/26   
Patrones de diseño.   
Son patrones que nos sirven para resolver problemas, cada patron fue creado para resolver un cierto tipo de problema.   
   
Acertijos   
  Acertijo 1   
  Hay n focos apagados e n pasadas. En la pasada k (k = 1…n) se conmutan exactamente los múltiplos de k.   
  Tres preguntas, sin armar la matriz de nxn.   
  1. Si n = 1,000,000 ¿Cuantos focos quedan encendidos?   
  2. Cual es el segundo mayor numero de foco que queda encendido?   
  3. Formula del número de focos encendidos para un n cualqiera   
   
  Dos ciclos anidados para n=10^n no caben en el cuaderno por eso no existe el acertijo.   
     
  Acertijo 2   
  Un coche tapa un cajon:   
  16 \| 06 \| 68 \| 88 \| [coche] \| 98   
  ¿Que numero de dos dígitos está debajo del coche?   
  No es sucesión aritmética, ni geométrica, ni Fibonacci. Si salió 89, 96 o 108, esa es la trampa.    
     
  Acertijo 3   
  Dos trenes salen al mismo tiempo uno hacia el otro. Distancia inicial: 240km. Cada uno va a 60 km/h. Una mosca vuela a 90 km/h desde el frente del primer tren; llega al segundo, se da la vuelta, llega al primero, se da la vuelta… hasta que los trenes chocan y la aplastan.   
  ¿Cuantos kilómetros recorre la mosca?   
  La fuerza bruta es sumar infinitos tramos cada vez más cortos. Hay una forma de escribir esa seria.   
   
   
# 31/08/26   
Investigar 20 leguajes de programación con su respectivo paradigma (y su patron de diseño). Y hacer un análisis de los lenguajes que generen un problema o que les valga gorro un cierto tipo de patron de diseño. Hacerlo en tipo comparativa.   
|           |       Lenguaje   <br> |                                         Paradigmas principales   <br> |                                                                         Patrones que favorece   <br> |                                                                                                                                                                                                                                             Patrones que puede volver innecesarios, complicar o debilitar   <br> |
|:----------|:----------------------|:----------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1   <br> |       **Java**   <br> |                     Orientado a objetos, imperativo, funcional   <br> |                   **Factory, Strategy, Observer, Command, Template Method, Abstract Factory**   <br> |                                                                                                             `Singleton` puede ser problemático por estado global; lambdas reducen la necesidad de **Strategy/Command** en casos simples. Mucho boilerplate puede hacer pesados los patrones creacionales.   <br> |
|  2   <br> |         **C#**   <br> |                         OO, imperativo, funcional, concurrente   <br> |                                **Dependency Injection, Strategy, Observer, Factory, Command**   <br> |                                                                                                                                                                    Delegates/lambdas pueden reemplazar **Strategy, Command y Observer** sencillos. `Singleton` se puede sustituir fácilmente mediante DI.   <br> |
|  3   <br> |        **C++**   <br> |            Multiparadigma: OO, genérico, funcional, imperativo   <br> |                                        **RAII**, Strategy, Factory, Adapter, Observer, Policy   <br> |                                                       Templates y programación genérica pueden reemplazar **Strategy/Factory** en ciertos casos. RAII reduce la necesidad de patrones relacionados con gestión manual de recursos. `Singleton` suele generar problemas con estado global y ciclo de vida.   <br> |
|  4   <br> |     **Python**   <br> |            Multiparadigma: OO, imperativo, funcional, dinámico   <br> |                                           **Strategy, Factory, Decorator, Adapter, Iterator**   <br> |                                                                                                Duck typing reduce la necesidad de **Adapter**. Funciones de primera clase/lambdas reducen **Strategy y Command**. Decoradores del lenguaje hacen que el patrón **Decorator** sea particularmente natural.   <br> |
|  5   <br> | **JavaScript**   <br> | Multiparadigma, funcional, OO basado en prototipos, imperativo   <br> |                                **Module, Factory, Observer, Strategy, Decorator, Middleware**   <br> |                                                             Closures y funciones de primera clase pueden reemplazar **Strategy, Command y Factory**. Módulos ES reducen la necesidad del patrón **Module** tradicional. Prototipos hacen menos natural parte del enfoque clásico de **Abstract Factory**.   <br> |
|  6   <br> | **TypeScript**   <br> |                    OO, funcional, estructurado, multiparadigma   <br> |                               **Strategy, Factory, Adapter, Dependency Injection, Decorator**   <br> |                                                           Tipado estructural puede reducir la necesidad de **Adapter**. Union types y funciones pueden reemplazar jerarquías complejas y algunos usos de **Visitor**. Los decorators no siempre justifican implementar Decorator como estructura clásica.   <br> |
|  7   <br> |         **Go**   <br> |                          Imperativo, concurrente, estructurado   <br> |                               **Strategy, Adapter, Decorator, Factory, Dependency Injection**   <br> |    Interfaces pequeñas y funciones de primera clase reducen **Abstract Factory, Strategy y Template Method**. La ausencia de herencia elimina/reduce patrones basados en jerarquías como **Template Method**. No existe excepción tradicional, por lo que patrones de manejo de errores cambian bastante.   <br> |
|  8   <br> |       **Rust**   <br> |                   Imperativo, funcional, concurrente, sistemas   <br> |                                               **Strategy, State, Builder, Iterator, Visitor**   <br> |                           Traits, enums y pattern matching pueden reemplazar **Factory, State, Visitor y Strategy** clásicos. Ownership/borrowing hace innecesarios varios patrones utilizados para controlar manualmente la memoria. `Singleton` global es considerablemente más restringido/complicado.   <br> |
|  9   <br> |     **Kotlin**   <br> |                                                 OO + funcional   <br> |                                               **Builder, Strategy, Factory, Observer, State**   <br> |                                                                       `data class`, funciones de extensión, lambdas, null-safety y sealed classes pueden eliminar bastante boilerplate. **Builder** suele ser innecesario para objetos simples. **Singleton** tiene soporte idiomático mediante `object`.   <br> |
| 10   <br> |      **Swift**   <br> |                    OO/protocol-oriented, funcional, imperativo   <br> |                                               **Strategy, Factory, Observer, Builder, State**   <br> |                                                                                    Protocol extensions, closures y enums pueden sustituir **Strategy, State y Template Method** clásicos. Property wrappers reducen algunos usos de **Decorator**. ARC elimina patrones explícitos de gestión de memoria.   <br> |
| 11   <br> |       **Ruby**   <br> |                                        OO, funcional, dinámico   <br> |                                   **Decorator, Strategy, Template Method, Observer, Factory**   <br> |                                      Metaprogramación, bloques y duck typing reducen la necesidad de muchos patrones GoF. **Adapter** puede ser trivial mediante métodos dinámicos. **Singleton** existe directamente como mecanismo del lenguaje/librería, aunque sigue teniendo problemas conceptuales.   <br> |
| 12   <br> |        **PHP**   <br> |                                      Imperativo, OO, funcional   <br> |                             **Factory, Strategy, Repository, Dependency Injection, Observer**   <br> |                                            Closures reducen algunos usos de **Strategy/Command**. Frameworks como Symfony/Laravel hacen que DI, Repository, Facade, etc. sean muy comunes, pero también pueden convertir ciertos patrones en convenciones del framework más que necesidades del lenguaje.   <br> |
| 13   <br> |          **C**   <br> |                           Imperativo, estructurado, procedural   <br> |                     **State, Strategy, Factory, Facade, Observer** mediante funciones/structs   <br> |                                                                                             La ausencia de OO hace que patrones como **Decorator, Template Method, Abstract Factory** sean más difíciles y verbosos. Muchos patrones GoF deben implementarse manualmente con structs y function pointers.   <br> |
| 14   <br> |    **Haskell**   <br> |                              Funcional puro, declarativo, lazy   <br> |                  **Strategy, State, Iterator, Interpreter, Visitor** mediante funciones/tipos   <br> |                                                                           Inmutabilidad y funciones de primera clase reducen enormemente la necesidad de **Singleton, Observer, Command, Strategy y Builder** tradicionales. Muchos patrones GoF de OO directamente dejan de ser la abstracción adecuada.   <br> |
| 15   <br> |      **Scala**   <br> |                                                 OO + funcional   <br> |                                **Strategy, Factory, Observer, Interpreter, Visitor, Adapter**   <br> |                                                                                                  Pattern matching, funciones, traits y ADTs pueden reemplazar **Visitor, State, Strategy y Factory** clásicos. La combinación OO/FP puede hacer que algunos patrones GoF sean innecesariamente complejos.   <br> |
| 16   <br> |         **F#**   <br> |                                      Funcional, OO, imperativo   <br> | **Strategy, State, Interpreter, Pipeline, Visitor** mediante funciones y discriminated unions   <br> |                                                                                              Funciones de primera clase y discriminated unions hacen que **Visitor, Command, Strategy y State** clásicos pierdan mucha utilidad. Inmutabilidad reduce la necesidad de patrones basados en estado mutable.   <br> |
| 17   <br> |     **Elixir**   <br> |                            Funcional, concurrente, distribuido   <br> |                                **Pipeline, Strategy, State, Observer** mediante funciones/OTP   <br> |                                                                                             El modelo Actor/OTP hace que patrones como **Singleton, Observer y Command** tradicionales sean poco apropiados. Supervisors y GenServers sustituyen muchas arquitecturas/patrones que serían manuales en OO.   <br> |
| 18   <br> |     **Erlang**   <br> |                            Funcional, concurrente, distribuido   <br> |                                                  **Actor model, Supervisor, Pipeline, State**   <br> |                                                                                          OTP vuelve innecesarias muchas implementaciones manuales de **Observer, State, Singleton y Command**. La concurrencia basada en procesos cambia radicalmente la utilidad de patrones clásicos de sincronización.   <br> |
| 19   <br> |       **Dart**   <br> |                                      OO, funcional, imperativo   <br> |                                           **Builder, Factory, Strategy, Observer, Singleton**   <br> |                                                                                      Null-safety, funciones de primera clase y mixins reducen ciertos usos de **Strategy, Adapter y Template Method**. `factory constructors` hacen que algunas implementaciones de **Factory** sean mucho más sencillas.   <br> |

   
# 02/09/26   
Hacer misión 1 y 2 del apartado de apuntes.   
## Misión 1   
Enuncie **seis** problemas distintos del relato (un renglón cada uno). Para cada uno indique:   
- la **capa** (presentación, políticas transversales, aplicación/dominio, datos, integración);   
- el **patrón** (o la pareja de patrones) que corresponde;   
- **por qué ese** y no el vecino más fácil de confundir (por ejemplo Adapter frente a Facade, Observer frente a Unit of Work);   
- **cuándo no** aplicaría, aunque el nombre «quede bonito».   
   
Entregable: una tabla de seis filas. El portal **no** puede aparecer como «es MVC» ni como «es hexagonal».   
   
|                                                                           **Problema**   <br> |                 **Capa**   <br> |             **Patron**    <br> | **Por que ese**   <br> | **Cuando no**   <br> |
|:----------------------------------------------------------------------------------------------|:--------------------------------|:-------------------------------|:-----------------------|:---------------------|
|   Varios bloques duplicados a lo largo de 40 archivos (Sesión, bitácora y encabezados)   <br> |  Políticas transversales   <br> | Chain of Responsibility   <br> |                        |                      |
|                                              El switch de pago.php tiene 200 de codigo   <br> |              Integración   <br> |                Strategy   <br> |                        |                      |
|                                  Duplicación de consultas de SQL con diferente formato   <br> |                    Datos   <br> |              Repository   <br> |                        |                      |
|                               Fallos en el registro del correo y duplicación de cargos   <br> |     Aplicación / Dominio   <br> |            Unit of Work   <br> |                        |                      |
|                                      Doce peticiones para pintar la pantalla de inicio   <br> |     Presentación cliente   <br> |                     BFF   <br> |                        |                      |
|                                       Servicio de banco y CURP se caen con regularidad   <br> |              Integración   <br> |         Circuit Breaker   <br> |                        |                      |

## Misión 2   
Siga el caso de uso **pagar la inscripción** desde el clic (o desde `POST`) hasta persistir y notificar. Liste, **en orden**, las estructuras que atraviesa la petición. Para cada paso: qué objeto o mecanismo es (enrutador, filtro, servicio, repositorio…) y **qué patrón** está realizando.   
Apóyese en el esquema de composición a lo largo de una petición HTTP del apartado web. No invente una capa vacía que solo delega.   
   
1. Recibir el POST    
    1. **Mecanismo**: Enrutador del marco web   
    2. **Patron**: Front Controller   
    3. **Función**: Recibe el POST y lo dirige al controlador correspondiente.   
2. Autenticación del POST   
    1. **Mecanismo**: Filtro   
    2. **Patron**: Chain of Responsibility   
    3. **Función**: Se valida el token de sesión del estudiante. Si el pago ya se registro o la sesión caduco, cancela la petición.   
3. Registro del pago   
    1. **Mecanismo**: Servicio   
    2. **Patron**: Adapter   
    3. **Función**: Valida los datos enviados y hace la ejecución del servicio. Al terminar envía una respuesta HTTP.   
4. Procesar pago   
    1. **Mecanismo**: Servicio   
    2. **Patron**: Strategy + Adapter   
    3. **Función**: Ejecuta el servicio de cobro (Strategy). Traducimos la consulta a lo que pide el banco, para posteriormente traducir la respuesta a los estados internos (pendiente / acreditado / rechazado)   
5. Cambio de estado   
    1. **Mecanismo**: Repositorio   
    2. **Patron**: Repository   
    3. **Función**: Se registra el cambio en la base de datos y el estado del pago se cambia.   
6. Notificación del pago   
    1. **Mecanismo**: Servicio   
    2. **Patron**: Observer   
    3. **Función**: Al confirmar el pago en la base notifica a cualquier oyente (Alta en Control Escolar, Notificación a Caja y Servicio de Email)   
   
   
04/09/26   
Análisis de cada proyecto (agregar los patrones de diseño que se deben usar para cada problema encontrado, tomar en cuenta el lenguaje del proyecto)   
CINEREX\_DJANGO   
- En la base de datos, las tablas no contienen un autoincremento en los ID, así como también no parece que especifique que el ID es una llave primaria. En las tablas que que hacen referencia a otras tablas no se especifica que hay una llave foranea.   
- Falta de documentación apropiada   
   
   
HOTELLUNA\_SPRING   
- En la base de datos, tiene un problema similar a Cinerex, algunas de las tablas no especifican la llave primaria, y no especifica las llaves foraneas en las tablas que hacen referencia a otras tablas.    
- Falta de documentación apropiada   
   
   
PASOFIT\_FLUTTER   
-    
   
   
SABORES\_LARAVEL   
   
   
TALLERPRO\_EXPRESS   
   
18/09/26 - FALTA DE SUBIR (EQUIPO)   
Factory method, adapter strategy incorporado en los siguientes frameworks   
Laravel    
     
Django   
     
   
22/09/2026   
Django, Laravel y Rails ya cuentan con un servidor integrado?   
Django   
  Local: Ya cuenta con servidor integrado para desarrollo local   
  Producción: Gunicorn (Web Server Gateway Interface) + Nginx + uWSGI   
Laravel   
  Local: Ya cuenta con servidor integrado para desarrollo local   
  Producción: Nginx + PHP-FPM   
Rails   
  Local: Ya cuenta con servidor integrado para desarrollo local   
  Producción: Puma + Nginx   
   
29/09/26   
Investigar que ventajas tiene Larabel y Rubi on rails.   
**Laravel** (PHP) incluye o facilita:   
- ORM (Eloquent),   
- autenticación y autorización (Breeze, Jetstream, Fortify),   
- migraciones y *seeders*,   
- enrutamiento y manejo de URLs,   
- sistema de plantillas (Blade),   
- *middleware*,   
- colas de trabajo (*queues*) y tareas programadas (*scheduler*),   
- validación de datos,   
- manejo de sesiones y *cookies*,   
- eventos y oyentes (*events & listeners*),   
- almacenamiento y manejo de archivos (*Flysystem*),   
- envío de correos y notificaciones,   
- pruebas automatizadas (Pest / PHPUnit),   
- herramientas de depuración y panel de comandos (Artisan).   
   
**Ruby on Rails** (Ruby) incluye o facilita:   
- ORM (Active Record),   
- migraciones de base de datos,   
- enrutamiento y URLs (*Action Dispatch*),   
- controladores y respuestas HTTP (*Action Controller*),   
- vistas y renderizado de plantillas (*Action View / ERB*),   
- autenticación de usuarios y gestión de sesiones (vía gemas estándar como Devise o herramientas nativas),   
- validación de modelos,   
- procesamiento de trabajos en segundo plano (*Active Job*),   
- envío y recepción de correos (*Action Mailer*),   
- comunicación en tiempo real (*Action Cable*),   
- gestión de archivos adjuntos (*Active Storage*),   
- pruebas e integración continua (*Minitest* / *RSpec*),   
- consola interactiva y comandos CLI ( `rails console`).   
   
   
06/10/26   
Relación entre medio recomendado, clima, destino, paquete   
Clima = no parece ser que afecte en la decisión, ya que, idealmente se evitaría que el repartidor tenga que mojarse debido a que podría enfermarse, pero parece ser que esto no importa por que lo envían de todos modos. Se evita el uso de dron.   
   
   
TAREA: que algoritmos de estadísticas puedo usar para sacar más información del dataset.   
### Algoritmos para descubrir patrones y relaciones   
1. **Algoritmos de Asociación (Reglas de Asociación)**
Son ideales para encontrar combinaciones frecuentes de condiciones que suelen llevar a una elección específica. Por ejemplo, te pueden responder preguntas como: *"¿Cuándo se elige 'Dron'? ¿Es común que sea con peso ligero, clima despejado y distancia corta?"*. El algoritmo **Apriori** o **FP-Growth** es lo que buscas para esto. Te dará reglas como: `Si Peso < 2kg Y Clima = Soleado -> Transporte = Dron (Confianza: 85%)`.    
2. **Algoritmos de Agrupación (Clustering)**
Te ayudan a segmentar tus pedidos en grupos con características similares sin que tú les digas de antemano qué buscar. Por ejemplo, podrías descubrir que existen "pedidos urbanos ligeros" o "pedidos pesados de larga distancia", y ver qué medio de transporte predomina en cada grupo. **K-Means** es el algoritmo más común para esto. Te permite ver si la decisión del transporte se agrupa naturalmente por ciertas combinaciones de variables.   
   
### Algoritmos para entender relaciones y predecir   
**3. Regresión Logística**
Dado que tu variable objetivo es **categórica** (Bici, Moto, Dron, Camioneta), la regresión logística es más apropiada que la regresión lineal. Te sirve para medir **cómo cada variable independiente (peso, tráfico, clima) afecta la probabilidad** de elegir un transporte en particular. Por ejemplo, podrías cuantificar cuánto aumenta la probabilidad de elegir "Camioneta" por cada kilogramo extra de peso.   
**4. Árboles de Decisión**
Son excelentes para visualizar y entender **las reglas de decisión** que rigen la elección del transporte. Un árbol te mostrará de forma jerárquica qué variable es la más importante para dividir los datos primero (por ejemplo, si el peso es el factor principal, luego el tráfico, etc.)  . Es muy intuitivo para explicar el comportamiento del sistema.   
   
12/10/26   
Buscar que en el dataset no este, por ejemplo que haya una situación en la que el modelo no sepa que recomendar.   
   
   
20/10/26   
Analizar los 5 casos y verificar si este afecta a nuestra plataforma   
   
CVS 1   
Presenta una cantidad de pedidos por medio balanceados, es decir, de los 10,000 pedidos 2,500 son de cada medio (Moto, camioneta, bici, dron)   
   
CVS 2   
Presenta un nuevo medio, scoter y a diferencia del primer csv este no está balanceado en cuando a la cantidad de pedidos y medios.   
   
CSV 3   
Presenta los mismo medios que el primer csv, pero este muestra una cantidad de pedidos con moto más alta que cualquier otro medio, poco más del 70% de los pedidos son con moto.   
   
CSV 4   
Al igual que el anterior, hay más pedidos de motos que de cualquier otro medio, un poco más del 50%. Los datos del peso de las motos y camionetas no hay una clara diferencia entre uno y otro, ya que tanto la moto como la camioneta tienen pedidos desde pesos de menos de 1kg hasta pesos como 25kg (en el caso de la moto) y 80 kg (en caso de la camioneta). Tienen datos mesclados en cuanto a los pesos (kg) que lleva cada medio.    
   
CSV 5   
   
   
CSV 6   
   
   
   
   
 --- 
Pendiente por subir al repo personal   
   
   
 --- 
Pendiente por subir al repo del grupo   
-    
   
   
   
EVALUACIÓN - Haremos identificación de patrones mediante la interpretación de analogias   
