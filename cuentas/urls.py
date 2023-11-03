from django.urls import path
from cuentas.views import login, register, editar_perfil, CambiarPassword, ver_perfil
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),  
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('perfil/ver/', ver_perfil, name='ver_perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/editar/password/', CambiarPassword.as_view(), name='editar_pass'),
]