import matplotlib.pyplot as cajas
from scipy.stats import geom

p_geom = 0.08

tamaños = [10**2, 10**3, 10**4, 10**5]

geometricos = [geom.rvs(p_geom, size=size) for size in tamaños]

cajas.figure(figsize=(12, 8))
cajas.boxplot(geometricos, labels=["10^2", "10^3", "10^4", "10^5"])
cajas.title("Diagramas de Cajas para Distribución Geométrica")
cajas.xlabel("Tamaño ")
cajas.ylabel("Valores")
cajas.show()

cajas.figure(figsize=(12, 8))
for i, geoms in enumerate(geometricos):
    cajas.subplot(2, 2, i+1)
    cajas.hist(geoms, bins=30, alpha=0.7)
    cajas.title(f"Histograma para tamaño de muestra = 10^{i+2}")
    cajas.xlabel("Valores")
    cajas.ylabel("Frecuencia")
cajas.tight_layout()
cajas.show()


def calcular_mediana(geom):
    geomasordenados = sorted(geom)
    n = len(geom)
    mid = n // 2

    if n % 2 == 0:
        return (geomasordenados[mid - 1] + geomasordenados[mid]) / 2
    else:
        return geomasordenados[mid]



def calcular_moda(geom):
    frecuencia = {}
    for num in geom:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num] = 1

    max_frecuencia = max(frecuencia.values())
    modas = [key for key, value in frecuencia.items() if value ==
             max_frecuencia]
    return modas[0]


medianas = []
modas = []

for geoms in geometricos:
    mediana = calcular_mediana(geoms)
    moda = calcular_moda(geoms)
    medianas.append(mediana)
    modas.append(moda)

print("Medianas Geométricas:", medianas)
print("Modas Geométricas:", modas)