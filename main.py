import ordenadores
import auxiliar
import sys


try:
    definicoes = auxiliar.lerArq(sys.argv[1])
except IndexError:
    definicoes = auxiliar.lerArq('input.txt')
    
if definicoes == -1:
    sys.exit('Encerrando programa com erro')
gerado = auxiliar.gerarVetor(definicoes[0],definicoes[1])

if definicoes[0] < 15:
    selection, compInfo, timer = ordenadores.selectionSort(gerado[:],definicoes[0])
    linhaSelection = f"Selection: {' '.join(map(str,selection ))} comparadorado: {compInfo} veze(s) tempo: {timer*1000000:.2f} microssegundos"

    bubble, compInfo, timer = ordenadores.bubbleSort(gerado[:])
    linhaBubble = f"Bubble: {' '.join(map(str,bubble ))} comparadorado: {compInfo} veze(s) tempo: {timer*1000000:.2f} microssegundos"

    insertion, compInfo, timer = ordenadores.insertionSort(gerado[:])
    linhaInsertion = f"Insertion: {' '.join(map(str,insertion ))} comparadorado: {compInfo} veze(s) tempo: {timer*1000000:.2f} microssegundos"

    merge, compInfo, timer = ordenadores.mergeSort(gerado[:])
    linhaMerge = f"Merge: {' '.join(map(str,merge ))} comparadorado: {compInfo} veze(s) tempo: {timer*1000000:.2f} microssegundos"

    quick, compInfo, timer = ordenadores.quick(gerado[:])
    linhaQuick = f"Quick: {' '.join(map(str,quick ))} comparadorado: {compInfo} veze(s) tempo: {timer*1000000:.2f} microssegundos"

    heap, compInfo, timer = ordenadores.heapSort(gerado[:])
    linhaheap = f"heap: {' '.join(map(str,heap ))} comparadorado: {compInfo} veze(s) tempo: {timer*1000000:.2f} microssegundos"
    
    cocktail, compInfo, timer = ordenadores.cocktailSort(gerado[:])
    linhacocktail = f"cocktail: {' '.join(map(str,cocktail))} comparadorado: {compInfo} veze(s) tempo: {timer*1000000:.2f} microssegundos"
    
else:
    selection, compInfo, timer = ordenadores.selectionSort(gerado[:],definicoes[0])
    linhaSelection = f"Selection - comparadorado: {compInfo} veze(s) tempo: {timer*1000000:.2f} microssegundos"

    bubble, compInfo, timer = ordenadores.bubbleSort(gerado[:])
    linhaBubble = f"Bubble - comparadorado: {compInfo} veze(s) tempo: {timer*1000000:.2f} microssegundos"

    insertion, compInfo, timer = ordenadores.insertionSort(gerado[:])
    linhaInsertion = f"Insertion - comparadorado: {compInfo} veze(s) tempo: {timer*1000000:.2f} microssegundos"

    merge, compInfo, timer = ordenadores.mergeSort(gerado[:])
    linhaMerge = f"Merge - comparadorado: {compInfo} veze(s) tempo: {timer*1000000:.2f} microssegundos"

    quick, compInfo, timer = ordenadores.quick(gerado[:])
    linhaQuick = f"Quick - comparadorado: {compInfo} veze(s) tempo: {timer*1000000:.2f} microssegundos"

    heap, compInfo, timer = ordenadores.heapSort(gerado[:])
    linhaheap = f"heap - comparadorado: {compInfo} veze(s) tempo: {timer*1000000:.2f} microssegundos"
    
    cocktail, compInfo, timer = ordenadores.cocktailSort(gerado[:])
    linhacocktail = f"cocktail - comparadorado: {compInfo} veze(s) tempo: {timer*1000000:.2f} microssegundos"

print(gerado)
linhas = [linhaSelection,linhaBubble,linhaInsertion,linhaMerge,linhaQuick,linhaheap,linhacocktail]
for i in linhas: print(i)

auxiliar.escreverArq(linhas)