import re
"""
  Recebo um caminho de um arquivo .txt e utilizo uma função que lê o arquivo e retorna o conteúdo em uma string.
"""
def ler_arquivo(caminho: str) -> str:
    with open(caminho, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

arthur = ler_arquivo("dados/autores_conhecidos/Arthur_Conan_Doyle.txt")
charles = ler_arquivo("dados/autores_conhecidos/charles_dickens.txt")
jane = ler_arquivo("dados/autores_conhecidos/jane_austen.txt")
mark = ler_arquivo("dados/autores_conhecidos/mark_twain.txt")


#----------------------------MANIPULAÇÃO DO TEXTO----------------------------------------------------
"""
  Separar por frases é uma função que recebe uma lista com um texto em string e retorna várias listas separadas por frases.
  Uma frase é definida como uma sequência de caracteres que termina com um ponto final, ponto de interrogação ou ponto de exclamação.
"""
def separar_por_frases(texto: str) -> list:
    frases = re.split(r'(?<=[.!?]) +', texto)
    return [frase.strip() for frase in frases if frase.strip()]

"""
  Oração é definida como uma sequência de palavras que contém um verbo.
  A função separar_por_oracoes recebe uma lista de frases e retorna várias listas separadas por orações
"""
def separar_por_oracoes(frases: list) -> list:
    oracoes = []
    for frase in frases:
        oracoes.extend(re.split(r'(?<=[,;:]) +', frase))
    return [oracao.strip() for oracao in oracoes if oracao.strip()]

"""
  Separar por palavras é uma função que recebe uma lista de orações e retorna várias listas separadas por palavras, é necessário remover pontuações e caracteres especiais nas palavras
"""
def separar_por_palavras(oracoes: list) -> list:
    palavras = []
    for oracao in oracoes:
        palavras.extend(re.findall(r'\b\w+\b', oracao))
    return [palavra.lower() for palavra in palavras if palavra.strip()]

"""
Para cada autor conhecido a função processar listas deve chamar as funções de separar por frases, orações e palavras. É necessário variáveis para armazenar os resultados intermediários, não precisa retornar nada, mas preciso que as variáveis d efrases, orações e palavras estejam disponíveis no escopo global.
"""
def processar_listas(texto: str):
    global texto_frases, texto_oracoes, texto_palavras
    texto_frases = separar_por_frases(texto)
    texto_oracoes = separar_por_oracoes(texto_frases)
    texto_palavras = separar_por_palavras(texto_oracoes)


#----------------------------------------CÁLCULOS DA IMPRESSÃO DIGITAL------------------------------------------------
"""A função tamanho_medio_das _palavras calcula total de letras/total de palavras"""
def tamanho_medio_das_palavras(palavras: list) -> float:
    total_letras = sum(len(palavra) for palavra in palavras)
    total_palavras = len(palavras)
    return total_letras / total_palavras if total_palavras > 0 else 0

"""A função numero_de_palavras_diferentes calcula o número de palavras únicas em uma lista de palavras / total de palavras"""
def numero_de_palavras_diferentes(palavras: list) -> float:
    palavras_unicas = set(palavras)
    total_palavras = len(palavras)
    return len(palavras_unicas) / total_palavras if total_palavras > 0 else 0

"""A função palavras_usadas_uma_vez calcula o número de palavras que aparecem apenas uma vez na lista de palavras / total de palavras"""
def palavras_usadas_uma_vez(palavras: list) -> float:
    contador = {}
    for palavra in palavras:
        contador[palavra] = contador.get(palavra, 0) + 1
    total_palavras = len(palavras)
    return sum(1 for count in contador.values() if count == 1) / total_palavras if total_palavras > 0 else 0

"""A função numero_medio_de_palavras_por_frase calcula o total de palavras / total de frases"""
def numero_medio_de_palavras_por_frase(palavras: list, frases: list) -> float:
    total_palavras = len(palavras)
    total_frases = len(frases)
    return total_palavras / total_frases if total_frases > 0 else 0

""" A função complexidade_media_das_frases calcula o total de orações / total de frases """
def complexidade_media_das_frases(oracoes: list, frases: list) -> float:
    total_oracoes = len(oracoes)
    total_frases = len(frases)
    return total_oracoes / total_frases if total_frases > 0 else 0

""" A função calcular_impressao_digital chama as funções acima e retorna uma lista com os resultados, com apenas 3 casas decimais """
def calcular_impressao_digital(palavras: list, frases: list, oracoes: list) -> list:
    return [
        round(tamanho_medio_das_palavras(palavras), 3),
        round(numero_de_palavras_diferentes(palavras), 3),
        round(palavras_usadas_uma_vez(palavras), 3),
        round(numero_medio_de_palavras_por_frase(palavras, frases), 3),
        round(complexidade_media_das_frases(oracoes, frases), 3)
    ]

""" Automatiza o cálculo e impressão da impressão_digital para qualquer autor fornecido em um dicionário """
autores = {
  "Arthur Conan Doyle": arthur,
  "Charles Dickens": charles,
  "Jane Austen": jane,
  "Mark Twain": mark
}

resultados = {}

for nome, texto in autores.items():
  processar_listas(texto)
  resultados[nome] = calcular_impressao_digital(texto_palavras, texto_frases, texto_oracoes)

for nome, resultado in resultados.items():
  print(f"Impressão Digital de {nome}:", resultado)


#--------------------------------------AUTOR DESCONHECIDO------------------------------------------
""" Tenho um caminho para um texto de um autor desconhecido, preciso ler o arquivo, processar as listas e calcular a impressão digital, imprimindo o resultado. """
caminho_texto_desconhecido = "dados/desconhecido2.txt"

texto_desconhecido = ler_arquivo(caminho_texto_desconhecido)

processar_listas(texto_desconhecido)
resultado_desconhecido = calcular_impressao_digital(texto_palavras, texto_frases, texto_oracoes)

print(f"\nImpressão Digital do Autor Desconhecido:", resultado_desconhecido)  

""" A função calcular diferença em módulo do autor conhecido e de um autor desconhecido"""

def calcular_diferenca_impressao_digital(autor_conhecido: list, autor_desconhecido: list) -> list:
    diferencas = []
    for i in range(len(autor_conhecido)):
        diff = autor_conhecido[i] - autor_desconhecido[i]
        if diff < 0:
            diff = -diff
        diferencas.append(diff)
    # print(f"Diferença em módulo: {diferencas}")  
    return diferencas

""" A função identificar_autor_desconhecido recebe o cálculo da diferença de impressão digital e faz uma soma ponderada com os seguintes pesos [11, 33, 50, 0.4, 4] e retorna o nome do autor conhecido com a menor soma ponderada """
def calcular_soma_ponderada(diferencas: list) -> float:
    """Faz a soma ponderada das diferenças com pesos específicos."""
    pesos = [11, 33, 50, 0.4, 4]
    soma_ponderada = sum(d * p for d, p in zip(diferencas, pesos))
    return soma_ponderada

def identificar_autor(resultados_conhecidos: dict, resultado_desconhecido: list) -> str:
    somas_ponderadas = {}
    for nome_autor, impressao_digital in resultados_conhecidos.items():
        diferencas = calcular_diferenca_impressao_digital(impressao_digital, resultado_desconhecido)
        soma = calcular_soma_ponderada(diferencas)
        somas_ponderadas[nome_autor] = soma
        print(f"Soma ponderada de {nome_autor}: {soma:.2f}")
    autor_identificado = min(somas_ponderadas, key=somas_ponderadas.get)
    return autor_identificado

autor_identificado = identificar_autor(resultados, resultado_desconhecido)

print(f"\nAutor Desconhecido identificado como: {autor_identificado}")