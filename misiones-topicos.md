---
# yaml-language-server: $schema=schemas\page.schema.json
Object type:
    - Page
Creation date: "2026-09-03T05:13:22Z"
Created by:
    - 'Richard '
Emoji: "\U0001F4DC"
id: bafyreidak5332m43trtcwj5kj6xnwcx5w2g5w2o5dgz3k3bidg3h74c4tq
---
# Misiones - TOPICOS   
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
