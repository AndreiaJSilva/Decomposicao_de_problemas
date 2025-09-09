# Importação dos módulos
from app import gerador_listas
from app import processador_texto
from app import calculadora_metricas
from app import identificador_autor

# ---------------- GERAR LISTA DE ARQUIVOS ---------------------------
# Define a lista de caminhos para os arquivos dos autores conhecidos
caminhos_autores = [
    "dados/autores_conhecidos/Arthur_Conan_Doyle.txt",
    "dados/autores_conhecidos/charles_dickens.txt",
    "dados/autores_conhecidos/jane_austen.txt",
    "dados/autores_conhecidos/mark_twain.txt"
]

# --------- PROCESSAMENTO E CÁLCULO PARA AUTORES CONHECIDOS ---------
resultados = {}
for caminho in caminhos_autores:
    # 1. Lê o conteúdo do arquivo usando a função do módulo gerador_listas
    texto = gerador_listas.ler_arquivo(caminho)

    # 2. Processa o texto em frases, orações e palavras usando o módulo processador_texto
    frases, oracoes, palavras = processador_texto.processar_listas(texto)

    # 3. Calcula a impressão digital do autor usando o módulo calculadora_metricas
    impressao_digital = calculadora_metricas.calcular_impressao_digital(
        palavras, frases, oracoes
    )

    # 4. Extrai o nome do autor do caminho do arquivo e armazena o resultado
    nome_autor = caminho.split('/')[-1].replace('.txt', '')
    resultados[nome_autor] = impressao_digital

print("Impressões Digitais de Autores Conhecidos:")
for nome, resultado in resultados.items():
  print(f"{nome}:", resultado)


#--------------------------------------AUTOR DESCONHECIDO------------------------------------------
""" Tenho um caminho para um texto de um autor desconhecido, preciso ler o arquivo, processar as listas e calcular a impressão digital, imprimindo o resultado. """
caminho_texto_desconhecido = "dados/desconhecido4.txt"

texto_desconhecido = gerador_listas.ler_arquivo(caminho_texto_desconhecido)

# Processa e calcula a impressão digital
frases_desconhecido, oracoes_desconhecido, palavras_desconhecido = \
    processador_texto.processar_listas(texto_desconhecido)

impressao_digital_desconhecido = calculadora_metricas.calcular_impressao_digital(
    palavras_desconhecido, frases_desconhecido, oracoes_desconhecido
)

print(f"\nImpressão Digital do Autor Desconhecido: {impressao_digital_desconhecido}")

autor_identificado = identificador_autor.identificar_autor(resultados, impressao_digital_desconhecido)

print(f"\nAutor Desconhecido identificado como: {autor_identificado}")