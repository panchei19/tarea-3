import matplotlib.pyplot as cajas 
from scipy.stats import binom

n = 100
p = 0.35

tamaños = [10**2, 10**3, 10**4, 10**5]
binomios = []

for size in tamaños:
    binomio = binom.rvs(n, p, size=size)
    binomios.append(binomio)

cajas.figure(figsize=(12, 8))
cajas.boxplot(binomios,  labels =["10^2", "10^3", "10^4", "10^5"])
cajas.title("Diagramas de Cajas")
cajas.xlabel("Tamañ0")
cajas.ylabel("Valor")
cajas.show()

cajas.figure(figsize=(12, 8))
for i, binom in enumerate(binomios):
    cajas.subplot(2, 2, i+1)
    cajas.hist(binom, bins=30, alpha=0.7)
    cajas.title(f"Histograma para tamaño de muestra = 10^{i+2}")
    cajas.xlabel("Valores")
    cajas.ylabel("Frecuencia")
cajas.tight_layout()
cajas.show()

medianas= []
modas= []

def calcular_mediana(binomio):
    binomiosordenados = sorted(binomio)
    n = len(binomio)
    mid = n // 2

    if n % 2 == 0:
        return (binomiosordenados[mid - 1] + binomiosordenados[mid]) / 2
    else:
        return binomiosordenados[mid]


def calcular_moda(binomio):
    frecuencia = {}
    for num in binomio:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num] = 1

    max_frecuencia = max(frecuencia.values())
    modas = [key for key, value in frecuencia.items() if value == max_frecuencia]
    return modas[0]

for binom in binomios:
    mediana = calcular_mediana(binom)
    medianas.append(mediana)
    
    moda = calcular_moda(binom)
    modas.append(moda)