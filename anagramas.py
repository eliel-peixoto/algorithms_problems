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

    while True: # Entrada: n palavras - Custo: O(n)
        try:
            linha = input().strip()
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
        chave = "".join(merge_sort(list(palavra_original))) # Custo da ordenação com Merge Sort: O(n lg n)

        # Adiciona a palavra original na sua respectiva classe no dicionário
        if chave not in classes:
            classes[chave] = []
        classes[chave].append(palavra_original) # Possível colocação de custo O(1)

    # Para cada classe de anagramas, selecionamos a menor palavra (em ordem alfabética)
    representantes = []
    for chave, lista_palavras in classes.items(): # Custo deste laço for: O(n) - Maior consumo
        # Ordenamos a lista de palavras originais dessa classe usando o merge_sort
        palavras_ordenadas = merge_sort(lista_palavras) # Custo da ordenação com Merge Sort: O(n lg n)
        # O primeiro elemento é a menor palavra da classe
        menor_palavra = palavras_ordenadas[0] # Custo: O(1)
        representantes.append(menor_palavra) # Possível colocação de custo O(1)

    # Ordena todas as palavras representantes em ordem lexicográfica (alfabética)
    representantes_ordenados = merge_sort(representantes) # Custo da ordenação com Merge Sort: O(n lg n)

    # Imprime cada palavra representante, uma por linha
    for rep in representantes_ordenados: # Custo deste laço for: O(n) - Maior consumo
        print(rep)

# Complexidade assintótica final: O(n) + O(n lg n) + O(n) + O(n lg n) + O(1) + O(n lg n) + O(n) = O(n lg n)