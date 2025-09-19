import pandas as pd
from .models import FluxoArquivo

CAMINHO_RELACAO = r"Z:\PRICING\UPLOADSTESTE\relacaoBancoResponsavel.xlsx"

def get_responsavel(banco: str) -> str:
    """Busca o responsável correspondente ao banco na planilha"""
    df = pd.read_excel(CAMINHO_RELACAO, sheet_name="Planilha1")
    linha = df.loc[df["BANCO"] == banco]
    if not linha.empty:
        return linha.iloc[0]["RESPONSAVEL"]
    return "NÃO ENCONTRADO"

def salvar_no_banco(form, caminho_arquivo: str) -> FluxoArquivo:
    """
    Salva todos os campos do formulário no banco de dados.
    Recebe:
        - form: UploadForm já validado
        - caminho_arquivo: caminho completo do arquivo enviado
    Retorna:
        - FluxoArquivo salvo
    """
    # Pega os dados do form.cleaned_data
    dados = form.cleaned_data
    fluxo = FluxoArquivo(
        banco=dados.get("banco"),
        responsavel=dados.get("responsavel"),
        caminho_arquivo=caminho_arquivo,
        nome_arquivo=caminho_arquivo.split("\\")[-1],
        tipo=dados.get("tipo"),
        situacao=dados.get("situacao"),
        convenio=dados.get("convenio"),
        tipo_op=dados.get("tipo_op"),
        recebido=dados.get("recebido"),
        emailOuContato=dados.get("emailOuContato"),
        observação=dados.get("observação"),
    )
    fluxo.save()
    return fluxo
