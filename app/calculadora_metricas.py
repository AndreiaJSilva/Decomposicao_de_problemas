#--------------------------------- CÁLCULOS DA IMPRESSÃO DIGITAL -----------------------------------------

"""
  A função tamanho_medio_das_palavras calcula total de letras/total de palavras
"""
def tamanho_medio_das_palavras(palavras: list) -> float:
    total_letras = sum(len(palavra) for palavra in palavras)
    total_palavras = len(palavras)
    return total_letras / total_palavras if total_palavras > 0 else 0

"""
  A função numero_de_palavras_diferentes calcula o número de palavras únicas em uma lista de palavras/total de palavras
"""
def numero_de_palavras_diferentes(palavras: list) -> float:
    palavras_unicas = set(palavras)
    total_palavras = len(palavras)
    return len(palavras_unicas) / total_palavras if total_palavras > 0 else 0

"""
  A função palavras_usadas_uma_vez calcula o número de palavras que aparecem apenas uma vez na lista de palavras/total de palavras
"""
def palavras_usadas_uma_vez(palavras: list) -> float:
    contador = {}
    for palavra in palavras:
        contador[palavra] = contador.get(palavra, 0) + 1
    total_palavras = len(palavras)
    return sum(1 for count in contador.values() if count == 1) / total_palavras if total_palavras > 0 else 0

"""
  A função numero_medio_de_palavras_por_frase calcula o total de palavras/total de frases
"""
def numero_medio_de_palavras_por_frase(palavras: list, frases: list) -> float:
    total_palavras = len(palavras)
    total_frases = len(frases)
    return total_palavras / total_frases if total_frases > 0 else 0

"""
  A função complexidade_media_das_frases calcula o total de orações/total de frases
"""
def complexidade_media_das_frases(oracoes: list, frases: list) -> float:
    total_oracoes = len(oracoes)
    total_frases = len(frases)
    return total_oracoes / total_frases if total_frases > 0 else 0

"""
  A função calcular_impressao_digital chama as funções acima e retorna uma lista com os resultados, com apenas 3 casas decimais
"""
def calcular_impressao_digital(palavras: list, frases: list, oracoes: list) -> list:
    return [
        round(tamanho_medio_das_palavras(palavras), 3),
        round(numero_de_palavras_diferentes(palavras), 3),
        round(palavras_usadas_uma_vez(palavras), 3),
        round(numero_medio_de_palavras_por_frase(palavras, frases), 3),
        round(complexidade_media_das_frases(oracoes, frases), 3)
    ]
