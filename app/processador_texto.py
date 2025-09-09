import re
#----------------------------MANIPULAÇÃO DO TEXTO----------------------------------------------------

"""
  Separar por frases é uma função que recebe uma lista com um texto em string e retorna uma lista separadas por frases.
  Uma frase é definida como uma sequência de caracteres que termina com um ponto final, ponto de interrogação ou ponto de exclamação.
"""
def separar_por_frases(texto: str) -> list:
    frases = re.split(r'(?<=[.!?]) +', texto)
    return [frase.strip() for frase in frases if frase.strip()]

"""
  Oração é definida como uma sequência de palavras que contém um verbo.
  A função separar_por_oracoes recebe uma lista de frases e retorna uma lista separadas por orações
"""
def separar_por_oracoes(frases: list) -> list:
    oracoes = []
    for frase in frases:
        oracoes.extend(re.split(r'(?<=[,;:]) +', frase))
    return [oracao.strip() for oracao in oracoes if oracao.strip()]

"""
  Separar por palavras é uma função que recebe uma lista de orações e retorna uma lista separadas por palavras, é necessário remover pontuações e caracteres especiais nas palavras
"""
def separar_por_palavras(oracoes: list) -> list:
    palavras = []
    for oracao in oracoes:
        palavras.extend(re.findall(r'\b\w+\b', oracao))
    return [palavra.lower() for palavra in palavras if palavra.strip()]

"""
  Para cada autor conhecido a função processar listas deve chamar as funções de separar por frases, orações e palavras e retorna os resultados.
"""
def processar_listas(texto: str):
    texto_frases = separar_por_frases(texto)
    texto_oracoes = separar_por_oracoes(texto_frases)
    texto_palavras = separar_por_palavras(texto_oracoes)
    return texto_frases, texto_oracoes, texto_palavras
