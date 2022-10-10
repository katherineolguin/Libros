from flask_app.config.mysqlconnection import connectToMySQL
#importo de modelos  libro.PY
from flask_app.models import libro

#IMPORTAR FLASH
from flask import flash

import re #EXPRECIONES REGULARES
#PENDIENTE PONERLAS

class Author:
    def __init__ (self, data):

        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.created_at = data['created_at']
        self.UPDATED_AT = data['UPDATED_AT']

    #JOIN LIBROS
        self.libros_fav = []



    @classmethod 
    def save(cls, formulario):
        query = "INSERT INTO usuarios (id, nombre, apellido) VALUES (%(id)s, %(nombre)s,  %(apellido)s)"
        results = connectToMySQL('esquema_libros_').query_db(query, formulario)

        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * from usuarios  ORDER BY nombre ASC"
        results = connectToMySQL('esquema_libros_').query_db(query)

        autores= []  #Creo una lista para que me devuelva todos los autores agregados 

        for autor in results:
            autores.append(cls(autor))

        return autores 
    
    @classmethod
    def get_autor(cls, data):
        query = "SELECT * From esquema_libros_.usuarios LEFT JOIN esquema_libros_.favoritos on usuarios.id = usuario_id LEFT JOIN esquema_libros_.libros on libros.id = libro_id where usuarios.id = %(id)s;"
        result =  connectToMySQL('esquema_libros_').query_db(query, data)

        autor = cls(result[0]) #Creo un diccionario  para devolver el id del autor que quiero a la pagina donde lo mostraré ej: /authors/fav/<int:id>  /authors/fav/<1> -> id:1 = jane 

        for datos in result:      #detengo el mostrar libros si no tengo datos en libros.id
            if datos['libros.id'] == None:   
                break 

#Para llamar a los libros favoritos tengo que hacer la iniciacion de la clase libros junto con sus rutas y metodos de clase, asi puedo obtener la instancia "libro" que he creado 

            data = {
                "id": datos['libros.id'],
                "titulo": datos['titulo'],
                "numero_de_paginas": datos['numero_de_paginas'],
                "created_at": datos['created_at'],
                "update_time": datos['update_time']


            }

            autor.libros_fav.append(libro.Libro(data))


        return autor


    @classmethod 
    def autor_no_favorito(cls, data):

        query = "SELECT * from esquema_libros_.usuarios WHERE usuarios.id not in (select usuario_id FROM esquema_libros_.favoritos WHERE libro_id = %(id)s);"

        result = connectToMySQL('esquema_libros_').query_db(query, data)

        autores =[]

        for fila in result:

            autores.append(cls(fila))

        return autores
    
    @classmethod
    def nuevo_book_favorito(cls, data):

        query= "INSERT INTO esquema_libros_.favoritos (usuario_id, libro_id) VALUES ( %(usuario_id)s, %(libro_id)s);"
        result = connectToMySQL('esquema_libros_').query_db(query, data)

        return result

    

    


