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


if __name__ == "__main__":
    # Dicionário para agrupar as palavras originais pela sua "assinatura"
    classes = {}

    while True: # Custo do total de leituras das n entradas (palavras): O(n)
        try:
            linha = input().strip() # Custo da leitura de cada entrada: O(1)
        except EOFError:
            break

        # Condição de parada especificada pelo professor
        if linha == "*":
            break

        # Ignora linhas vazias caso existam
        if not linha:
            continue

        palavra_original = linha

        # Gera a chave ordenada (assinatura do anagrama) usando merge_sort
        # Exemplo: "roma" -> list("roma") -> merge_sort(...) -> ['a', 'm', 'o', 'r'] -> "amor"
        chave = "".join(merge_sort(list(palavra_original))) # Custo da ordenação com Merge Sort: O(k lg k), sendo k o tamanho (quantidade de caracteres) da palavra original


        # Adiciona a palavra original na sua respectiva classe no dicionário
        if chave not in classes:
            classes[chave] = []
        classes[chave].append(palavra_original) # Custo: O(1)


    # Para cada classe de anagramas, selecionamos a menor palavra (em ordem lexicográfica)
    representantes = []
    for chave, lista_palavras in classes.items(): # Custo deste laço for: O(m), sendo m a quantidade de chaves existentes no dicionário

        # Ordenamos a lista de palavras originais dessa classe usando o merge_sort
        palavras_ordenadas = merge_sort(lista_palavras) # Custo da ordenação com Merge Sort: O(p lg p), sendo p o tamanho da lista associada à chave específica

        # O primeiro elemento é a menor palavra da classe
        menor_palavra = palavras_ordenadas[0] # Custo: O(1)
        representantes.append(menor_palavra) # Custo: O(1)

    # Ordena todas as palavras representantes em ordem lexicográfica
    representantes_ordenados = merge_sort(representantes) # Custo da ordenação com Merge Sort: O(m lg m), pois
    # o tamanho da lista representantes é igual à quantidade de chaves, que por sua vez é igual à quantidade de classes, já que
    # cada classe possui apenas 1 chave. Esse tamanho é m.

    # Imprime cada palavra representante, uma por linha
    for rep in representantes_ordenados: # Custo deste laço for: O(m), pois a lista representantes_ordenados possui o mesmo tamanho que a lista representantes
        print(rep)

# Complexidade assintótica final: 

# 1. PIOR CASO (Nenhuma palavra é anagrama de outra -> m = n, p = 1):
#   - Leitura e geração de chaves: n passadas executando O(k lg k) -> O(n * k lg k)
#   - Extração de representantes: m passadas com merge_sort de p=1 -> O(m) -> O(n)
#   - Ordenação final de líderes: merge_sort com m = n elementos -> O(n lg n)
#   - Impressão na tela: Percorre m = n elementos em tempo linear -> O(n)

# Custo unificado do pior caso: O(n * k lg k + n lg n)