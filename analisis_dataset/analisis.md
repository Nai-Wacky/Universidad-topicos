---
# yaml-language-server: $schema=schemas\page.schema.json
Object type:
    - Page
Creation date: "2026-10-13T14:32:47Z"
Created by:
    - 'Richard '
Emoji: "\U0001F4DC"
id: bafyreifloux3iueridwtskslqh3ji74mare4mqkvhujjy7r3qmkhyah6ei
---
# ANALISIS   
## Actividad 1 — El retrato del dataset   
**Predigan.** Cuando llueve, ¿Qué medio creen que domina? ¿Y para el centro de la ciudad? ¿Cuál será la distancia más larga que recorre una bicicleta en los datos? ¿Habrá envíos con una etiqueta que rompa las reglas del negocio?   
**Respuesta**:    
  El medio que domina sería la moto, la mayoría de los paquetes no son muy pesados por lo que usar la camioneta solo sería un gasto mayor;    
  Para el centro, la moto también sería la moto, ya que el centro de la ciudad suelen tener mucho trafico por lo que la moto es ideal;    
  La distancia más larga que recorre la bici es de 2.5km~   
  No creo pedidos que rompan las reglas.   
   
**Herramientas.**   
- `pd.crosstab(datos[columna], datos["medio_recomendado"], normalize`"index")= da, para cada valor de la columna, el porcentaje de envíos que va en cada medio.   
- `datos.groupby("medio_recomendado")[columnas].agg(["min", "median", "max"])` resume las columnas numéricas por medio.   
- `datos.apply(funcion, axis=1)` aplica una función a cada fila; con `es_posible` pueden revisar si cada etiqueta respeta las reglas.   
   
   
   
**Preguntas.**   
1. ¿En qué zonas y con qué climas el dron nunca aparece? ¿Qué regla del paso 12 lo explica en cada caso?   
    1. El dron solo aparece en un clima despejado, cualquier otro clima se prefiere enviar la moto o la bicicleta, en el caso de paquetes pequeños. Solo aparece en periferia y residencial.   
   
    ```
    Medio recomendado por zona:
    medio_recomendado  bicicleta  camioneta   dron   moto
    zona_destino                                         
    centro                 0.584      0.135  0.000  0.280
    periferia              0.009      0.140  0.126  0.725
    residencial            0.262      0.146  0.173  0.419
    rural                  0.000      0.408  0.000  0.592
    
    Medio recomendado por clima:
    medio_recomendado  bicicleta  camioneta   dron   moto
    clima                                                
    despejado              0.328      0.166  0.135  0.371
    lluvia                 0.085      0.167  0.000  0.748
    viento_fuerte          0.317      0.184  0.000  0.499
    ```
2. La bicicleta casi no va a la periferia, aunque ninguna regla se lo prohíbe. ¿Qué otra columna lo explica? Demuéstrenlo con un número.   
    1. Suele encontrarse cerca del limite de lo que puede recorrer la bicicleta, la distancia suele promediar los 6km, un km menos que el limite. Y al ser la mayoría de paquetes pequeños se prefiere usar el dron.   
   
    ```
    Máximos observados:
                       distancia_km  peso_kg  volumen_l
    medio_recomendado                                  
    bicicleta                  7.00     7.99      39.70
    camioneta                 59.12    80.00     400.57
    dron                      14.99     2.50      11.98
    moto                      39.90    24.93      89.99
    
    Distancia promedio de los pedidos en bicicleta a la periferia:
    6.402777777777778
    ```
3. Comparen los máximos de distancia, peso y volumen de cada medio con la tabla `LIMITES`. ¿Qué límites se pueden adivinar solo mirando los datos? ¿Cuál no y por qué?   
    1. Bicicleta: Si es posible adivinar el porque de los limites, ya que al revisar los datos se muestra que los valores más altos fueron los que se tomaron como el limite.   
    2. Moto: Mismo caso con la moto, los valores más altos son los limites.   
    3. Camioneta: En este caso los valores más altos no son los limites, por lo que no se puede adivinar el por que mirando los datos, aun así se puede intuir que los limites son los limites de lo que la camioneta puede llevar (peso y volumen) y recorrer (distancia).   
    4. Dron: Al igual que la mayoría, los valores más altos son los limites.   
   
    ```
    Máximos observados:
                       distancia_km  peso_kg  volumen_l
    medio_recomendado                                  
    bicicleta                  7.00     7.99      39.70
    camioneta                 59.12    80.00     400.57
    dron                      14.99     2.50      11.98
    moto                      39.90    24.93      89.99
    ```
4. Hay más de cien camionetas para viajes de menos de 2 km, lo que suena a desperdicio. ¿Cuántas tienen una razón clara para ir en camioneta? Para las que no, propongan una explicación.   
    1. Las que tienen una razon clara serían por un paquete con un peso grande (más de 25 kg) y/o un volumen grande (más de 90 L).    
   
    ```
    Máximos observados:
                       distancia_km  peso_kg  volumen_l
    medio_recomendado                                  
    bicicleta                  7.00     7.99      39.70
    camioneta                 59.12    80.00     400.57
    dron                      14.99     2.50      11.98
    moto                      39.90    24.93      89.99
    ```
   
**Para pensar.** Si les dieran solo el CSV, sin las reglas, ¿podrían reconstruir las reglas del negocio a partir de los datos? ¿Cuáles sí y cuáles no? ¿Qué riesgo hay en dejar que un modelo «descubra» las reglas en lugar de escribirlas a mano?   
- Se podrían escribir las reglas sin que nos la den. Todas se podrían escribir. Ya que el modelo generaliza, los limites no son del todo claros, por lo que el modelo terminaría recomendando un medio fuera de los limites.   
   
   
   
## Actividad 2 — La hora y el dron   
**Predigan.** ¿Cuántos drones creen que salen a las 3:00? ¿Qué porcentaje de los envíos creen que sale de noche (antes de las 6 o desde las 21)?   
Respuesta:   
  En caso de que la paquetería acepte enviar pedidos a esa hora, no creo que ninguno. Además, ¿Quién recibe un paquete un paquete a las 3:00 AM? ¿Qué tal si lo roban?   
  Menos del 10%   
   
**Herramientas.**   
- `pd.crosstab(datos["hora_salida"], datos["medio_recomendado"])`.   
- Para verlo como gráfica (requiere `pip install matplotlib`): `tabla.plot(kind`"bar", stacked=True)= y `.figure.savefig("archivo.png")`.   
   
   
**Preguntas.**   
1. ¿En qué horas no hay ni un solo dron? ¿Coincide exactamente con la regla?   
    1. Desde las 21 hasta las 5. Si, hay una regla que indica que el dron no debe salir por la noche, que coincide con las horas en las que el dron no tiene pedidos.   
   
    ```
    Envíos por hora y medio:
    medio_recomendado  bicicleta  camioneta  dron  moto
    hora_salida                                        
    0                          2         12     0    63
    1                          6         11     0    49
    2                          5         19     0    59
    3                          4         13     0    60
    4                          2         10     0    47
    5                          8         25     0   116
    6                         94         50    33   136
    7                        204         92    68   233
    8                        205        118    57   252
    9                        187         97    65   279
    10                       192        123    68   273
    11                       178        107    72   283
    12                       217        111    82   297
    13                       211        112    70   284
    14                       204        103    72   274
    15                       199        122    81   303
    16                       213        108    59   260
    17                       192         97    69   292
    18                       162         97    72   248
    19                       166         78    45   199
    20                       115         72    35   160
    21                        20         58     0   240
    22                         5         28     0   116
    23                         5         15     0    55
    ```
2. ¿Cuántos envíos de noche hay, comparados con los de día? ¿Qué consecuencia tiene eso para lo que el modelo puede aprender sobre la noche?   
    1. Hay 1053 pedidos de noche, los cuales son 7894 pedidos menos que en el día; Esto implicaría que no hay tanta precisión en la predicción del medio de transporte por el desbalance de los datos en comparación de lo pedidos del día.    
   
    ```
    Cantidad de envíos de noche y de día:
    es_noche
    día      8947
    noche    1053
    
    ```
3. Entre las 20:00 y las 21:00 las bicicletas casi desaparecen y las motos aumentan. Busquen en el `README.md` qué lo explica.   
    1. Las bicicletas reciben una penalización al haber un pedido de noche debido al riesgo, por lo que reduce la posibilidad de que se elijan.   
   
    ```
    - **Riesgos:** los paquetes frágiles penalizan a la moto, a la bicicleta y al dron. Los de valor alto penalizan al dron y a la bicicleta. La bicicleta de noche y con lluvia también recibe penalizaciones.
    ```
4. Un árbol solo pregunta «¿la hora es menor o igual que X?». ¿Por qué le cuesta representar «de noche»? ¿Cuántas preguntas sobre la hora necesitaría como mínimo?   
    1. Le cuesta ya que generaliza los datos y aquellos limites que para nosotros son claros para el modelo se hace borrosos; Solo debe preguntar dos veces, si es después de las 6 o antes de las 21.    
   
   
**Para pensar.** Sin mirar los ejercicios de arriba, diseñen una columna nueva que le facilite al árbol entender la noche. Expliquen cómo la calcularían a partir de las columnas que ya existen y cómo comprobarían, con un número, que de verdad ayudó. Si les da tiempo, háganlo.   
**Respuesta**:    
  La forma más fácil que se ocurre de que diferencia la noche con el día es una nueva columna llamada "es\_noche" la cual se calcularía con la columna de la hora de salida; Esto se podría comprobar pidiéndole al una entrega con dron en la noche (Más específicamente en las horas limites como a las 22 o a las 5) y verificar el porcentaje sea 0%.   
   
   
## Actividad 3 — Anatomía de los errores   
**Predigan.** ¿Qué confusión creen que será la más frecuente? ¿El modelo confundirá alguna vez una bicicleta con una camioneta?   
**Respuesta**:    
  Los limites son las áreas donde el modelo podría cometer más errores, además de también aquellos escenarios donde no se tenga mucha información, como son los pedidos en la noche.   
  No creo que llegue al punto de confundir dos medios.   
   
   
**Herramientas.**   
- Para estudiar los errores necesitan exactamente los envíos que el modelo nunca vio. Por eso tienen que separar los datos **igual** que en el paso 4: mismas columnas, `test_size=0.2`, `stratify` y `random_state=42`. Respondan también: ¿qué pasaría con su análisis si usaran otro `random_state`?   
    - random\_state en un parámetro que dicta la semilla para el generador de números aleatorios, lo que permite que los resultados puedan ser reproducibles. Usando Minecraft de ejemplo, si nosotros elegimos las misma semilla (42) el mundo sería el mismo siempre que lo generamos, lo mismo pasa con cualquier otro numero que hayamos elegido. Pero si ponemos el valor none, ese valor se volverá aleatorio, como si no eligiéramos la semilla en Minecraft y nos dará resultados diferentes cada vez.    
- `joblib.load("modelo_medios.joblib")` y `modelo.predict(x_prueba)`.   
- `x_prueba.assign(real=y_prueba, predicho`…)= junta lo real y lo predicho en una tabla; con un filtro se quedan con los errores, y con `groupby(["real", "predicho"]).size()` los cuentan.   
   
   
   
**Preguntas.**   
1. ¿Cuántos errores hay y cuáles son las tres confusiones más frecuentes? ¿Son entre medios parecidos o muy distintos? ¿Qué les dice eso?   
    1. Hubo 158 errores; Las tres confusiones mas comunes son moto-bici, camioneta-moto y moto-dron; Hay muy distintos como moto-camioneta o moto-dron, pero también hay muy parecidos como moto-bici; Parece ser que los medios que se confunde comparten limites, como bici y moto o moto y camioneta, aunque también los que no lo hacen como moto y dron, por lo que podríamos decir que lo que predije esta parcialmente correcto, ya que los medio que más se confunden son aquellos que están cerca de sus limites.    
   
    ```
    Cantidad total de errores:
    158
    
    Confusiones más frecuentes:
    real       predicho 
    moto       bicicleta    46
    camioneta  moto         32
    moto       dron         29
    dtype: int64
    ```
2. Revisen los envíos que eran moto y el modelo mandó a dron. ¿Cuántos son de noche? ¿Cuáles corregirían las reglas del negocio y cuáles no? ¿Qué tienen en común los que no?   
    1. Hay 29 errores. Hay 26 que son de noche. Las reglas corregirían 26 (las que fueron de noche) de los 29 pedidos. Los que no se corrigieron son los pedidos que son de día, además de contar con paquetes pequeños en volumen y peso.   
   
    ```
    Errores moto -> dron:
    Total: 29
    De noche: 26
    
    Casos que corregirían las reglas:
    predicho_posible
    sí corregirían    26
    no corregirían     3
    Name: count, dtype: int64
    
    Errores moto -> dron que las reglas no corregirían:
            distancia_km   peso_kg  volumen_l zona_destino      clima  hora_salida  refrigerado
    count       3.000000  3.000000   3.000000            3          3     3.000000          3.0
    unique           NaN       NaN        NaN            1          1          NaN          NaN
    top              NaN       NaN        NaN  residencial  despejado          NaN          NaN
    freq             NaN       NaN        NaN            3          3          NaN          NaN
    mean        9.013333  1.206667   5.333333          NaN        NaN    16.000000          0.0
    std         2.709619  0.408207   1.497910          NaN        NaN     2.645751          0.0
    min         7.350000  0.900000   3.680000          NaN        NaN    13.000000          0.0
    25%         7.450000  0.975000   4.700000          NaN        NaN    15.000000          0.0
    50%         7.550000  1.050000   5.720000          NaN        NaN    17.000000          0.0
    75%         9.845000  1.360000   6.160000          NaN        NaN    17.500000          0.0
    max        12.140000  1.670000   6.600000          NaN        NaN    18.000000          0.0
    ```
3. Revisen los que eran moto y el modelo mandó a bicicleta. ¿Están cerca del límite de 7 km? Si no es la distancia, busquen qué columnas los distinguen de las bicicletas que el modelo sí acertó.   
    1. Hubo algunos que se acercaron al limite, aunque el promedio esta en los 4km. Parece ser que el peso es la característica que si acerto.   
   
    ```
    Moto -> bicicleta: resumen numérico:
            distancia_km  peso_kg  volumen_l  hora_salida
    count          46.00    46.00      46.00        46.00
    mean            4.08     2.37       9.96        12.98
    median          3.88     1.81       9.05        13.50
    min             1.35     0.27       0.47         2.00
    max             6.89    14.63      31.03        21.00
    
    Bicicletas acertadas: resumen numérico:
            distancia_km  peso_kg  volumen_l  hora_salida
    count         539.00   539.00     539.00       539.00
    mean            3.55     2.16      10.13        12.84
    median          3.37     1.69       7.32        13.00
    min             0.37     0.12       0.30         1.00
    max             7.00     7.75      38.72        23.00
    ```
   
   
   
**Para pensar.** Si solo pudieran arreglar un tipo de error, ¿cuál elegirían y por qué? ¿Lo arreglarían cambiando el modelo, los datos o las reglas del negocio?   
**Respuesta**:    
  Lo medios son importantes, por lo que arreglarlos de forma que no se mezclen sería lo ideal, pero si tuviera que elegir entres los medio que arreglar sería moto-bicicleta que es el más común. Probablemente sea un problemas de datos, debido al desbalance que hay entre los medios usados.   
   
## Actividad 4 — ¿Qué columnas usa de verdad el modelo?   
**Predigan.** Antes de ver nada, ordenen las catorce columnas de la más importante a la menos importante para elegir el medio. Marquen las que creen que el modelo no usa.   
Respuesta:    
  La más importante sería la distancia de ahí seria peso, volumen. Y las que el modelo no usaría serían frágil, refrigerado, valor del producto y prioridad.   
   
**Herramientas.**   
- `modelo.named_steps["arbol"].feature_importances_` da la importancia de cada columna (todas suman 1), en el mismo orden que `modelo.named_steps["preparacion"].get_feature_names_out()`.   
- Para saber qué pasa sin una columna, entrenen otro árbol igual pero quitándola de `NUMERICAS` o `CATEGORICAS`, y mídanlo con los mismos envíos de prueba.   
   
   
   
**Preguntas.**   
1. ¿Cuáles son las cuatro columnas más importantes? ¿Coinciden con las primeras preguntas del árbol del paso 8? ¿Y con su predicción?   
    1. Las columnas son: distancia\_km, volumen\_l, clima y refrigerado. Si coinciden. No coinciden con mi predicción.   
2. ¿Qué columna, al quitarla, baja más la exactitud? ¿Cuáles no la cambian nada?   
    1. Clima hace que la exactitud baje hasta un 84%. Zona\_destino, valor\_declarado y trafico.    
3. La zona de destino tiene importancia cero, pero en la actividad 1 vieron que el dron nunca va al centro. ¿Cómo puede ser que el modelo no use la zona y, aun así, la plataforma nunca mande un dron al centro?   
    1. Los datos que usamos en la primera actividad fueron solo el dataset, no el modelo. Los datos de ese dataset solo se eligieron en base a las reglas de negocio, no el modelo.   
   
   
   
**Para pensar.** La app le pide a la persona catorce datos. Si el modelo no usa algunos, ¿deberían dejar de pedirlos? ¿Hay razones para pedir un dato que el modelo no usa?   
**Respuesta**:   
  Si dejamos a los limites puestos en el código fuera (como es\_posible), no habría problema en dejarlos fuera.   
   
Gini = pureza del dataset (un gini puro significa que no están mezcladas las clases)   
   
## Actividad 5 — El dron es minoría: ¿hay que balancear el dataset?   
Solo el 9.5 % de los envíos son de dron, contra el 45.8 % de moto. A eso se le llama un dataset *desbalanceado*: una clase tiene muchos menos ejemplos que las demás. Muchos modelos aprenden a favorecer a la clase mayoritaria, porque equivocarse con la minoritaria les cuesta poco en la exactitud total. Esta actividad es la más abierta: no se trata de aplicar una receta, sino de decidir si hace falta balancear, cómo hacerlo sin engañarse y qué consecuencias tiene para la plataforma.   
   
   
- Parte A — Pensar antes de tocar los datos   
    Respondan antes de escribir código:   
1. ¿Qué exactitud tendría un «modelo» que nunca dice dron y siempre acierta todo lo demás? ¿Y uno que siempre dice moto? ¿Qué les dice eso sobre usar la exactitud para juzgar un dataset desbalanceado? ¿Qué medidas del paso 7 usarían en su lugar?   
    1. Un modelo que nunca acierta uno de los 4, sería un 90% exacto la mayoría del tiempo, ya que solo se usa el dron 10% de las veces. Mucho menos exacto. Se podría asumir que hay un problema con el dataset.    
2. ¿Por qué hay tan pocos drones? ¿Es un error de los datos o refleja cómo funciona la empresa? ¿Cambia eso la decisión de balancear?   
    1. Hay pocos datos ya que los pedidos no suelen estar dentro de las características para enviarlo en dron, esto ocurre más bien por el consume de los clientes que por preferencia de la empresa (la necesidad del mercado de la empresa). Podría ser, ya que quieres que sea preciso en todos los casos.   
3. Si deciden balancear, ¿se balancea antes o después de separar los datos de entrenamiento y de prueba? ¿Se balancean también los datos de prueba? Justifiquen las dos respuestas **antes** de experimentar.   
    1. Antes, para que el modelo ya tenga los datos listo para entrenar el modelo.   
    2. Si, se balancean los datos de prueba.   
   
   
   
- Parte B — Probar estrategias   
    Propongan y prueben **al menos tres** formas de balancear. No les decimos cuáles; piensen en estas ideas generales y decidan cómo llevarlas a código:   
- quitar ejemplos de las clases que sobran;   
- repetir ejemplos de la clase que falta;   
- conseguir ejemplos nuevos de la clase que falta (el generador del dataset acepta `--filas` y `--semilla`);   
- decirle al modelo que equivocarse con un dron cuesta más (busquen qué hace el parámetro `class_weight` de `DecisionTreeClassifier`).   
   
Reglas para que la comparación sea justa:   
- Todas las estrategias se evalúan con los **mismos** 2 000 envíos de prueba de siempre, sin tocarlos. Les conviene escribir una función `evaluar(x_entreno, y_entreno)` que entrene un árbol igual al del paso 6 y lo mida siempre con esa prueba.   
- Para cada estrategia, llenen esta tabla:   
| <br>Estrategia   <br> |  Envíos de entrenamiento   <br> | Exactitud   <br> | Precision dron   <br> | Recall dron   <br> | Veces que predice dron   <br> | Sugerencias imposibles   <br> |
|:----------------------|:--------------------------------|:-----------------|:----------------------|:-------------------|:------------------------------|:------------------------------|
|  Sin balancear   <br> |                                 |                  |                       |                    |                               |                               |
|              …   <br> |                                 |                  |                       |                    |                               |                               |

Las sugerencias imposibles se cuentan con `es_posible` sobre lo que predijo el modelo, como en el paso 12. En la prueba hay 190 drones reales; comparen con cuántas veces los predice cada modelo.   
Después, **hagan trampa a propósito una vez**: balanceen haciendo lo contrario de lo que respondieron en la pregunta 3 de la parte A (por ejemplo, repitan drones antes de separar, o balanceen también la prueba) y midan otra vez. Expliquen por qué los números mejoran y por qué esa mejora es falsa.   
   
   
- Parte C — Interpretar   
1. ¿Qué pasó con el recall del dron y qué pasó con su precision? ¿Por qué una sube cuando la otra baja?   
2. ¿Alguna estrategia dejó al modelo con muchos menos datos de entrenamiento? ¿Qué se pierde con eso?   
3. Si dos estrategias distintas les dieron números casi iguales para el dron, expliquen por qué son, en el fondo, la misma idea.   
4. En el paso 15, el `motivo` de la respuesta dice «confianza 84 %». Después de balancear, ¿ese porcentaje sigue significando lo mismo? (Piensen en qué proporción de drones vio el modelo al entrenar y qué proporción hay en la realidad.)   
   
   
   
- Parte D — Decidir   
    **Para pensar.** La empresa les pregunta si deben usar el modelo balanceado en la plataforma. Respondan con una recomendación y sus razones. Consideren:   
- qué le cuesta más a la empresa: mandar un dron cuando no convenía, o no usar el dron cuando sí convenía;   
- cuáles de esos errores corrigen las reglas del negocio y cuáles no;   
- qué pasaría si mañana la empresa compra el doble de drones;   
- que la respuesta «no balancear» también es válida, si la justifican.   
