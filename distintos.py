def merge_sort(arr):
    # Caso base: vetores com 0 ou 1 elemento já estão ordenados
    if len(arr) <= 1:
        return arr

    # 1. DIVISÃO: Encontra o meio e divide o vetor em duas metades
    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])

    # 2. CONQUISTA: Intercala as duas metades ordenadas
    return merge(esquerda, direita)


def merge(esquerda, direita):
    resultado = []
    i = j = 0

    # Compara os elementos das duas sublistas e insere o menor no resultado
    while i < len(esquerda) and j < len(direita):
        # O operador '<=' garante a estabilidade do algoritmo
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Anexa os elementos remanescentes de cada metade (se houver)
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado

# Custo da ordenação utilizando o algoritmo Merge Sort: 

def busca_distintos(array):
    if not array:
        return 0
    
    cont = 1
    for i in range(1, len(array)):
        if array[i-1] != array[i]:
            cont += 1
        else:
            pass

    return cont


if __name__ == "__main__":

    vetor = list((map(int, input().split()))) # Custo da leitura da entrada: O(1)

    vetor_ordenado = merge_sort(vetor) # Custo da ordenação com Merge Sort: O(n lg n)

    print(busca_distintos(vetor_ordenado)) # Custo da busca pelos números distintos: O(n)

# Complexidade assintótica final: O(1) + O(n lg n) + O(n) = O(n lg n)