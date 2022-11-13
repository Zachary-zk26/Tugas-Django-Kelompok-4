from django.shortcuts import render

from . forms import TamuMahasiswa
from. models import Mahasiswa


def index(request):
    buku_tamu=TamuMahasiswa()
    context={
        'BukuTamu':buku_tamu,       
    }
    if request.method=="POST":
        Mahasiswa.objects.create(
            nim=request.POST.get('nim'),
            nama=request.POST.get('nama'),
            
        )
    return render (request, 'mahasiswa/index.html',context)