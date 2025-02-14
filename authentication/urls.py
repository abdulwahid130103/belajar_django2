from django.urls import path

from .views.auth import AuthView
from django.views.generic import TemplateView

app_name = "authentication"

urlpatterns = [
    path('', AuthView.as_view(), name="index"),
    path('sign_in', AuthView.as_view(), name="sign_in"),

]