# ## Desafio 1

# VOCÊ É UM DEV E PRECISA CRIAR UM SISTEMA PARA UMA ESCOLA. 

# SISTEMA DE NOTAS DE ALUNOS QUE MOSTRE COM ESTATISTICA A MODA E A MEDIA E 
# DESVIO DE PADRÃO, DAS NOTAS DE ALUNOS DE UM COLÉGIO, ALÉM DE MOSTRAR MENOR E A  
# MAIOR NOTA, SEPARE EM FUNÇÕES DIFERENTES 

# 1 -  ***VOCÊ CRIAR SEUS PRÓPRIOS MÓDULOS***

# 2 - ***OU USAR STATISTICS *****

import statistics


def calcular_media(notas):
    return sum(notas) / len(notas)


def calcular_moda(notas):
    try:
        return statistics.mode(notas)
    except statistics.StatisticsError:
        return  print("Não existe moda (valores repetidos)")


def calcular_desvio_padrao(notas):
    return statistics.stdev(notas)


def calcular_maior_menor_nota(notas):
    maior = max(notas)
    menor = min(notas)
    return maior, menor


def sistema_notas():
    
    notas = []
    num_alunos = int(input("Quantos alunos têm na turma? "))
    
    for i in range(num_alunos):
        nota = float(input(f"Digite a nota do aluno {i + 1}: "))
        notas.append(nota)
    
    
    media = calcular_media(notas)
    moda = calcular_moda(notas)
    desvio_padrao = calcular_desvio_padrao(notas)
    maior_nota, menor_nota = calcular_maior_menor_nota(notas)
    
    
    print("\nEstatísticas da turma:")
    print(f"Média das notas: {media:.2f}")
    print(f"Moda das notas: {moda}")
    print(f"Desvio padrão das notas: {desvio_padrao:.2f}")
    print(f"Maior nota: {maior_nota}")
    print(f"Menor nota: {menor_nota}")


sistema_notas()
