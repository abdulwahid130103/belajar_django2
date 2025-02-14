from rest_framework import routers, serializers, viewsets
from rest_framework.serializers import ValidationError
from .models import Siswa, Kelas
from django.contrib.auth.models import User

class SiswaSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Siswa
        fields = '__all__'
        
class KelasSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Kelas
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer) :
    class Meta:
        model = User
        fields = '__all__'
        

