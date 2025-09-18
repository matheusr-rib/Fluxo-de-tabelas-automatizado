from django.shortcuts import render, redirect
from django.conf import settings
from .forms import UploadForm
import os
import pandas as pd
from openpyxl import load_workbook
from datetime import datetime

# Caminhos fixos
PLANILHA_BANCOS = r"Z:\PRICING\UPLOADSTESTE\relacaoBancoResponsavel.xlsx"
PLANILHA_FLUXO = r"Z:\PRICING\UPLOADSTESTE\fluxo.xlsx"
PASTA_UPLOADS = r"Z:\PRICING\UPLOADSTESTE"

def upload_view(request):
    mensagem = ""
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES['arquivo']
            banco = form.cleaned_data['banco']

            # Salva o arquivo na pasta de uploads
            caminho_arquivo = os.path.join(PASTA_UPLOADS, arquivo.name)
            with open(caminho_arquivo, 'wb+') as destino:
                for chunk in arquivo.chunks():
                    destino.write(chunk)

            # Busca responsável na planilha relacaoBancoResponsavel.xlsx
            df = pd.read_excel(PLANILHA_BANCOS, sheet_name=0)
            responsavel = df.loc[df["BANCO"] == banco, "RESPONSAVEL"].values[0]

            # Abre planilha fluxo.xlsx e adiciona linha
            wb = load_workbook(PLANILHA_FLUXO)
            ws = wb["Planilha1"]  # aba de fluxo

            nova_linha = [
                datetime.now().strftime("%d/%m/%Y"),  # RECEBIMENTO
                datetime.now().strftime("%H:%M:%S"),  # HORA
                banco,                                # BANCO
                responsavel,                          # AGENTE
                arquivo.name,                         # NOME ARQUIVO
                caminho_arquivo                       # PASTA ARQUIVO BANCO (link)
            ]
            ws.append(nova_linha)
            wb.save(PLANILHA_FLUXO)

            mensagem = f"Arquivo {arquivo.name} enviado e registrado com sucesso!"

    else:
        form = UploadForm()

    return render(request, "upload.html", {"form": form, "mensagem": mensagem})
