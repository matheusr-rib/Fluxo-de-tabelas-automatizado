from django.db import models

# Create your models here.
class Upload(models.Model):
    arquivo = models.FileField(upload_to='')
    criado_em = models.DateTimeField(auto_now_add=True)



class FluxoArquivo(models.Model):
    data = models.DateField(auto_now_add=True)         # Data de upload
    hora = models.TimeField(auto_now_add=True)         # Hora de upload
    banco = models.CharField(max_length=100)           # Banco
    responsavel = models.CharField(max_length=100)     # Responsável
    caminho_arquivo = models.CharField(max_length=500) # Caminho do arquivo
    nome_arquivo = models.CharField(max_length=255) 
    tipo = models.CharField(max_length=60, null=True) 
    situacao = models.CharField(max_length=20, null=True)
    convenio = models.CharField(max_length=60, null=True)
    tipo_op = models.CharField(max_length=20, null=True)
    recebido = models.CharField(max_length=20, null=True)
    emailOuContato = models.CharField(max_length=500, null=True)
    observação = models.CharField(max_length=500, null=True)

    def __str__(self):
        return f"{self.banco} - {self.nome_arquivo}"