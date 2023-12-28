# people.py


from flask import abort,make_response
from config import db
from models import Person, people_schema, person_schema



""" def create(person):
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
      """   

def read_all():  #Server will run read_all() when it receives an HTTP request to GET /api/people  --> after db: return all the data in the person db
    people=Person.query.all()
    return people_schema.dump(people)  #serialize  Python objects with .dump()


def read_one(lname):
     person=Person.query.filter(lname==Person.lname).one_or_none()  #return one or none
     if person is not None:
        return person_schema.dump(person) 
     else:
        abort(
            404, f"Person with last name {lname} not found"
        )



def create(person): #write to db
    lname=person.get("lname")
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()
    if existing_person is None:
        newPerson=person_schema.load(person,session=db.session)
        db.session.add(newPerson)
        db.session.commit()
        return person_schema.dump(newPerson), 201
    else:
        abort(
            406, f"Person with last name {lname} already exists"
        )


    
def update(lname,person):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()
    if existing_person is not None:
        updatePerson=person_schema.load(person,session=db.session)
        existing_person.fname=updatePerson.fname
        db.session.merge(existing_person)
        db.session.commit()
        return person_schema.dump(existing_person), 201
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )
    

def delete(lname):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()
    if existing_person is not None:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(
            f"{lname} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )

