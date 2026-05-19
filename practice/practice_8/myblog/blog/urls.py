from django.urls import path
from . import views # Ось тут цей імпорт правильний [cite: 596, 597]

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]