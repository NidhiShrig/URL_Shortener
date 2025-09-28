print("Loading shortener.urls")
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<str:short_code>/', views.redirect_to_long_url, name='redirect_to_long_url'),
]