
import time

def bubbleSort(lista):
    inicio = time.time()
    comparacoes = 0
    
    troca = True
    j = len(lista)-1
    while(troca):
        comparacoes += 1
        troca = False
        for i in  range(j):
            comparacoes += 1    
            if lista[i] > lista[i+1]:
                comparacoes += 1
                lista[i],lista[i+1] = lista[i+1], lista[i]
                troca = True
        j -= 1
    fim =time.time()
    timer = fim-inicio
    return lista, comparacoes, timer

def selectionSort(vet, n):
    inicio = time.time() 
    comparacoes = 0
    for i in range(0,n-1):
        menor = i
        for j in range(i, n):
            comparacoes += 1
            if vet[menor] > vet[j]:
                menor = j
        if menor != i:
            vet[menor],vet[i]=vet[i],vet[menor]
        
    fim = time.time()
    timer = fim-inicio
    return vet, comparacoes, timer
