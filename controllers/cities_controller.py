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
    visited = "visited" in request.form.keys()
    want_to_visit = "want_to_visit" in request.form.keys()
    country = country_repository.select(country_id)
    city = City(name, country, want_to_visit, visited)
    city_repository.save(city)
    return redirect('/cities')

#SHOW
#GET '/cities/<id>
@cities_blueprint.route("/cities/<id>")
def show_city(id):
    city = city_repository.select(id)
    return render_template('cities/show.html', title = "City Info", city = city)

#FILTER
#GET '/cities/filter/<option>/<state>
@cities_blueprint.route("/cities/filter/<option>/<state>")
def show_filtered_cities(option,state):
    cities = city_repository.filter(option,state)
    return render_template("cities/index.html", title = "Cities", cities = cities)

#SEARCH BY NAME
#GET '/cities/filter/city
@cities_blueprint.route("/cities/filter/city", methods=["POST"])
def search_by_name():
    city_name = request.form['city'].capitalize()
    cities = city_repository.select_by_name(city_name)
    return render_template("/cities/index.html", title ="Cities", cities = cities)


#EDIT
#GET '/cities/<id>/edit'
@cities_blueprint.route("/cities/<id>/edit")
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template('cities/edit.html', title = "Edit City", city = city, countries = countries)


#UPDATE
#PUT '/countries/<id>'
@cities_blueprint.route("/cities/<id>", methods ={'POST'})
def update_city(id):
    name = request.form['name']
    country_id = request.form['country_id']
    visited = "visited" in request.form.keys()
    want_to_visit = "want_to_visit" in request.form.keys()
    country = country_repository.select(country_id)
    if visited:
        country.change_visited_status(True)
    city = City(name, country, want_to_visit, visited, id)
    city_repository.update(city)
    country_repository.update(country)
    return redirect('/cities')

# TOGGLE VISITED STATUS
@cities_blueprint.route("/cities/<id>/edit/visited", methods =['POST'])
def toggle_visited_status(id):
    city = city_repository.select(id)
    city.toggle_visited_status()
    city_repository.update(city)
    return redirect('/cities')

# TOGGLE WANT TO VISIT STATUS
@cities_blueprint.route("/cities/<id>/edit/want_to_visit", methods =['POST'])
def toggle_want_to_visit_status(id):
    city = city_repository.select(id)
    city.toggle_want_to_visit_status()
    city_repository.update(city)
    return redirect('/cities')

#DELETE
#DELETE '/countries/<id>
@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/cities')