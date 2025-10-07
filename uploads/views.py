import json
import os
from django.shortcuts import render
from .forms import UploadForm
from .utils import get_responsavel, salvar_no_banco

PASTA_UPLOADS = r"Z:\PRICING\UPLOADSTESTE"

def upload_arquivo(request):
    mensagem = None
    form = UploadForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        arquivo = request.FILES["arquivo"]
        caminho_arquivo = os.path.join(PASTA_UPLOADS, arquivo.name)

        # salva o arquivo fisico
        with open(caminho_arquivo, "wb+") as destino:
            for chunk in arquivo.chunks():
                destino.write(chunk)

        # salva no banco usando exatamente o que veio no form
        salvar_no_banco(form, caminho_arquivo)

        mensagem = f"Arquivo '{arquivo.name}' enviado e registrado com sucesso!"

        # recria um formulário limpo (opcional) para evitar resubmissão
        form = UploadForm()

    # mapa banco -> responsavel para JS preencher o campo visualmente
    responsaveis_dict = {
        choice[0]: get_responsavel(choice[0])
        for choice in form.fields["banco"].choices
    }
    responsaveis_json = json.dumps(responsaveis_dict)

    return render(request, "upload.html", {
        "form": form,
        "mensagem": mensagem,
        "responsaveis_json": responsaveis_json,
    })
