# people.py

from datetime import datetime
from flask import abort,make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEOPLE = {
    "Fairy": {
        "fname": "Tooth",
        "lname": "Fairy",
        "timestamp": get_timestamp(),
    },
    "Ruprecht": {
        "fname": "Knecht",
        "lname": "Ruprecht",
        "timestamp": get_timestamp(),
    },
    "Bunny": {
        "fname": "Easter",
        "lname": "Bunny",
        "timestamp": get_timestamp(),
    }
}

def create(person):
    lname=person.get("lname")
    fname=person.get("fname")


    if lname and fname not in PEOPLE:
        PEOPLE[lname]= {
            "fname": fname,
            "lname": lname,
            "timestamp": get_timestamp(),

        }
        return PEOPLE[lname],201
    else:
        abort (
            406,
            f"Person with last name {lname} already exists",
        )
        

def read_all():  #Server will run read_all() when it receives an HTTP request to GET /api/people
    return list(PEOPLE.values())
def read_one(lname):
     if lname in PEOPLE:
        return PEOPLE[lname]
     else:
        abort(
            404, f"Person with last name {lname} not found"
        )
    
def update(lname,person):
    if lname in PEOPLE:
        PEOPLE[lname]["fname"]=person.get("fname",PEOPLE[lname]["fname"])
        PEOPLE[lname]["timestamp"]=get_timestamp()
        return PEOPLE[lname]
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )
    

def delete(lname):
    if lname in PEOPLE:
         del PEOPLE[lname]
         return make_response(
            f"{lname} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )

