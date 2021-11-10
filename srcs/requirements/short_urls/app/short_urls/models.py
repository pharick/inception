from . import db


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), unique=True, nullable=False)
    hash = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'url: {self.url}, hash: {self.hash}'
