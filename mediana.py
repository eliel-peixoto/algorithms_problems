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

def encontrar_mediana(array):
    return array[((len(array) - 1) // 2)]


if __name__ == "__main__":

    vetor = list((map(int, input().split())))

    vetor_ordenado = merge_sort(vetor)
    
    print(encontrar_mediana(vetor_ordenado))