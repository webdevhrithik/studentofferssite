from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('top_deals/', views.top_deals, name='top_deals')
]
