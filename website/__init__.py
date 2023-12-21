from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

#Create the database instance
db = SQLAlchemy()
DB_NAME = 'browserhomepage.db'

def create_app():
    #Initialize Flask
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #Assumes database under root folder of application

    #Establish routes
    from .views import views
    app.register_blueprint(views, url_prefix="/") #Views blueprint used to render root route

    #Initialize database
    db.init_app(app)

    #Create database if does not already exist
    if not path.exists('website/instance/' + DB_NAME):
        from .models import Link

        with app.app_context():
            db.create_all()

        print(f'Created database {DB_NAME}')

    return app
