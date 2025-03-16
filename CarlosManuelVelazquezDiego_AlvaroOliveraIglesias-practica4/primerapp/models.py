from django.db import models


#Biblioteca
class Library(models.Model):
    name = models.CharField(max_length=255,unique = True) #Nombre unico de la biblioteca
    address = models.TextField() #Direccion de la biblioteca


    def __str__(self):  
        return self.name


#Libro
class Book(models.Model):
    title = models.CharField(max_length=255) #Titulo libro
    author = models.CharField(max_length=255) #Nombre autor
    library = models.ForeignKey(Library, related_name="books", on_delete=models.CASCADE)#Relacion con Biblioteca 1-N
    is_borrowed = models.BooleanField(default=False) #Indica si el libro esta prestado o no


    def __str__(self):
        return f"{self.title} ({self.author})"

#Usuario
class User(models.Model):
    name = models.CharField(max_length=255) #Nombre del usuario
    email = models.EmailField(unique=True) #Email unico

    def __str__(self):
        return self.name


#Prestamo

class Loan(models.Model):
    book = models.ForeignKey(Book, related_name="loans", on_delete=models.CASCADE) #Libro prestado
    user = models.ForeignKey(User, related_name="loans", on_delete=models.CASCADE)#Usuario que toma el libro
    loan_date = models.DateField(auto_now_add=True) #Fecha en la cual se presta el libro
    return_date = models.DateField(null=True,blank=True) #Fecha de devolucion , puede estar vacia

    def __str__(self):
        return f"Préstamo de {self.book.title} a {self.user.name} el {self.loan_date}"

