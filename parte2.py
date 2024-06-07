import matplotlib.pyplot as cajas
from scipy.stats import geom

# Parámetro de la distribución geométrica
p_geom = 0.08

# Tamaños de las muestras
tamaños = [10**2, 10**3, 10**4, 10**5]

# Generar muestras aleatorias de la distribución geométrica
geometricos = [geom.rvs(p_geom, size=size) for size in tamaños]

# Diagrama de cajas para cada muestra
cajas.figure(figsize=(12, 8))
cajas.boxplot(geometricos, labels=["10^2", "10^3", "10^4", "10^5"])
cajas.title("Distribución Geométrica\np = 0,08")
cajas.xlabel("Tamaño de la Muestra")
cajas.ylabel("Valores")
cajas.show()

# Histogramas para cada muestra
cajas.figure(figsize=(12, 8))
for i, geoms in enumerate(geometricos):
    cajas.subplot(2, 2, i+1)
    cajas.hist(geoms, bins=30, alpha=0.7)
    cajas.title(f"Distribución Geométrica\nTamaño de Muestra = 10^{i+2}")
    cajas.xlabel("Valores")
    cajas.ylabel("Frecuencia")
cajas.tight_layout()
cajas.show()


# Función para calcular la mediana
def calcular_mediana(binomio):
    binomiosordenados = sorted(binomio)
    n = len(binomio)
    mid = n // 2

    if n % 2 == 0:
        return (binomiosordenados[mid - 1] + binomiosordenados[mid]) / 2
    else:
        return binomiosordenados[mid]


# Función para calcular la moda
def calcular_moda(binomio):
    frecuencia = {}
    for num in binomio:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num] = 1

    max_frecuencia = max(frecuencia.values())
    modas = [key for key, value in frecuencia.items() if value ==
             max_frecuencia]
    return modas[0]


# Calcular mediana y moda para cada muestra
medianas = []
modas = []

for geoms in geometricos:
    mediana = calcular_mediana(geoms)
    moda = calcular_moda(geoms)
    medianas.append(mediana)
    modas.append(moda)

print("Medianas Geométricas:", medianas)
print("Modas Geométricas:", modas)
