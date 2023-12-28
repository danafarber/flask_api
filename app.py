""" 

from flask import render_template # Remove: import Flask
from flask.json import JSONEncoder as FlaskJSONEncoder
#import connexion
import config 
from models import Person


# app = connexion.App(__name__, specification_dir="./")
# app.add_api("swagger.yml")
app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

#basic web server and running and makes it respond with a home.html
    

"""


 # app.py

# app.py

""" from flask import render_template
from flask.json import JSONEncoder as FlaskJSONEncoder
from config import connex_app, db, ma  # Import the Connexion app, SQLAlchemy db, and Marshmallow objects
from models import Person

app = connex_app
app.app.json_encoder = FlaskJSONEncoder

@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)

if __name__ == "__main__":
    with app.app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", port=8000, debug=True) """


# app.py

from flask import render_template

import config
from models import Person

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)