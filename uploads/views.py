import json
from django.shortcuts import render
from .forms import UploadForm
from .utils import get_responsavel
import os

def upload_arquivo(request):
    mensagem = None

    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES["arquivo"]
            banco = form.cleaned_data["banco"]

            caminho_arquivo = os.path.join(r"Z:\PRICING\UPLOADSTESTE", arquivo.name)
            with open(caminho_arquivo, "wb+") as destino:
                for chunk in arquivo.chunks():
                    destino.write(chunk)

            responsavel = get_responsavel(banco)
            form.cleaned_data["responsavel"] = responsavel
            form.save()

            mensagem = f"Arquivo '{arquivo.name}' processado com sucesso!"
    else:
        form = UploadForm()

    # Criar mapa banco → responsável e converter para JSON
    responsaveis_dict = {choice[0]: get_responsavel(choice[0]) for choice in form.fields["banco"].choices}
    responsaveis_json = json.dumps(responsaveis_dict)  # converte para string JSON

    return render(request, "upload.html", {
        "form": form,
        "mensagem": mensagem,
        "responsaveis_json": responsaveis_json
    })
