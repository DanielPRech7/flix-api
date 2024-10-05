from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),  # Listar e criar
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),  # Detalhar, atualizar e deletar
]
