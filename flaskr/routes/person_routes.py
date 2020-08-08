from flaskr.db import get_db
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flaskr.models.person import Person

bp = Blueprint('person_routes', __name__)


def save_person(person):
    db = get_db()
    db.execute(
        '''INSERT INTO person(first_name, last_name, age, ethnicity, profession)
           VALUES(?, ?, ?, ?, ?)

        ''',
        (person.first_name, person.last_name, person.age, person.ethnicity, person.job_title)
    )
    db.commit()


def personRoute(app):
    @app.route('/persons')
    def getPerson():
        person = Person("John", "Smith", 30, "African American", "Software Engineer")
        first_name = person.first_name
        last_name = person.last_name
        age = person.age
        ethnicity = person.ethnicity
        job_title = person.job_title

        save_person(person)

        return {
            "First_Name": person.first_name,
            "Last_Name": person.last_name,
            "Age": person.age,
            "Ethnicity": person.ethnicity,
            "Profession": person.job_title
        }

    @app.route('/createperson', methods=['POST'])
    def create_person():
        print(request.path)

        person_json = request.get_json()

        person = Person(person_json['first_name'], person_json['last_name'],
                        person_json['age'], person_json['ethnicity'], person_json['job_title'])

        save_person(person)

        return {}
