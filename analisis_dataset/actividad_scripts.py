import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier

from entranar_arbol_tarea import NUMERICAS, CATEGORICAS, OBJETIVO
from usar_modelo import LIMITES, es_posible

datos = pd.read_csv("envios_medios.csv")

print("\nACTIVIDAD 1 --------------------------------------------------------")

# 1. Proporción de medios para cada zona y clima.
# normalize="index" hace que cada fila sume 1 (100 %).
print("\nMedio recomendado por zona:")
print(pd.crosstab(
    datos["zona_destino"],
    datos["medio_recomendado"],
    normalize="index",
).round(3))

print("\nMedio recomendado por clima:")
print(pd.crosstab(
    datos["clima"],
    datos["medio_recomendado"],
    normalize="index",
).round(3))

# 2. Resumen de las columnas numéricas por medio.
columnas_resumen = ["distancia_km", "peso_kg", "volumen_l"]
print("\nMínimo, mediana y máximo por medio:")
print(datos.groupby("medio_recomendado")[columnas_resumen].agg(
    ["min", "median", "max"]
).round(2))

# 3. Comprobar si cada etiqueta del CSV respeta las reglas del negocio.
# apply(axis=1) pasa cada fila como una Serie a es_posible.
datos["etiqueta_posible"] = datos.apply(
    lambda envio: es_posible(envio["medio_recomendado"], envio),
    axis=1,
)
print("\nEtiquetas que respetan las reglas:")
print(datos["etiqueta_posible"].value_counts().rename(
    {True: "posible", False: "imposible"}
))

# 4. Comprobar distancia promedio de los pedidos en bicicleta a la periferia.
print("\nDistancia promedio de los pedidos en bicicleta a la periferia:")
print(datos.loc[
    (datos["medio_recomendado"] == "bicicleta") &
    (datos["zona_destino"] == "periferia"),
    "distancia_km"
].mean())

print("\nACTIVIDAD 2 --------------------------------------------------------")

# 1. Cantidad de envíos por hora y medio.
# reindex incluye también las horas que no aparezcan en el CSV.
por_hora = pd.crosstab(
    datos["hora_salida"],
    datos["medio_recomendado"],
).reindex(range(24), fill_value=0)
print("\nEnvíos por hora y medio:")
print(por_hora)

# 2. Comparar envíos de noche y de día.
# La noche es antes de las 6:00 o desde las 21:00.
datos["es_noche"] = (
    (datos["hora_salida"] < 6) | (datos["hora_salida"] >= 21)
)
conteo_noche = datos["es_noche"].value_counts().rename(
    {True: "noche", False: "día"}
)
print("\nCantidad de envíos de noche y de día:")
print(conteo_noche)
print("\nPorcentaje de envíos de noche y de día:")
print((conteo_noche / len(datos) * 100).round(2))

print("\nACTIVIDAD 3 --------------------------------------------------------")

# 1. Separar exactamente los mismos datos que se apartaron al entrenar.
x = datos[NUMERICAS + CATEGORICAS]
y = datos[OBJETIVO]
x_entreno, x_prueba, y_entreno, y_prueba = train_test_split(
    x,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42,
)

modelo = joblib.load("modelo_medios.joblib")
prediccion = modelo.predict(x_prueba)

resultados = x_prueba.assign(
    real=y_prueba,
    predicho=prediccion,
)
errores = resultados[resultados["real"] != resultados["predicho"]]

print("\nCantidad total de errores:")
print(len(errores))

print("\nConfusiones más frecuentes:")
print(errores.groupby(["real", "predicho"]).size().sort_values(ascending=False).head(3))

# 2. Revisar los casos en que una moto fue predicha como dron.
moto_dron = errores[
    (errores["real"] == "moto") &
    (errores["predicho"] == "dron")
].copy()
moto_dron["predicho_posible"] = moto_dron.apply(
    lambda envio: es_posible(envio["predicho"], envio),
    axis=1,
)

print("\nErrores moto -> dron:")
print("Total:", len(moto_dron))
print("De noche:", moto_dron["hora_salida"].lt(6).add(
    moto_dron["hora_salida"].ge(21)
).sum())
print("\nCasos que corregirían las reglas:")
print(moto_dron["predicho_posible"].value_counts().rename(
    {True: "no corregirían", False: "sí corregirían"}
))

print("\nErrores moto -> dron que las reglas no corregirían:")
print(moto_dron.loc[
    moto_dron["predicho_posible"],
    ["distancia_km", "peso_kg", "volumen_l", "zona_destino",
     "clima", "hora_salida", "refrigerado"],
].describe(include="all"))

# 3. Comparar moto -> bicicleta con las bicicletas que sí acertó el modelo.
moto_bicicleta = errores[
    (errores["real"] == "moto") &
    (errores["predicho"] == "bicicleta")
].copy()
bicicletas_acertadas = resultados[
    (resultados["real"] == "bicicleta") &
    (resultados["predicho"] == "bicicleta")
].copy()

columnas_numericas = [
    "distancia_km", "peso_kg", "volumen_l", "hora_salida",
]
print("\nMoto -> bicicleta: resumen numérico:")
print(moto_bicicleta[columnas_numericas].agg(
    ["count", "mean", "median", "min", "max"]
).round(2))

print("\nBicicletas acertadas: resumen numérico:")
print(bicicletas_acertadas[columnas_numericas].agg(
    ["count", "mean", "median", "min", "max"]
).round(2))

print("\nACTIVIDAD 4 --------------------------------------------------------")

# 1. Importancia de las variables usadas por el árbol.
preparacion = modelo.named_steps["preparacion"]
arbol = modelo.named_steps["arbol"]
nombres_transformados = preparacion.get_feature_names_out()
importancias = pd.Series(
    arbol.feature_importances_,
    index=nombres_transformados,
).sort_values(ascending=False)

print("\nImportancia de las variables transformadas:")
print(importancias[importancias > 0].round(4))

# Las categorías tienen varias columnas one-hot; sumarlas permite comparar
# la importancia de cada columna original del CSV.
importancias_originales = {}
for nombre, importancia in importancias.items():
    nombre_sin_prefijo = nombre.split("__", 1)[1]
    columna = next(
        (
            candidata
            for candidata in NUMERICAS + CATEGORICAS
            if nombre_sin_prefijo == candidata
            or nombre_sin_prefijo.startswith(candidata + "_")
        ),
        nombre_sin_prefijo,
    )
    importancias_originales[columna] = (
        importancias_originales.get(columna, 0) + importancia
    )

print("\nImportancia acumulada por columna original:")
print(pd.Series(importancias_originales).sort_values(
    ascending=False
).round(4))

# 2. Medir la exactitud quitando una columna cada vez.
def entrenar_sin_columnas(numericas, categoricas):
    preparacion_reducida = ColumnTransformer([
        ("numericas", "passthrough", numericas),
        ("categoricas", OneHotEncoder(handle_unknown="ignore"), categoricas),
    ])
    modelo_reducido = Pipeline([
        ("preparacion", preparacion_reducida),
        ("arbol", DecisionTreeClassifier(
            max_depth=arbol.max_depth,
            min_samples_leaf=arbol.min_samples_leaf,
            random_state=arbol.random_state,
        )),
    ])
    columnas = numericas + categoricas
    modelo_reducido.fit(x_entreno[columnas], y_entreno)
    return modelo_reducido.predict(x_prueba[columnas])


exactitud_completa = (prediccion == y_prueba).mean()
resultados_sin_columna = {}
for columna in NUMERICAS + CATEGORICAS:
    numericas_reducidas = [
        candidata for candidata in NUMERICAS if candidata != columna
    ]
    categoricas_reducidas = [
        candidata for candidata in CATEGORICAS if candidata != columna
    ]
    prediccion_sin_columna = entrenar_sin_columnas(
        numericas_reducidas,
        categoricas_reducidas,
    )
    exactitud = (prediccion_sin_columna == y_prueba).mean()
    resultados_sin_columna[columna] = {
        "exactitud_sin_columna": exactitud,
        "cambio": exactitud - exactitud_completa,
    }

print("\nExactitud del modelo completo:")
print(f"{exactitud_completa:.3%}")
print("\nExactitud al quitar cada columna:")
print(pd.DataFrame(resultados_sin_columna).T.sort_values(
    "exactitud_sin_columna"
).round(4))
