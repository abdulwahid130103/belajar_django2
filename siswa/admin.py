from django.contrib import admin

from .models import Siswa, Kelas
# Register your models here.
@admin.register(Siswa)
class SiswaAdmin(admin.ModelAdmin) :
    list_display = ('id','user_id','nama','kelas_id','alamat','nilai')
    
@admin.register(Kelas)
class KelasAdmin(admin.ModelAdmin) :
    list_display = ('id','nama')