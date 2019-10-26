from flask import Flask, redirect, url_for, request
from config import Conf
from flask_sqlalchemy import SQLAlchemy
import sqlite3


from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_security import current_user
from flask_login import LoginManager

### Инициализация приложения ###

app = Flask(__name__)
app.config.from_object(Conf)

### Создание БД ###

db = SQLAlchemy(app)

### Создание курсосра и соединения с БД ###

conn = sqlite3.connect(r"data/db.db")
cursor = conn.cursor()

login_manager = LoginManager(app)
login_manager.setup_app(app)

### Миграции ###
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

### Админка ###
from mod import *

# class AdminView(ModelView):
#
#     def is_accessible(self):
#         return login.current_user.is_admin
#
#     def inaccessible_callback(self, name, **kwargs):
#         # redirect to login page if user doesn't have access
#         return redirect(url_for('login', next=request.url))

admin = Admin(app)
# admin.add_view(AdminView(Post, db.session))
# admin.add_view(AdminView(User, db.session))
# admin.add_view(AdminView(Tag, db.session))

admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Tag, db.session))

