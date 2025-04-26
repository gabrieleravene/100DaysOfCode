# verifique se uma lista está ordenada

# escreva uma função que verifica se uma lista de números está ordenada em ordem crescente ou decrescente

def verificar_ordem(lista):
    crescente = True
    decrescente = True
    
    for i in range(len(lista) - 1):
        if lista[i] > lista[i+1]:
            crescente = False
        if lista[i] < lista[i+1]:
            decrescente = False
        
    return crescente, decrescente