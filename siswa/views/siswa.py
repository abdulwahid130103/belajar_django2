from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from rest_framework.response import Response
from ..serializer import UserSerializer
from rest_framework.renderers import JSONRenderer,JSONRenderer, TemplateHTMLRenderer

from rest_framework import status
from .. models import Siswa
from django.contrib.auth.models import User
from .. serializer import SiswaSerializer
from django.template.response import TemplateResponse
from django.contrib.auth.hashers import make_password

class SiswaView(View) :
    
    template_name = "home/index.html"
    context = {}
    def get(self, request):
        context = {
            'username' : request.session.get("username"),
            'id' : request.session.get("id"),
            'email' : request.session.get("email"),
        }
        return render(request,self.template_name,context)

    # def getAll(self, request):
    #     siswa = Siswa.objects.all().order_by('-id')
    #     serializer = SiswaSerializer(siswa, many=True)
    #     return Response(serializer.data)

    # def getSiswa(request, pk):
    #     siswa = Siswa.objects.get(id=pk)
    #     serializer = SiswaSerializer(siswa, many=False)
    #     return Response(serializer.data)

    # def post(request):
    #     serializer = SiswaSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({
    #             "status": 200,
    #             "message": "Berhasil menyimpan data siswa",
    #         })
            
    # def put(request, pk):
    #     siswa = Siswa.objects.get(id=pk)
    #     serializer = SiswaSerializer(instance=siswa, data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()

    #     return Response({
    #         "status" : 200,
    #         "data" : serializer.data,
    #         "message" : "Berhasil update data siswa"
    #     })


    # def delete(request, pk):
    #     siswa = Siswa.objects.get(id=pk)
    #     siswa.delete()

    #     return Response({
    #         "status" : 200,
    #         "message" : "Berhasil hapus data siswa"
    #     })

class SiswaAjaxView(View) :
    
    template_name = "home/index.html"
    context = {}

    def get(self, request):
        siswa = Siswa.objects.all().order_by('-id'  )
        serializer = SiswaSerializer(siswa, many=True)
        return JsonResponse(serializer.data)