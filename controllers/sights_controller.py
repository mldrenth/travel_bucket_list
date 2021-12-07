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
    sight = Sight(name, category, city, visited, want_to_visit)
    sight_repository.save(sight)
    return redirect('/sights')

#FILTER
#GET '/sights/filter/<option>/<state>
@sights_blueprint.route("/sights/filter/<option>/<state>")
def show_filtered_sights(option,state):
    sights = sight_repository.filter(option,state)
    return render_template("sights/index.html", title = "Sights", sights = sights)

#SEARCH BY NAME
#GET '/sights/filter/sight
@sights_blueprint.route("/sights/filter/sight", methods=["POST"])
def search_by_name():
    sight_name = request.form['sight'].title()
    sights = sight_repository.select_by_name(sight_name)
    return render_template("/sights/index.html", title ="Sights", sights = sights)


#EDIT
#GET '/sights/<id>/edit'
@sights_blueprint.route("/sights/<id>/edit")
def edit_sight(id):
    sight = sight_repository.select(id)
    cities = city_repository.select_all()
    return render_template('sights/edit.html', title = "Edit Sight", sight = sight, cities = cities)


#UPDATE
#PUT '/countries/<id>'
@sights_blueprint.route("/sights/<id>", methods ={'POST'})
def update_sight(id):
    name = request.form['name']
    category = request.form['category']
    city_id = request.form['city_id']
    visited = "visited" in request.form.keys()
    want_to_visit = "want_to_visit" in request.form.keys()
    city = city_repository.select(city_id)
    country = country_repository.select(city.country.id)
    if visited:
        country.visited = True
        city.visited = True
    sight = Sight(name, category, city, visited, want_to_visit, id)
    city_repository.update(city)
    country_repository.update(country)
    sight_repository.update(sight)
    return redirect('/sights')

# TOGGLE VISITED STATUS
@sights_blueprint.route("/sights/<id>/edit/visited", methods =['POST'])
def toggle_visited_status(id):
    sight = sight_repository.select(id)
    sight.toggle_visited_status()
    city = city_repository.select(sight.city.id)
    country = country_repository.select(city.country.id)
    if sight.visited:
        country.visited = True
        city.visited = True
    sight_repository.update(sight)
    city_repository.update(city)
    country_repository.update(country)
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