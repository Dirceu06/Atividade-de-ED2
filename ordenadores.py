
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

def selectionSort(lista, n):
    inicio = time.time() 
    comparacoes = 0
    for i in range(0,n-1):
        menor = i
        for j in range(i, n):
            comparacoes += 1
            if lista[menor] > lista[j]:
                menor = j
        if menor != i:
            lista[menor],lista[i]=lista[i],lista[menor]
        
    fim = time.time()
    timer = fim-inicio
    return lista, comparacoes, timer

def insertionSort(lista):
    inicio = time.time()
    comparacoes = 0
    for i in range(1,len(lista)):
        k = i - 1
        aux = lista[i]
        while k >= 0 and aux < lista[k]:
            comparacoes += 1
            lista[k+1] = lista[k]
            k -= 1
        lista[k + 1] = aux
    fim = time.time()
    timer = fim-inicio
    return lista, comparacoes, timer

def mergeSort(lista,inicio, fim):
    inicio = time.time()
    global comparacoesMergeSort
    if inicio < fim:
        meio = (inicio+fim)//2
        mergeSort(lista,inicio, meio)
        mergeSort(lista, meio+1, fim)
        
        merge(lista, inicio,meio, fim)
    fim = time.time()
    timer = fim-inicio
    return lista, comparacoesMergeSort, timer



def merge(lista, inicio,meio, fim):
    global comparacoesMergeSort
    aux = []
    p1 = inicio
    p2 = meio + 1
    
    while p1 <= meio and p2 <= fim:
        comparacoesMergeSort += 1
        if lista[p1] < lista[p2]:
            aux.append(lista[p1])
            p1 += 1
        else:
            aux.append(lista[p2])
            p2 += 1

    aux.extend(lista[p1:meio+1])
    aux.extend(lista[p2:fim+1])
        
    for i in range(len(aux)):
        lista[inicio + i] = aux[i]

