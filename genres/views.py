from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from genres.models import Genre
from django.shortcuts import get_object_or_404
import json

@csrf_exempt
def genre_create_list_view(request):
    # Listar todos os gêneros
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    
    # Criar um novo gênero
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data['name'])
        new_genre.save()
        return JsonResponse({'id': new_genre.id, 'name': new_genre.name}, status=201)

@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)

    # Obter detalhes do gênero
    if request.method == 'GET':
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)

    # Atualizar um gênero existente
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data.get('name', genre.name)
        genre.save()
        return JsonResponse({'id': genre.id, 'name': genre.name}, status=200)
    
    # Excluir um gênero
    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse({'message': 'Gênero deletado'}, status=204)
