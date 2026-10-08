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

    vetor = list((map(int, input().split()))) # Custo da leitura, divisão e conversão de n elementos: O(n)

    vetor_ordenado = merge_sort(vetor) # Custo da ordenação com o Merge Sort: O(n lg n) - Etapa que domina o custo total
    
    print(encontrar_mediana(vetor_ordenado)) # Custo do cálculo do índice e do acesso direto ao elemento no vetor somados: O(1) + O(1) = O(1)

# Complexidade assintótica final: 
# O(n) + O(n lg n) + O(1) = O(n lg n)