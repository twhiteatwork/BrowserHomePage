from flask import Blueprint, render_template, request, jsonify
from . import db
from .models import Link
import json

views = Blueprint('views', __name__)

#home: Show categories and links
@views.route('/', methods=['GET', 'POST'])
def home():
    Categories = db.session.execute(db.select(Link.Category).distinct())
    Links = Link.query.all()
    return render_template('home.html', Categories=Categories, Links=Links)

#add: Add new links
@views.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST': 
        LinkName = request.form.get('LinkName') #Gets the URL from the form post 
        LinkURL = request.form.get('LinkURL') #Gets the LinkURL from the form post 
        Category = request.form.get('Category') #Gets the Category from the form post 

        print(LinkName, LinkURL, Category)

        new_link = Link(LinkName = LinkName, LinkURL = LinkURL, Category = Category)
        db.session.add(new_link)
        db.session.commit()
        print('Added new link to database')
    
    return render_template('add.html')

#deleteLink: Delete selected link upon button click
@views.route('/delete', methods=['POST'])
def deleteLink():  
    DeleteReq = json.loads(request.data) # this function expects a JSON from the static/index.js file 
    LinkIDToDelete = DeleteReq['LinkID']
    if LinkIDToDelete:
        Link.query.filter_by(LinkID=LinkIDToDelete).delete()
        db.session.commit()
        print(f'Link {LinkIDToDelete} deleted!')

    return jsonify({})
