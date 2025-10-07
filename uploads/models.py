from django.db import models

class Upload(models.Model):
    arquivo = models.FileField(upload_to='')
    criado_em = models.DateTimeField(auto_now_add=True)


class FluxoArquivo(models.Model):
    data = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    hora_encerramento = models.TimeField(null=True, blank=True)

    banco = models.CharField(max_length=100)            # obrigatório
    responsavel = models.CharField(max_length=100, null=True, blank=True)  # opcional

    caminho_arquivo = models.CharField(max_length=500)
    nome_arquivo = models.CharField(max_length=255)

    tipo = models.CharField(max_length=60, null=True, blank=True)
    situacao = models.CharField(max_length=20, null=True, blank=True)
    convenio = models.CharField(max_length=60, null=True, blank=True)
    tipo_op = models.CharField(max_length=20, null=True, blank=True)
    recebido = models.CharField(max_length=20, null=True, blank=True)
    emailOuContato = models.CharField(max_length=500, null=True, blank=True)
    observação = models.CharField(max_length=500, null=True, blank=True)  # mantém o nome com acento como você tinha

    def __str__(self):
        return f"{self.banco} - {self.nome_arquivo}"
