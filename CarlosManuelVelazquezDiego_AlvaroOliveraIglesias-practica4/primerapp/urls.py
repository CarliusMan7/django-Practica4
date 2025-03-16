from django.urls import path
from . import views

urlpatterns = [
    # Bibliotecas
    path('libraries/', views.list_libraries),
    path('libraries/create/', views.create_library),
    path('libraries/<int:id>/', views.detail_library),

    # Libros
    path('libraries/<int:library_id>/books/', views.list_books),
    path('books/create/', views.create_book),
    path('books/<int:id>/', views.detail_book),
    path('books/<int:id>/', views.update_book),  # Para actualizar libros


    # Usuarios
    path('users/', views.list_users),
    path('users/create/', views.create_user),
    path('users/<int:id>/', views.detail_user),

    # Préstamos
    path('loans/', views.list_loans),
    path('loans/create/', views.create_loan),
    path('users/<int:id>/loans/', views.user_loans),
    path('loans/<int:id>/return/', views.return_book),
]
