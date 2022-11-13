from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    nim=models.CharField(max_length=10)
    nama=models.CharField(max_length=50)
    
    def __str__(self) :
        return self.nim