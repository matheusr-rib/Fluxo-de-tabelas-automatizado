import json
from django.shortcuts import render
from .forms import UploadForm
from .utils import get_responsavel, salvar_no_banco
import os

def upload_arquivo(request):
    mensagem = None
    form = UploadForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        arquivo = request.FILES["arquivo"]
        caminho_arquivo = os.path.join(r"Z:\PRICING\UPLOADSTESTE", arquivo.name)

        # Salva fisicamente o arquivo
        with open(caminho_arquivo, "wb+") as destino:
            for chunk in arquivo.chunks():
                destino.write(chunk)

        # Preenche automaticamente o responsável se não estiver preenchido
        if not form.cleaned_data.get("responsavel"):
            form.cleaned_data["responsavel"] = get_responsavel(form.cleaned_data.get("banco"))

        # Salva todos os dados do formulário no banco
        salvar_no_banco(form, caminho_arquivo)

        mensagem = f"Arquivo '{arquivo.name}' processado com sucesso!"

    # Preparar mapa banco → responsável para JS
    responsaveis_dict = {choice[0]: get_responsavel(choice[0]) for choice in form.fields["banco"].choices}
    responsaveis_json = json.dumps(responsaveis_dict)

    return render(request, "upload.html", {
        "form": form,
        "mensagem": mensagem,
        "responsaveis_json": responsaveis_json
    })
