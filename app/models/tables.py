from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)

    @property
    def is_authenticated (self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.email = email
        self.name = name

    def __repr__(self):
        return '<Usuário %r>' % self.username

