from flask_app import app

# Importar controlador
#DEBEMOS IMPORTAR TODOS LOS CONTROLADORES

from flask_app.controllers import controllers_author
from flask_app.controllers import controllers_libro

# from flask_app.controllers import users_controllers

#Ejecutamos variable app
if __name__=="__main__":
    app.run(debug =True)
