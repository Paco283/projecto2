from django.urls import path
from .views import UserListCreateView, UserDetailView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list'),  # Lista y creación de usuarios
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # Detalles y edición de un usuario
]
