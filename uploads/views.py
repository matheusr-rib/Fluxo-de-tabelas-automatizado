import os
from datetime import datetime
from django.shortcuts import render, redirect
from .forms import UploadForm
import openpyxl

EXCEL_PATH = r'Z:\PRICING\Matheus\PROJETOFLUXOTABELAS\comissoes.xlsx'

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save()


            data = datetime.now().strftime("%d/%m/%Y")
            hora = datetime.now().strftime("%H:%M:%S")
            nome = upload.arquivo.name
            caminho = os.path.join(r'\\servidor\arquivos_banco', nome)

    
            wb = openpyxl.load_workbook(EXCEL_PATH)
            ws = wb.active
            ws.append([data, hora, nome, caminho])  
            wb.save(EXCEL_PATH)

            return redirect('upload_sucesso')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})
