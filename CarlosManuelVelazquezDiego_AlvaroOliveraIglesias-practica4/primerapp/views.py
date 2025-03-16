from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import date
from .models import Library, Book, User, Loan

#Gestión de Bibliotecas
@csrf_exempt
def create_library(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if not data.get('name') or not data.get('address'):
                return JsonResponse({'error': 'Faltan datos obligatorios'}, status=400)
            library = Library.objects.create(name=data['name'], address=data['address'])
            return JsonResponse({'id': library.id, 'name': library.name, 'address': library.address}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON mal formado'}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def list_libraries(request):
    libraries = Library.objects.all()
    libraries_list = [{'id': lib.id, 'name': lib.name, 'address': lib.address} for lib in libraries]
    return JsonResponse(libraries_list, safe=False)

def detail_library(request, id):
    try:
        library = Library.objects.get(id=id)
        return JsonResponse({'id': library.id, 'name': library.name, 'address': library.address})
    except Library.DoesNotExist:
        return JsonResponse({'error': 'Library not found'}, status=404)


#Gestión de Libros
@csrf_exempt
def create_book(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if not data.get('title') or not data.get('author') or not data.get('library_id'):
                return JsonResponse({'error': 'Faltan datos obligatorios'}, status=400)
            library = Library.objects.get(id=data['library_id'])
            book = Book.objects.create(title=data['title'], author=data['author'], library=library)
            return JsonResponse({'id': book.id, 'title': book.title, 'author': book.author, 'library': library.name}, status=201)
        except Library.DoesNotExist:
            return JsonResponse({'error': 'Library not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON mal formado'}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def list_books(request, library_id):
    books = Book.objects.filter(library_id=library_id)
    books_list = [{'id': book.id, 'title': book.title, 'author': book.author} for book in books]
    return JsonResponse(books_list, safe=False)

def detail_book(request, id):
    try:
        book = Book.objects.get(id=id)
        return JsonResponse({'id': book.id, 'title': book.title, 'author': book.author})
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)

@csrf_exempt
def update_book(request, id):
    try:
        book = Book.objects.get(id=id)
        if request.method in ['PUT', 'PATCH']:
            data = json.loads(request.body)
            if 'title' in data and not data['title']:
                return JsonResponse({'error': 'El título no puede estar vacío'}, status=400)
            book.title = data.get('title', book.title)
            book.author = data.get('author', book.author)
            book.save()
            return JsonResponse({'id': book.id, 'title': book.title, 'author': book.author})
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def delete_book(request, id):
    try:
        book = Book.objects.get(id=id)
        if request.method == 'DELETE':
            book.delete()
            return JsonResponse({'message': 'Book deleted successfully'}, status=200)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)


#Gestión de Usuarios
@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if not data.get('name') or not data.get('email'):
                return JsonResponse({'error': 'Faltan datos obligatorios'}, status=400)
            user = User.objects.create(name=data['name'], email=data['email'])
            return JsonResponse({'id': user.id, 'name': user.name, 'email': user.email}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON mal formado'}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)


#Gestión de Préstamos
@csrf_exempt
def update_loan(request, id):
    try:
        loan = Loan.objects.get(id=id)
        if request.method == 'PUT':
            data = json.loads(request.body)
            loan.return_date = data.get('return_date', date.today())
            loan.book.is_borrowed = False  # Marcar el libro como disponible
            loan.book.save()
            loan.save()
            return JsonResponse({
                'id': loan.id,
                'book': loan.book.title,
                'user': loan.user.name,
                'loan_date': loan.loan_date,
                'return_date': loan.return_date
            })
    except Loan.DoesNotExist:
        return JsonResponse({'error': 'Loan not found'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)
