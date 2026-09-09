---
# yaml-language-server: $schema=schemas\page.schema.json
Object type:
    - Page
Creation date: "2026-09-03T14:30:14Z"
Created by:
    - 'Richard '
Emoji: "\U0001F4DC"
id: bafyreib5j76gf37b5q3fwtb3rrqivejlooi2w4t3rhbkowznr2trkatpcm
---
# Revisión de codigo - TOPICO   
|          |                                                                                                               PROBLEMA   <br> |                                    CAPA   <br> |                                                                                                                                                  PATRON   <br> |                                                                                                                                                             PORQUE ESE   <br> |                                                                                                                                                                                                                              CUANDO NO   <br> |
|:---------|:------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   <br> | api.php ejecuta PHP recibido por el usuario mediante eval() y permite leer cualquier archivo con file\_get\_contents()   <br> |   Políticas transversales / integración   <br> |                                                                                                              Front Controller + Chain of Responsibility   <br> |                                          Page Controller solo organiza una página o recurso. No resuelve políticas comunes ni impide que cada endpoint quede expuesto.   <br> |                                                                                   en un script privado de mantenimiento ejecutado únicamente por CLI y fuera del servidor web. Aun así, eval() seguiría siendo innecesario y peligroso   <br> |
| 2   <br> |                             SQL construido concatenando entradas del usuario y consultas ejecutadas desde páginas HTML   <br> |                      Datos + aplicación   <br> |                                                                                                                              Repository + Service Layer   <br> |  Template View sirve para pintar datos ya preparados. No debe ejecutar consultas SQL. Llamarlo MVC mientras la vista consulta la base de datos sería un MVC degradado.   <br> |                                                                                                           para un script local de diagnóstico de una sola consulta, aunque seguirían siendo obligatorias las consultas parametrizadas.   <br> |
| 3   <br> |                                   El pago concentra todas las variantes en un switch y duplica la lógica de cada banco   <br> |                Aplicación / integración   <br> |                                                                                                                            Strategy + Adapter + Factory   <br> |                                                       Facade simplifica un subsistema propio. Aquí hace falta traducir una interfaz ajena, que es exactamente Adapter.   <br> |                                                                                                                     si solo existiera un método de pago y no se previeran variantes. En ese caso, un servicio directo sería más claro.   <br> |
| 4   <br> |                                              El pago, saldo, inscripción y correo no tienen atomicidad ni idempotencia   <br> |                     Datos + integración   <br> | Unit of Work para las escrituras locales y clave de idempotencia para el recurso de pago. Observer u Outbox puede encargarse del correo y otros avisos.   <br> |                                             Observer para todo: Observer desacopla notificaciones; no garantiza atomicidad. Un evento no sustituye a una transacción..   <br> |    Unit of Work: cuando solo existe una escritura independiente. Aquí sí hay varias operaciones que deben confirmarse juntas.<br>Observer: si el efecto debe ocurrir dentro de la misma transacción y su fallo debe invalidar el pago.   <br> |
| 5   <br> |                                 Autenticación basada en cookies manipulables, sin autorización real ni protección CSRF   <br> |                 Políticas transversales   <br> |                                                                                                              Front Controller + Chain of Responsibility   <br> |                                                                              poner un if en cada página duplica las políticas y facilita que algún endpoint las omita.   <br> |                                                  si solo existe una operación privada y el framework ya garantiza autenticación en un único middleware global. En ese caso se usa el mecanismo nativo, no una cadena casera adicional.   <br> |
| 6   <br> |                                   Credenciales y secretos están escritos en el código, incluyendo acceso de producción   <br> |   Políticas transversales / integración   <br> |                                                                                                           Configuration Provider + Dependency Injection   <br> |                                                              Singleton solo controla la cantidad de instancias; no protege secretos ni separa configuración de código.   <br> |                                                                                 Dependency Injection: para un script desechable sin colaboradores sustituibles. En una aplicación con base de datos, pagos y pruebas, sí aporta valor.   <br> |

   
## 1. Ejecución remota de código y lectura arbitraria   
En `api.php` se ejecuta directamente `$\_POST['codigo\_php']` con `eval()`. Además, `$\_GET['archivo']` controla qué archivo se lee.   
Esto permite ejecutar código PHP en el servidor o exfiltrar archivos de configuración, credenciales y código fuente. No es simplemente una validación incompleta: es control total del servidor.   
- **Capa:** políticas transversales, porque falta autenticación/autorización antes de llegar al caso de uso; también integración, porque expone una interfaz peligrosa.   
- **Patrón:** Front Controller + Chain of Responsibility. Todas las peticiones deberían pasar por un punto de entrada y una cadena de autenticación, autorización, validación y auditoría.   
- **Por qué no Page Controller:** Page Controller solo organiza una página o recurso. No resuelve políticas comunes ni impide que cada endpoint quede expuesto.   
- **Cuándo no aplicaría:** en un script privado de mantenimiento ejecutado únicamente por CLI y fuera del servidor web. Aun así, `eval()` seguiría siendo innecesario y peligroso.   
   
La corrección real es eliminar `eval()`, eliminar la lectura arbitraria y crear operaciones explícitas con una lista cerrada de acciones autorizadas.   
## 2. SQL Injection y mezcla de presentación con persistencia   
Hay concatenación directa de entradas en varios lugares:   
- `login1.php` concatena usuario y contraseña en el `SELECT`.   
- `index1.php` concatena `perfil\_id`.   
- `kardex1.php` concatena `matricula`.   
- `pagar1.php` concatena el alumno en varias consultas.   
   
Además, las páginas generan HTML, ejecutan SQL, calculan reglas y llaman servicios externos en el mismo archivo.   
- **Capa:** datos y aplicación.   
- **Patrón:** Repository + Service Layer. El repositorio encapsula consultas parametrizadas; el servicio ejecuta el caso de uso sin depender de HTTP ni de HTML.   
- **Por qué no Template View:** Template View sirve para pintar datos ya preparados. No debe ejecutar consultas SQL. Llamarlo MVC mientras la vista consulta la base de datos sería un MVC degradado.   
- **Cuándo no aplicaría:** para un script local de diagnóstico de una sola consulta, aunque seguirían siendo obligatorias las consultas parametrizadas.   
   
También deberían usarse contraseñas con `password\_hash()` y `password\_verify()`, nunca compararlas directamente en SQL.   
## 3. switch de pagos y protocolos bancarios acoplados   
En `pagar.php` se repite la misma estructura para numerosos bancos. En `pagar1.php`, tarjeta, SPEI y efectivo se resuelven en el mismo procedimiento.   
Hay dos variaciones diferentes:   
1. El **medio o política de pago** cambia.   
2. El **protocolo externo del banco** cambia.   
- **Capa:** aplicación e integración.   
- **Patrones:** Strategy + Adapter + Factory.   
    - **Strategy:** representa tarjeta, SPEI y efectivo como políticas intercambiables.   
    - **Adapter:** traduce respuestas externas como `00` o `credito` a conceptos internos como `acreditado`.   
    - **Factory:** crea o selecciona el cobrador concreto a partir del medio elegido.   
- **Por qué no solo Facade:** Facade simplifica un subsistema propio. Aquí hace falta traducir una interfaz ajena, que es exactamente Adapter.   
- **Cuándo no aplicar Strategy:** si solo existiera un método de pago y no se previeran variantes. En ese caso, un servicio directo sería más claro.   
- **Cuándo no aplicar Factory:** si solo existe una implementación concreta y no hay decisión de creación.   
   
En JavaScript o PHP no hace falta copiar una jerarquía enorme de clases: pueden bastar funciones, objetos con contrato común o una tabla de estrategias.   
## 4. Pago parcialmente persistido y doble cobro   
Después de cobrar externamente, el código actualiza saldo, inserta el recibo, registra materias, elimina `pre\_alta` y envía correo sin una transacción única. Si falla una operación intermedia, el banco puede haber cobrado pero la inscripción quedar incompleta.   
Además, no existe una clave de idempotencia. Un doble clic puede generar dos cargos.   
- **Capa:** datos e integración.   
- **Patrones:** Unit of Work para las escrituras locales y clave de idempotencia para el recurso de pago. Observer u Outbox puede encargarse del correo y otros avisos.   
- **Por qué no Observer para todo:** Observer desacopla notificaciones; no garantiza atomicidad. Un evento no sustituye a una transacción.   
- **Cuándo no aplicar Unit of Work:** cuando solo existe una escritura independiente. Aquí sí hay varias operaciones que deben confirmarse juntas.   
- **Cuándo no aplicar Observer:** si el efecto debe ocurrir dentro de la misma transacción y su fallo debe invalidar el pago.   
   
La operación debería recibir una clave única, por ejemplo `Idempotency-Key`, y devolver el mismo resultado cuando se reintente la misma operación.   
## 5. Autenticación y autorización insuficientes   
En `index1.php`, basta con que exista la cookie `usuario\_logueado=si` o una sesión. La cookie es controlable por el cliente. Además, `perfil\_id` se recibe por URL y no se comprueba que corresponda al usuario autenticado.   
En `index.php`, incluso aparece un bypass administrativo mediante cookie.   
- **Capa:** políticas transversales.   
- **Patrón:** Front Controller + Chain of Responsibility mediante middleware de autenticación y autorización.   
- **Por qué no Singleton de sesión:** la sesión pertenece a una petición/usuario y debe persistirse mediante sesión segura o token validado. Un Singleton global sería incorrecto en un servidor concurrente.   
- **Por qué no Page Controller:** poner un `if` en cada página duplica las políticas y facilita que algún endpoint las omita.   
- **Cuándo no aplicar una cadena:** si solo existe una operación privada y el framework ya garantiza autenticación en un único middleware global. En ese caso se usa el mecanismo nativo, no una cadena casera adicional.   
   
También falta CSRF para operaciones que cambian estado, como pagos y bajas de materias.   
## 6. Secretos y configuración sensible dentro del código   
Las conexiones contienen usuarios, contraseñas, direcciones internas y credenciales de producción en:   
- `db\_connect.php`   
- `db\_connect\_produccion.php`   
- `pagar1.php`   
- `login1.php`   
- `kardex1.php`   
- **Capa:** políticas transversales e integración.   
- **Patrones:** Configuration Provider + Dependency Injection. La aplicación recibe una conexión o cliente configurado desde fuera, mediante variables de entorno, secretos del despliegue o un gestor de secretos.   
- **Por qué no Singleton:** Singleton solo controla la cantidad de instancias; no protege secretos ni separa configuración de código.   
- **Cuándo no aplicar Dependency Injection:** para un script desechable sin colaboradores sustituibles. En una aplicación con base de datos, pagos y pruebas, sí aporta valor.   
   
Las credenciales expuestas deben revocarse y rotarse; moverlas a un archivo ignorado por Git no basta si ya fueron comprometidas.   
   
EXPOSICIÓN   
- Mal versionado (config1)   
- Datos de conexión expuesto en DB, riesgo de seguridad   
- Un archivo hace todo   
- Codigo html y sql revuelto   
