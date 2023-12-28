import pathlib

import connexion
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir=basedir)

app = connex_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'people.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
# config.py
"""
import os
import pathlib
import sqlite3
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import marshmallow

basedir = pathlib.Path(__file__).parent.resolve()

def create_app():
    connex_app = connexion.App(__name__, specification_dir=basedir)

    app = connex_app.app
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI", f"sqlite:///{basedir / 'people.db'}")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)  # Initialize SQLAlchemy
    marshmallow.init_app(app)  # Initialize Marshmallow

    return connex_app

connex_app = create_app()
"""