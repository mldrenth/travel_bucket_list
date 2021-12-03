from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", title = "Cities", cities = cities)

#NEW
#GET '/countries/new'
@cities_blueprint.route("/cities/new")
def new_city():
    countries = country_repository.select_all()
    return render_template("cities/new.html", title = "Create New City", countries = countries)

#POST '/cities'
@cities_blueprint.route("/cities", methods=['POST'])
def create_city():
    name = request.form['name']
    country_id = request.form['country_id']
    visited = False
    if "visited" in request.form.keys():
        visited = True
    want_to_visit = False
    if "want_to_visit" in request.form.keys():
        want_to_visit = True
    country = country_repository.select(country_id)
    city = City(name, country, want_to_visit, visited)
    city_repository.save(city)
    return redirect('/cities')

#DELETE
#DELETE '/countries/<id>
@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/cities')