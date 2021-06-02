from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('description/', views.DescriptionView.as_view(), name='description'),
    path('about/', views.AboutView.as_view(), name='about'),
]