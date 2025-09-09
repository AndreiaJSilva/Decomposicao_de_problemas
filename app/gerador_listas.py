
""" 
    Recebo um caminho de um arquivo .txt e utilizo uma função que lê o arquivo e retorna o conteúdo em uma lista de string.
"""
def ler_arquivo(caminho: str) -> str:
    with open(caminho, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo
