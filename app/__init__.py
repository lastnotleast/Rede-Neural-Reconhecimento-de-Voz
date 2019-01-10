from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config.from_object('config')


db = SQLAlchemy(app)
Migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager(app)

socketio = SocketIO(app)

from app.models import tables
from app.controllers import default



