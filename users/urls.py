from django.urls import path
from users import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('cadastro', views.cadastro, name="cadastro"),
    path('meuperfil/<str:nome>', views.meuperfil, name="meu_perfil")
]
