
""" 
  A função calcular diferença em módulo do autor conhecido e de um autor desconhecido
"""
def calcular_diferenca_impressao_digital(autor_conhecido: list, autor_desconhecido: list) -> list:
    diferencas = []
    for i in range(len(autor_conhecido)):
        diff = autor_conhecido[i] - autor_desconhecido[i]
        if diff < 0:
            diff = -diff
        diferencas.append(diff)
    return diferencas

""" 
  A função identificar_autor_desconhecido recebe o cálculo da diferença de impressão digital e faz uma soma ponderada com os seguintes pesos [11, 33, 50, 0.4, 4] e retorna o nome do autor conhecido com a menor soma ponderada
"""
def calcular_soma_ponderada(diferencas: list) -> float:
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
