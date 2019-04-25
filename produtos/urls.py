from django.urls import path
from .views import listagem, create, update, delete

urlpatterns = [
    path('list/', listagem, name='listagem_produtos'),
    path('new/', create, name="novo_produto"),
    path('update/<int:id>/', update, name="update_produto"),
    path('delete/<int:id>/', delete, name="delete_produto"),
]
