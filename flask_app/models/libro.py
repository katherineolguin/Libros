from flask_app.config.mysqlconnection import connectToMySQL

#Importo modelos
from flask_app.models import autor

#IMPORTAR FLASH
from flask import flash 

import re #EXPRECIONES REGULARES
#PENDIENTE PONERLAS

class Libro:
    def __init__(self, data):

        self.id = data['id']
        self.titulo = data['titulo']
        self.numero_de_paginas = data['numero_de_paginas']
        self.created_at = data['created_at']
        self.update_time = data['update_time']

        #join
        self.autor_fav = []


    
    @classmethod 
    def save(cls, formulario):
        query = "INSERT INTO libros (titulo, numero_de_paginas) VALUES (  %(titulo)s,  %(numero_de_paginas)s)"
        results = connectToMySQL('esquema_libros_').query_db(query, formulario)

        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * from libros  ORDER BY titulo ASC"
        results = connectToMySQL('esquema_libros_').query_db(query)

        libros= []  #Creo una lista para que me devuelva todos los libros agregados 

        for libro in results:
            libros.append(cls(libro))

        return libros
    

    @classmethod
    def get_libro(cls, data):
        query = "SELECT  * From esquema_libros_.libros LEFT JOIN esquema_libros_.favoritos on libros.id = libro_id LEFT JOIN esquema_libros_.usuarios on libros.id =usuarios.id = usuario_id where libros.id =  %(id)s;"
        result =  connectToMySQL('esquema_libros_').query_db(query, data)

        libro = cls(result[0]) #Creo un diccionario  para devolver el id del autor que quiero a la pagina donde lo mostraré ej: /authors/fav/<int:id>  /authors/fav/<1> -> id:1 = jane 

        for datos in result:
            if datos['usuarios.id'] == None:
                break 

            data = {
                "id": datos['usuarios.id'],
                "nombre": datos['nombre'],
                "apellido": datos['apellido'],
                "created_at":  datos['created_at'],
                "UPDATED_AT": datos['UPDATED_AT']
            }

            libro.autor_fav.append(autor.Author(data))
        
        return libro


    
    @classmethod 
    def libros_no_favoritos (cls, data):

        query = "SELECT * from esquema_libros_.libros WHERE libros.id not in (select libro_id FROM esquema_libros_.favoritos WHERE usuario_id = %(id)s);"

        result = connectToMySQL('esquema_libros_').query_db(query, data)

        libros_no =[]

        for libro in result:

            libros_no.append(cls(libro))

        return libros_no
    
    @classmethod
    def nuevo_autor_favorito(cls, data):

        query= "INSERT INTO esquema_libros_.favoritos (usuario_id, libro_id) VALUES ( %(usuario_id)s, %(libro_id)s);"
        result = connectToMySQL('esquema_libros_').query_db(query, data)

        return result

    



