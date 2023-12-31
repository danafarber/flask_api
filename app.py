
# app.py

from flask import abort, render_template
import config
from models import Person

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)


@app.route('/people/<string:lname>')
def get_person(lname):
    person = Person.query.get(lname)
    if person is None:
        abort(404)

    return render_template("user.html", person=person)








@app.route('/people/<string:lname>',methods=["DELETE"])
def delete_person(lname):
    person = Person.query.get(lname)
    if person is None:
        abort(404)
    
    person.delete_person()

    return f"Person {lname} deleted successfully", 204



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)