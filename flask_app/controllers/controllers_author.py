from flask import render_template, redirect, request, session, flash
from flask_app import app

#IMPORTAR MODELOSS
from flask_app.models.autor import Author
from flask_app.models.libro import Libro



#IMPORTAR BCRYPT
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index ():

    #lista con todos los autores
    autores = Author.get_all()



    return render_template ('new_author.html', autores=autores)


@app.route('/new/author', methods=['post'])
def new_author():

    #Poner validacion autor

    #Guardar author
    Author.save(request.form)
    



    
    return redirect ('/')

@app.route('/authors/fav/<int:id>')
def autor_fav(id):
    data = {
        "id":id
    }
    autor = Author.get_autor(data)  # para devolder el nombre del autor
    libros_no_favoritos = Libro.libros_no_favoritos(data)
    


    return render_template ('autors_fav.html', autor=autor, libros_no_favoritos=libros_no_favoritos)



@app.route('/add/book/fav', methods=['POST'])
def guardar_nuevo_favorito():
    data = {
        'libro_id': request.form['libro_id'],
        'usuario_id': request.form['usuario_id']
        
    }
    Author.nuevo_book_favorito(data) #Llamo a la clase Author y a la funcion que guarda los libros favoritos
    return redirect (f"/authors/fav/{request.form['usuario_id']}")
    #retorno a la pagina de autores favoritos tomando el id del usuario desde el formulario
