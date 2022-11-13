from django.db import models


# Create your models here.
class Kelas(models.Model):
    kelas=models.CharField(max_length=1)

    def __str__(self) :
        return self.kelas

class Post(models.Model):
    mata_kuliah = models.CharField(max_length=255)
    dosen = models.CharField(max_length=255)
    kelas = models.ForeignKey(Kelas,on_delete=models.SET_NULL,null=True)
    

    def __str__(self):
        return self.mata_kuliah