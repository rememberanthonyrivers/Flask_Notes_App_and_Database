# the file makes the website folder a package. Now when importing this folder this file will run 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy     # import the SQLAlchemy library
from os import path # this line uses the path module to see if the database exists 
db = SQLAlchemy()   # create a db instance ( database object | instance of the database)
DB_NAME = "database.db"     # name of the database
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Schoolone123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{DB_NAME}'   #   my sql light database is stored at this location 
    db.init_app(app) 
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    from .models import User, Note      #   imported this module to define the methods created in models.py for our user within our database
    create_database(app)
    return app
def create_database(app):       #   this method is going to check if the databse exiits already 
    if not path.exists('website/' + DB_NAME):   #   website is the folder name    
        db.create_all(app=app)  #     create all method creates the app ,  (app) is passed as an arg to tell flask this is the app to create the database for
        print('Created Database!')  #   basic confirmation msg within the terminal 