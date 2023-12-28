# app.py

from flask import render_template # Remove: import Flask
from flask.json import JSONEncoder
import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

#basic web server and running and makes it respond with a home.html """
    

