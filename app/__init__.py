from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap
from config import Config
from prometheus_flask_exporter import PrometheusMetrics, Counter


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
admin = Admin(app)
bootstrap = Bootstrap(app)
metrics = PrometheusMetrics(app)


from app import routes, models

