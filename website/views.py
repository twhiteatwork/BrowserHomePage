from flask import Blueprint, render_template, request, jsonify, redirect, url_for

Views = Blueprint('Views', __name__)

#Parameter of name passed to template
@Views.route('/')
def home():
    return render_template('index.html', name='Ted')

#variable value of username in route used as parameter to template
@Views.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', name=username)

#variable value of username in querystring used as parameter to template
@Views.route('/profileqs')
def profileqs():
    args = request.args
    username = args.get("name")
    return render_template("index.html", name=username)

#return some json using jsonify
@Views.route('/json')
def gimme_json():
    return jsonify({'name': 'Ted', 'level': 10})

#ingest json data
@Views.route('/data')
def ingest_json_data():
    data = request.json
    return jsonify(data)

#redirect to a particular view, home
@Views.route('/go-to-home')
def go_to_home():
    return redirect(url_for('views.home'))