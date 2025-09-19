from django import forms
import pandas as pd
from .models import FluxoArquivo

PLANILHA_BANCOS = r"Z:\PRICING\UPLOADSTESTE\relacaoBancoResponsavel.xlsx"

# Lê a planilha de relação banco-responsável
df_bancos = pd.read_excel(PLANILHA_BANCOS, sheet_name=0)

BANCO_CHOICES = [
    (row["BANCO"], row["BANCO"])
    for _, row in df_bancos.iterrows()
    if pd.notna(row["BANCO"])
]

class UploadForm(forms.ModelForm):
    arquivo = forms.FileField(label="Selecione o arquivo de comissão")
    banco = forms.ChoiceField(choices=BANCO_CHOICES, label="Banco")
    responsavel = forms.CharField(label="Responsável", required=False)  # <--- novo campo

    class Meta:
        model = FluxoArquivo
        fields = [
            "arquivo",
            "banco",
            "responsavel",
            "tipo",
            "situacao",
            "convenio",
            "tipo_op",
            "recebido",
            "emailOuContato",
            "observação",
        ]
        labels = {
            "responsavel": "Responsável",
            "tipo": "Tipo",
            "situacao": "Situação",
            "convenio": "Convênio",
            "tipo_op": "Tipo de Operação",
            "recebido": "Recebido",
            "emailOuContato": "E-mail ou Contato",
            "observação": "Observação",
        }
        widgets = {
            "observação": forms.Textarea(attrs={"rows": 3}),
        }
