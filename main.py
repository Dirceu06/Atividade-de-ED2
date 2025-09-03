import ordenadores
import auxiliar
import sys


try:
    definicoes = auxiliar.lerArq(sys.argv[1])
except IndexError:
    definicoes = auxiliar.lerArq('input.txt')
gerado = auxiliar.gerarVetor(definicoes[0],definicoes[1])
selection, compInfo, timer = ordenadores.selectionSort(gerado[:],definicoes[0])
linhaSelection = f"Selection: {' '.join(map(str,selection ))} comparadorado: {compInfo} veze(s) tempo: {timer*1000000:.2f} microssegundos"
bubble, compInfo, timer = ordenadores.bubbleSort(gerado[:])
linhaBubble = f"Bubble: {' '.join(map(str,bubble ))} comparadorado: {compInfo} veze(s) tempo: {timer*1000000:.2f} microssegundos"


print(gerado)
print(linhaSelection)
print(linhaBubble)

linhas = [linhaSelection,linhaBubble]
auxiliar.escreverArq(linhas)