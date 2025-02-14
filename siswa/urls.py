from django.urls import path
from views.siswa import SiswaView
from core_app.siswa.views_old import SiswaAjaxView
from django.views.generic import TemplateView

app_name = "siswa"

urlpatterns = [
    
    # path('', auth_view.index, name="get-siswa-list")
    path('siswa-list/', SiswaView.as_view(), name="siswa-list"),
    path('siswa-list/getall', SiswaAjaxView.as_view(), name="siswa-getall"),
	path('siswa-list/<str:pk>/edit', SiswaView.as_view(), name="siswa-edit"),
	path('siswa-list/create', SiswaView.as_view(), name="siswa-create"),

	path('siswa-list/<str:pk>/update', SiswaView.as_view(), name="siswa-update"),
	path('siswa-list/<str:pk>/delete', SiswaView.as_view(), name="siswa-delete",),

]