from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from rest_framework.response import Response
from .. serializer import UserSerializer
from rest_framework.renderers import JSONRenderer,JSONRenderer, TemplateHTMLRenderer
# from rest_framework.decorators import api_view, renderer_classes
from rest_framework import status
# from api.models import User
from django.contrib.auth.models import User
# from .. models import Siswa
from django.template.response import TemplateResponse
from django.contrib.auth.hashers import make_password

    
class AuthView(View) :
    
    template_name = "auth/index.html"
    context = {
        'title' : 'Auth'
    }

    def get(self, request) :
        return render(request,self.template_name,self.context)

    def post(self,request) :
        try :
            if request.method == "POST" :    
                user = None
                
                username = request.POST["username"]
                password = request.POST["password"]

                
                user = authenticate(request, username=username, password=password)
                
                if user is not None:
                    login(request, user)
                    query = User.objects.filter(username=username).values()
                    serializer = UserSerializer(query, many=True)
                    request.session['username'] = serializer.data[0]['username']
                    request.session['id'] = serializer.data[0]['id']
                    request.session['email'] = serializer.data[0]['email']
                    request.session.save()
                    return JsonResponse({'message': "Berhasil Login" ,'status':status.HTTP_200_OK}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({'message': "Gagal melakukan login" ,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
            else :
                return JsonResponse({'message': "Gagal melakukan login", 'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        except :
            return JsonResponse({'message': "Gagal melakukan login", 'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
    
    # def sign_out(request) :
    #     if request.method == "POST" and request.POST.get("logout") == "Submit":
    #         logout(request)
            
    #     return HttpResponseRedirect(reverse("authenticate:login"))
        
