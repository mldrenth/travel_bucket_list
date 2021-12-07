from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.city import City
from models.country import Country
from models.sight import Sight
import repositories.sight_repository as sight_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

sights_blueprint = Blueprint("sights", __name__)

@sights_blueprint.route("/sights")
def cities():
    sights = sight_repository.select_all()
    return render_template("sights/index.html", title = "Sights", sights = sights)

#NEW
#GET '/countries/new'
@sights_blueprint.route("/sights/new")
def new_sight():
    cities = city_repository.select_all()
    return render_template("sights/new.html", title = "Create New Sight", cities = cities)

#POST '/sights'
@sights_blueprint.route("/sights", methods=['POST'])
def create_sight():
    name = request.form['name']
    category = request.form['category']
    city_id = request.form['city_id']
    visited = "visited" in request.form.keys()
    want_to_visit = "want_to_visit" in request.form.keys()
    city = city_repository.select(city_id)
    sight = Sight(name, category, city, want_to_visit, visited)
    sight_repository.save(sight)
    return redirect('/sights')

# #FILTER
# #GET '/cities/filter/<option>/<state>
# @cities_blueprint.route("/cities/filter/<option>/<state>")
# def show_filtered_cities(option,state):
#     cities = city_repository.filter(option,state)
#     return render_template("cities/index.html", title = "Cities", cities = cities)

# #SEARCH BY NAME
# #GET '/cities/filter/city
# @cities_blueprint.route("/cities/filter/city", methods=["POST"])
# def search_by_name():
#     city_name = request.form['city'].title()
#     cities = city_repository.select_by_name(city_name)
#     return render_template("/cities/index.html", title ="Cities", cities = cities)


# #EDIT
# #GET '/cities/<id>/edit'
# @cities_blueprint.route("/cities/<id>/edit")
# def edit_city(id):
#     city = city_repository.select(id)
#     countries = country_repository.select_all()
#     return render_template('cities/edit.html', title = "Edit City", city = city, countries = countries)


# #UPDATE
# #PUT '/countries/<id>'
# @cities_blueprint.route("/cities/<id>", methods ={'POST'})
# def update_city(id):
#     name = request.form['name']
#     country_id = request.form['country_id']
#     visited = "visited" in request.form.keys()
#     want_to_visit = "want_to_visit" in request.form.keys()
#     country = country_repository.select(country_id)
#     if visited:
#         country.change_visited_status(True)
#     city = City(name, country, want_to_visit, visited, id)
#     city_repository.update(city)
#     country_repository.update(country)
#     return redirect('/cities')

# TOGGLE VISITED STATUS
@sights_blueprint.route("/sights/<id>/edit/visited", methods =['POST'])
def toggle_visited_status(id):
    sight = sight_repository.select(id)
    sight.toggle_visited_status()
    sight_repository.update(sight)
    return redirect('/sights')

# TOGGLE WANT TO VISIT STATUS
@sights_blueprint.route("/sights/<id>/edit/want_to_visit", methods =['POST'])
def toggle_want_to_visit_status(id):
    sight = sight_repository.select(id)
    sight.toggle_want_to_visit_status()
    sight_repository.update(sight)
    return redirect('/sights')

#DELETE
#DELETE '/countries/<id>
@sights_blueprint.route("/sights/<id>/delete", methods=['POST'])
def delete_sight(id):
    sight_repository.delete(id)
    return redirect('/sights')