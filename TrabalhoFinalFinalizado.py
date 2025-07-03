import time

def encontrar_palavras(matriz, palavras):
    if not matriz or not matriz[0]:
        return []

    linhas, colunas = len(matriz), len(matriz[0])

    visitado = [[False for _ in range(colunas)] for _ in range(linhas)] 
    
    palavras_encontradas = []

    for palavra in palavras:

        start_busca_palavra = time.perf_counter()
        

        caminho_encontrado = buscar_palavra(matriz, palavra, visitado)
        

        end_busca_palavra = time.perf_counter()

        if caminho_encontrado:
            palavras_encontradas.append(palavra)

            for r, c in caminho_encontrado:
                visitado[r][c] = True
    
    return palavras_encontradas


def buscar_palavra(matriz, palavra, visitado):
    linhas, colunas = len(matriz), len(matriz[0])

    for r in range(linhas):
        for c in range(colunas):

            if not visitado[r][c] and matriz[r][c] == palavra[0]:

                caminho = busca_recursiva(matriz, palavra, r, c, 0, visitado)
                if caminho:
                    return caminho
    return None


def busca_recursiva(matriz, palavra, r, c, index, visitado):
    if matriz[r][c] != palavra[index]:
        return None

    if index == len(palavra) - 1:
        return [(r, c)] 

    visitado[r][c] = True

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            
            proximo_r, proximo_c = r + dr, c + dc
            
            linhas, colunas = len(matriz), len(matriz[0])
            if (0 <= proximo_r < linhas and 0 <= proximo_c < colunas and
                    not visitado[proximo_r][proximo_c]):
                
                caminho_parcial = busca_recursiva(matriz, palavra, proximo_r, proximo_c, index + 1, visitado)
                
                if caminho_parcial:

                    visitado[r][c] = False 
                    return [(r, c)] + caminho_parcial


    visitado[r][c] = False
    return None


if __name__ == "__main__":
    matriz_exemplo = [
        ['E', 'A', 'R', 'A'],
        ['N', 'L', 'E', 'C'],
        ['I', 'A', 'I', 'S'],
        ['B', 'Y', 'O', 'T']
    ]

    print("--- Testes com Matriz Exemplo Pequena ---")
    
    palavras_a_buscar = ["REI", "CEIA"]
    start_total_1 = time.perf_counter()
    print(f"\n--- Teste com a ordem: {palavras_a_buscar} ---")
    
    palavras_encontradas_1 = encontrar_palavras(matriz_exemplo, palavras_a_buscar)
    
    end_total_1 = time.perf_counter()
    print(f"Palavras encontradas: {palavras_encontradas_1}")
    print("Explicação: 'REI' é encontrada, e suas células são bloqueadas. \n'CEIA' falha por não poder usar as mesmas células para 'E' e 'I'.")
    print(f"Tempo total de execução do Teste 1: {(end_total_1 - start_total_1):.6f} segundos\n")

    palavras_a_buscar_2 = ["CEIA", "REI"]
    start_total_2 = time.perf_counter()
    print(f"--- Teste com a ordem: {palavras_a_buscar_2} ---")
    
    palavras_encontradas_2 = encontrar_palavras(matriz_exemplo, palavras_a_buscar_2)
    
    end_total_2 = time.perf_counter()
    print(f"Palavras encontradas: {palavras_encontradas_2}")
    print("Explicação: 'CEIA' é encontrada, e suas células são bloqueadas. \n'REI' falha por não poder usar as mesmas células.")
    print(f"Tempo total de execução do Teste 2: {(end_total_2 - start_total_2):.6f} segundos\n")

    print("--- Teste com Matriz e Palavras Maiores ---")
    matriz_grande = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'J'],
        ['K', 'L', 'M', 'N', 'O'],
        ['P', 'Q', 'R', 'S', 'T'],
        ['U', 'V', 'W', 'X', 'Y']
    ]
    palavras_grandes_a_buscar = ["HELLO", "WORLD", "PYTHON", "PROGRAM", "TABLE"]

    start_total_3 = time.perf_counter()
    print(f"\n--- Teste com a ordem: {palavras_grandes_a_buscar} ---")
    
    palavras_encontradas_3 = encontrar_palavras(matriz_grande, palavras_grandes_a_buscar)
    
    end_total_3 = time.perf_counter()
    print(f"Palavras encontradas: {palavras_encontradas_3}")
    print(f"Tempo total de execução do Teste 3: {(end_total_3 - start_total_3):.6f} segundos\n")

    print("\n--- Outro Teste com Matriz Grande e Palavras Complexas ---")
    matriz_complexa = [
        ['A', 'B', 'C', 'D', 'E', 'F'],
        ['G', 'H', 'I', 'J', 'K', 'L'],
        ['M', 'N', 'O', 'P', 'Q', 'R'],
        ['S', 'T', 'U', 'V', 'W', 'X'],
        ['Y', 'Z', 'A', 'B', 'C', 'D'],
        ['E', 'F', 'G', 'H', 'I', 'J']
    ]
    palavras_complexas_a_buscar = ["HIPOGRIFO", "ENGENHARIA", "ALGORITMO", "COMPUTACAO", "UNIFESO"]

    start_total_4 = time.perf_counter()
    print(f"\n--- Teste com a ordem: {palavras_complexas_a_buscar} ---")
    
    palavras_encontradas_4 = encontrar_palavras(matriz_complexa, palavras_complexas_a_buscar)
    
    end_total_4 = time.perf_counter()
    print(f"Palavras encontradas: {palavras_encontradas_4}")
    print(f"Tempo total de execução do Teste 4: {(end_total_4 - start_total_4):.6f} segundos\n")
