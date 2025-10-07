import pandas as pd
from .models import FluxoArquivo

CAMINHO_RELACAO = r"Z:\PRICING\UPLOADSTESTE\relacaoBancoResponsavel.xlsx"

def get_responsavel(banco: str) -> str:
    """Busca o responsável correspondente ao banco na planilha."""
    try:
        df = pd.read_excel(CAMINHO_RELACAO, sheet_name="Planilha1")
        linha = df.loc[df["BANCO"] == banco]
        if not linha.empty:
            return str(linha.iloc[0]["RESPONSAVEL"]).strip()
    except Exception:
        pass
    return ""

def salvar_no_banco(form, caminho_arquivo: str) -> FluxoArquivo:
    """
    Salva no modelo FluxoArquivo os dados do formulário.
    Se o campo 'responsavel' vier vazio, busca o padrão da planilha.
    """
    dados = form.cleaned_data

    def norm(v):
        return "" if v is None else str(v).strip()

    banco = norm(dados.get("banco"))
    responsavel = norm(dados.get("responsavel"))

    # 👇 fallback automático se estiver vazio
    if not responsavel:
        responsavel = get_responsavel(banco)

    fluxo = FluxoArquivo(
        banco=banco,
        responsavel=responsavel,
        caminho_arquivo=norm(caminho_arquivo),
        nome_arquivo=norm(caminho_arquivo.split("\\")[-1]),
        tipo=norm(dados.get("tipo")),
        situacao=norm(dados.get("situacao")),
        convenio=norm(dados.get("convenio")),
        tipo_op=norm(dados.get("tipo_op")),
        recebido=norm(dados.get("recebido")),
        emailOuContato=norm(dados.get("emailOuContato")),
        observação=norm(dados.get("observação")),
    )
    fluxo.save()
    return fluxo
