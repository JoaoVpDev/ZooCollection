from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=100)
    especime = models.CharField(max_length=100, default="desconhecido")  # Adicionando o campo especime
    data_coleta = models.DateField(default='2025-01-01')  # Adicionando o campo data_coleta

    def __str__(self):
        return self.nome