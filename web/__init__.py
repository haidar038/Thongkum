from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_toastr import Toastr
from flask_login import LoginManager
from flask_admin import Admin

db = SQLAlchemy()
toast = Toastr()
login_manager = LoginManager()
admin = Admin(name='Admin', template_mode='bootstrap4')

DB_NAME = 'thongkum.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hadeethongkum'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['FLASK_ADMIN_SWATCH'] = 'simplex'
    db.init_app(app)
    toast.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)

    from web.auth.routes import auth
    from web.views.routes import views

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    # from web import models

    with app.app_context():
        db.create_all()

    return app