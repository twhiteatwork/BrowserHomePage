from flask import Flask
from .views import Views
from .auth import Auth

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dslkvkck sdfkjsdfk sdfkjksdf'
    
    app.register_blueprint(Views, url_prefix="/") #Views blueprint used to render root route
    app.register_blueprint(Auth, url_prefix="/") #Auth blueprint used to render root route

    return app