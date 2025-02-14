from django.utils.translation import gettext_lazy as _
from django.db import models
from rest_framework import routers, serializers
from django.contrib.auth.models import User

class Kelas(models.Model) :
    nama = models.CharField(max_length=20)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'kelas'
        
    def __str__(self):
        return self.nama
    
class Siswa(models.Model) :
    nama = models.CharField(max_length=20)
    alamat = models.CharField(max_length=250)
    nilai = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,default = "")
    kelas_id = models.ForeignKey(Kelas, on_delete=models.CASCADE,default = "")
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'siswa'
        
    def __str__(self):
        return self.nama
