import random
def lerArq(nome):
    try:
        f = open(nome, "r")
        numero = int(f.readline().strip())
        caractere = f.readline().strip()
        f.close()
        info = (numero,caractere)
        return info
    except FileNotFoundError:
        print('não existe o arquivo')
        
def gerarVetor(tamanho,modo):
    vetor = list()
    if modo in 'cC':
        for i in range(tamanho):
            vetor.append(i)
    elif modo in 'dD':
        for i in range(tamanho,0,-1):
            vetor.append(i)
    elif modo in 'rR':
        for i in range(tamanho):
            vetor.append(random.randint(0,32000))
    else:
        print('não existe')
        return 0
    return vetor

def escreverArq(linhas):
    arq = open('output.txt', 'w')
    for i in linhas: arq.write(i)