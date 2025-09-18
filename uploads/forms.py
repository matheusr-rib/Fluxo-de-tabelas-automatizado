from django import forms
import pandas as pd

PLANILHA_BANCOS = r"Z:\PRICING\UPLOADSTESTE\relacaoBancoResponsavel.xlsx"

# Lê a planilha de relação banco-responsável
df_bancos = pd.read_excel(PLANILHA_BANCOS, sheet_name=0)

BANCO_CHOICES = [
    (row["BANCO"], row["BANCO"])
    for _, row in df_bancos.iterrows()
    if pd.notna(row["BANCO"])
]

class UploadForm(forms.Form):
    arquivo = forms.FileField(label="Selecione o arquivo de comissão")
    banco = forms.ChoiceField(choices=BANCO_CHOICES, label="Banco")
