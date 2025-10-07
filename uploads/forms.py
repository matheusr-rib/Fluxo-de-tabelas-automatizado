from django import forms
import pandas as pd
from .models import FluxoArquivo

PLANILHA_BANCOS = r"Z:\PRICING\UPLOADSTESTE\relacaoBancoResponsavel.xlsx"

df_bancos = pd.read_excel(PLANILHA_BANCOS, sheet_name=0)
BANCO_CHOICES = [
    (row["BANCO"], row["BANCO"])
    for _, row in df_bancos.iterrows()
    if pd.notna(row["BANCO"])
]

class UploadForm(forms.ModelForm):
    arquivo = forms.FileField(label="Selecione o arquivo de comissão", required=True)
    banco = forms.ChoiceField(choices=BANCO_CHOICES, label="Banco", required=True)
    responsavel = forms.CharField(
        label="Responsável",
        required=False,
        widget=forms.TextInput(attrs={"id": "id_responsavel"})
    )

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
        widgets = {"observação": forms.Textarea(attrs={"rows": 3})}
