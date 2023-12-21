from . import db

class Link(db.Model):
            LinkID = db.Column(db.Integer, primary_key=True)
            LinkName = db.Column(db.String(50))
            LinkURL = db.Column(db.String(255))
            Category = db.Column(db.String(50))
