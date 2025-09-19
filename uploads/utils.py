import pandas as pd
from .models import FluxoArquivo

# Caminho fixo da planilha de relação banco ↔ responsável
CAMINHO_RELACAO = r"Z:\PRICING\UPLOADSTESTE\relacaoBancoResponsavel.xlsx"

def get_responsavel(banco: str) -> str:
    """
    Busca o responsável correspondente ao banco na planilha de relação.
    Caso não encontre, retorna 'NÃO ENCONTRADO'.
    """
    df = pd.read_excel(CAMINHO_RELACAO, sheet_name="Planilha1")
    linha = df.loc[df["BANCO"] == banco]
    if not linha.empty:
        return linha.iloc[0]["RESPONSAVEL"]
    return "NÃO ENCONTRADO"

def salvar_no_banco(caminho_arquivo: str, **dados) -> FluxoArquivo:
    """
    Salva os dados do upload no banco de dados.
    Recebe o caminho do arquivo e demais campos como argumentos nomeados (**dados).
    """
    nome_arquivo = caminho_arquivo.split("\\")[-1]

    fluxo = FluxoArquivo(
        caminho_arquivo=caminho_arquivo,
        nome_arquivo=nome_arquivo,
        **dados
    )
    fluxo.save()
    return fluxo
