from app.main import ler_arquivo, separar_por_frases
# separar_por_frases, separar_por_oracoes, separar_por_palavras, processar_listas, tamanho_medio_das_palavras, numero_de_palavras_diferentes, palavras_usadas_uma_vez, numero_medio_de_palavras_por_frase, complexidade_media_das_frases, calcular_impressao_digital,calcular_diferenca_impressao_digital, calcular_soma_ponderada, identificar_autor

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