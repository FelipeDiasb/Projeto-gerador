# # ## Desafio 2

# Você é um analista de dados, e decidiu trocar de emprego.

# Utilize a media, moda, mediana e o desvio padrão para decidir qual empresa faz sentido para você:

# Justificar por que decidiu por essa empresa.

# ***Verifique isso através dos salários:***

# empresa1 = [1000,6000,1200,8000,1400]

# empresa2 = [5000,4000,3000,2000,7000]

# empresa3 = [1200,1300,8000,3000,15000]

# empresa4 = [1400,1750,2000,4500,5900]

import statistics


empresa1 = [1000, 6000, 1200, 8000, 1400]
empresa2 = [5000, 4000, 3000, 2000, 7000]
empresa3 = [1200, 1300, 8000, 3000, 15000]
empresa4 = [1400, 1750, 2000, 4500, 5900]


def calcular_media(salarios):
    return sum(salarios) / len(salarios)

def calcular_moda(salarios):
    try:
        return statistics.mode(salarios)
    except statistics.StatisticsError:
        return "Não há moda (valores únicos)"

def calcular_mediana(salarios):
    return statistics.median(salarios)

def calcular_desvio_padrao(salarios):
    return statistics.stdev(salarios)


def analisar_empresa(nome, salarios):
    media = calcular_media(salarios)
    moda = calcular_moda(salarios)
    mediana = calcular_mediana(salarios)
    desvio_padrao = calcular_desvio_padrao(salarios)

    print(f"\nAnálise da {nome}:")
    print(f"Média dos salários: {media:.2f}")
    print(f"Moda dos salários: {moda}")
    print(f"Mediana dos salários: {mediana}")
    print(f"Desvio padrão dos salários: {desvio_padrao:.2f}")
    
    return media, moda, mediana, desvio_padrao


empresas = {
    "Empresa 1": empresa1,
    "Empresa 2": empresa2,
    "Empresa 3": empresa3,
    "Empresa 4": empresa4
}

resultados = {}

for nome, salarios in empresas.items():
    resultados[nome] = analisar_empresa(nome, salarios)

def justificar_escolha(resultados):
    melhor_empresa = None
    melhor_justificativa = None
    maior_media = -float('inf')
    menor_desvio = float('inf')

    for nome, (media, moda, mediana, desvio_padrao) in resultados.items():
        if media > maior_media and desvio_padrao < menor_desvio:
            maior_media = media
            menor_desvio = desvio_padrao
            melhor_empresa = nome
            melhor_justificativa = f"A {nome} tem a maior média de salário e o menor desvio padrão, indicando estabilidade e boa remuneração."

    return melhor_empresa, melhor_justificativa

# Justificando a escolha
melhor_empresa, justificativa = justificar_escolha(resultados)
print(f"\nA melhor empresa para você é a {melhor_empresa}.")
print(f"Justificativa: {justificativa}")
