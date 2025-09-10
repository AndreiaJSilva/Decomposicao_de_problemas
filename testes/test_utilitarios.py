from app.gerador_listas import ler_arquivo
from app.processador_texto import separar_por_frases, separar_por_oracoes, separar_por_palavras, processar_listas
from app.calculadora_metricas import tamanho_medio_das_palavras, numero_de_palavras_diferentes, palavras_usadas_uma_vez, numero_medio_de_palavras_por_frase, complexidade_media_das_frases, calcular_impressao_digital
from app.identificador_autor import calcular_diferenca_impressao_digital, calcular_soma_ponderada, identificar_autor
# calcular_diferenca_impressao_digital, calcular_soma_ponderada, identificar_autor

# Verificar se o arquivo tem conteúdo
def test_ler_arquivo():
    caminho = "dados/autores_conhecidos/Arthur_Conan_Doyle.txt"
    conteudo = ler_arquivo(caminho)
    assert isinstance(conteudo, str)
    assert len(conteudo) > 0

def test_separar_por_frases():
    texto = "Olá! Como vai você? Espero que bem."
    frases = separar_por_frases(texto)
    assert isinstance(frases, list)
    assert len(frases) == 3
    assert frases[0] == "Olá!"
    assert frases[1] == "Como vai você?"
    assert frases[2] == "Espero que bem."

def test_separar_por_oracoes():
    texto = "Eu gosto de ler livros, especialmente mistério e aventura."
    oracoes = separar_por_oracoes([texto])
    assert isinstance(oracoes, list)
    assert len(oracoes) == 2

def test_separar_por_palavras():
    texto = "Eu gosto de ler livros."
    palavras = separar_por_palavras([texto])
    assert isinstance(palavras, list)
    assert len(palavras) == 5
    assert palavras[0] == "eu"
    assert palavras[1] == "gosto"
    assert palavras[2] == "de"
    assert palavras[3] == "ler"
    assert palavras[4] == "livros"

def test_processar_listas():
    texto = "Olá! Eu gosto de ler livros, especialmente mistério e aventura."
    frases, oracoes, palavras = processar_listas(texto)
    assert isinstance(frases, list)
    assert isinstance(oracoes, list)
    assert isinstance(palavras, list)
    assert len(frases) == 2
    assert len(oracoes) == 3
    assert len(palavras) == 10

def test_tamanho_medio_das_palavras():
    palavras = ["Eu", "gosto", "de", "ler", "livros"]
    resultado = tamanho_medio_das_palavras(palavras)
    assert isinstance(resultado, float)
    assert round(resultado, 3) == 3.6  # (2 + 5 + 2 + 3 + 6) / 5 = 3.6

def test_numero_de_palavras_diferentes():
    palavras = ["Eu", "gosto", "de", "ler", "livros", "Eu"]
    resultado = numero_de_palavras_diferentes(palavras)
    assert isinstance(resultado, float)
    assert round(resultado, 3) == 0.833  # 5 palavras únicas / 6 palavras totais

def test_palavras_usadas_uma_vez():
    palavras = ["Eu", "gosto", "de", "ler", "livros", "Eu", "gosto"]
    resultado = palavras_usadas_uma_vez(palavras)
    assert isinstance(resultado, float)
    assert round(resultado, 3) == 0.429  # 3 palavras usadas uma vez / 7 palavras totais

def test_numero_medio_de_palavras_por_frase():
    frases = ["Eu gosto de ler.", "Livros são ótimos.", "A leitura é divertida."]
    palavras = ["Eu", "gosto", "de", "ler", "Livros", "são", "ótimos", "A", "leitura", "é", "divertida"]
    resultado = numero_medio_de_palavras_por_frase(palavras, frases)
    assert isinstance(resultado, float)
    assert round(resultado, 3) == 3.667  # 11 / 3 = 3.667

def test_complexidade_media_das_frases():
    frases = ["Eu gosto de ler.", "Livros são ótimos.", "A leitura é divertida."]
    oracoes = ["Eu gosto de ler", "Livros são ótimos", "A leitura é divertida", "e informativa"]
    resultado = complexidade_media_das_frases(oracoes, frases)
    assert isinstance(resultado, float)
    assert round(resultado, 3) == 1.333  # 4 / 3 = 1.333

def test_calcular_impressao_digital():
    palavras = ["Eu", "gosto", "de", "ler", "livros", "Eu", "gosto"]
    frases = ["Eu gosto de ler.", "Livros são ótimos."]
    oracoes = ["Eu gosto de ler", "Livros são ótimos"]
    resultado = calcular_impressao_digital(palavras, frases, oracoes)
    assert isinstance(resultado, list)
    assert len(resultado) == 5
    assert all(isinstance(valor, float) for valor in resultado)
    assert [round(valor, 3) for valor in resultado] == [3.571, 0.714, 0.429, 3.5, 1.0]

def test_calcular_diferenca_impressao_digital():
    autor_conhecido = [4.0, 0.8, 0.5, 5.0, 1.2]
    autor_desconhecido = [3.5, 0.7, 0.4, 4.5, 1.0]
    resultado = calcular_diferenca_impressao_digital(autor_conhecido, autor_desconhecido)
    assert isinstance(resultado, list)
    assert len(resultado) == 5
    assert all(isinstance(valor, float) for valor in resultado)
    assert [round(valor, 3) for valor in resultado] == [0.5, 0.1, 0.1, 0.5, 0.2]

def test_calcular_soma_ponderada():
    diferencas = [0.5, 0.1, 0.1, 0.5, 0.2]
    resultado = calcular_soma_ponderada(diferencas)
    assert isinstance(resultado, float)
    assert round(resultado, 3) == 14.8  # (0.5*11) + (0.1*33) + (0.1*50) + (0.5*0.4) + (0.2*4) = 14.8

def test_identificar_autor():
    resultados_conhecidos = {
        "Autor_A": [4.0, 0.8, 0.5, 5.0, 1.2],
        "Autor_B": [3.0, 0.6, 0.3, 4.0, 0.9],
        "Autor_C": [5.0, 0.9, 0.6, 6.0, 1.5]
    }
    resultado_desconhecido = [3.5, 0.7, 0.4, 4.5, 1.0]
    autor_identificado = identificar_autor(resultados_conhecidos, resultado_desconhecido)
    assert isinstance(autor_identificado, str)
    assert autor_identificado in resultados_conhecidos.keys()
    assert autor_identificado == "Autor_B"  # Autor_B tem a menor soma ponderada