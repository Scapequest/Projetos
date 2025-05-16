import random
bingo = "BINGO"
n_disponiveis = []

# Esse loop serve para criar uma matriz, onde cada vetor representa uma coluna com todos os possíveis números.
for i in range(5): 
    lista = list(range(1+(15*i),16+(15*i)))
    random.shuffle(lista)
    n_disponiveis.append(lista)

# Aqui eu é onde eu crio a cartela em si, selecionando aleatóriamente os números de cada linha e coluna.
matriz = []
for l in range(5):
    linha = []
    for c in range(5): #Utilizando a matriz separadas em colunas me possibilitou usar esse loop para pegar um número de cada para formar a linha.
        n = n_disponiveis[c]
        # Abaixo eu utilizei o 'random.randint()' porque não conhecia o 'random.choice()' ainda.
        linha.append(n.pop(random.randint(((len(n)-1)*(-1)),(len(n)-1)))) #Utilizo o primeiro parâmetro multiplicando por -1 para o range total não ser apenas de 0 a 14, mas de -14 a 14, assim aumentando a aleatoriedade do número selecionado.
    matriz.append(linha)

# E aqui é onde faço o print de tudo estruturado para ficar igual à uma cartela de bingo real.
for i in range(5):
    print(f"{bingo[i]:2}", end=" ")
print("")
for l in range(len(matriz)):
    for c in range(len(matriz[0])):
        if l == 2 and c == 2: #Para o centro ser 'BG' e não um número
            print("BG", end=" ")
        else:
            print(f"{matriz[l][c]:02}", end=" ")
    print("")