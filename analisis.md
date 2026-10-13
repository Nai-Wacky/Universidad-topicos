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
- Actividad 1 — El retrato del dataset   
    **Predigan.** Cuando llueve, ¿qué medio creen que domina? ¿Y para el centro de la ciudad? ¿Cuál será la distancia más larga que recorre una bicicleta en los datos? ¿Habrá envíos con una etiqueta que rompa las reglas del negocio?   
    **Herramientas.**   
- `pd.crosstab(datos[columna], datos["medio_recomendado"], normalize`"index")= da, para cada valor de la columna, el porcentaje de envíos que va en cada medio.   
- `datos.groupby("medio_recomendado")[columnas].agg(["min", "median", "max"])` resume las columnas numéricas por medio.   
- `datos.apply(funcion, axis=1)` aplica una función a cada fila; con `es_posible` pueden revisar si cada etiqueta respeta las reglas.   
   
**Preguntas.**   
1. ¿En qué zonas y con qué climas el dron nunca aparece? ¿Qué regla del paso 12 lo explica en cada caso?   
    1. El dron solo aparece en un clima despejado, cualquier otro clima se prefiere enviar la moto o la bicicleta, en el caso de paquetes pequeños. Solo aparece en periferia y rsidencial.   
2. La bicicleta casi no va a la periferia, aunque ninguna regla se lo prohíbe. ¿Qué otra columna lo explica? Demuéstrenlo con un número.   
    1. Suele encontrarse cerca del limite de lo que puede recorrer la bicicleta, la distancia suele promediar los 6km, un km menos que el limite. Y al ser la mayoría de paquetes pequeños se prefiere usar el dron.   
3. Comparen los máximos de distancia, peso y volumen de cada medio con la tabla `LIMITES`. ¿Qué límites se pueden adivinar solo mirando los datos? ¿Cuál no y por qué?   
    1. Bicicleta: Si es posible adivinar el porque de los limites, ya que al revisar los datos se muestra que los valores más altos fueron los que se tomaron como el limite.   
    2. Moto: Mismo caso con la moto, los valores más altos son los limites.   
    3. Camioneta: En este caso los valores más altos no son los limites, por lo que no se puede adivinar el por que mirando los datos, aun así se puede intuir que los limites son los limites de lo que la camioneta puede llevar (peso y volumen) y recorrer (distancia).   
    4. Dron: Al igual que la mayoría, los valores más altos son los limites.   
4. Hay más de cien camionetas para viajes de menos de 2 km, lo que suena a desperdicio. ¿Cuántas tienen una razón clara para ir en camioneta? Para las que no, propongan una explicación.   
    1. Las que tienen una razon sería por el peso y volumen del paquete.   
   
   
**Para pensar.** Si les dieran solo el CSV, sin las reglas, ¿podrían reconstruir las reglas del negocio a partir de los datos? ¿Cuáles sí y cuáles no? ¿Qué riesgo hay en dejar que un modelo «descubra» las reglas en lugar de escribirlas a mano?   
   
   
