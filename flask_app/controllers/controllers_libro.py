from flask import render_template, redirect, request, session, flash
from flask_app import app

#IMPORTAR MODELOSS
from flask_app.models.autor import Author
from flask_app.models.libro import Libro



#IMPORTAR BCRYPT
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/libro')
def libros():

    #lista con todos los autores
    libros = Libro.get_all()

    return render_template ('new_book.html', libros=libros)


@app.route('/new/book', methods=['post'])
def new_libro():

    #Poner validacion autor

    #Guardar author
    Libro.save(request.form)

    return redirect ('/libro')

@app.route('/books/fav/<int:id>')
def libro_fav(id):
    data = {
        "id":id
    }
    libro = Libro.get_libro(data)  # para devolder el nombre del autor
    autor_no_favorito = Author.autor_no_favorito(data)

    return render_template ('books_fav.html', libro=libro, autor_no_favorito=autor_no_favorito)


@app.route('/add/autor/fav', methods=['POST'])
def guardar_favorito():
    data = {
        'libro_id': request.form['libro_id'],
        'usuario_id': request.form['usuario_id']
        
    }
    Libro.nuevo_autor_favorito(data) #Llamo a la clase Author y a la funcion que guarda los libros favoritos
    return redirect (f"/books/fav/{request.form['usuario_id']}")
    #retorno a la pagina de autores favoritos tomando el id del usuario desde el formulario