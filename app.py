from flask import Flask
from views import views


app = Flask(__name__)
app.register_blueprint(views, url_prefix="/") #views blueprint used to render root route

if __name__ == '__main__':
    app.run(debug=True, port=8080) #listen at port 8080, enabling debug causes reload following changes
