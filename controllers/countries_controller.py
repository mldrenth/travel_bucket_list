from flask import Flask, render_template, redirect, request
from flask import Blueprint
import geonamescache
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)

gc = geonamescache.GeonamesCache()

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", title = "Countries", countries = countries)

#NEW
#GET '/countries/new'
@countries_blueprint.route("/countries/new")
def new_country():
    all_countries = gc.get_countries_by_names()
    return render_template("countries/new.html", title = "Create New Country", all_countries = all_countries)

#POST '/countries'
@countries_blueprint.route("/countries", methods=['POST'])
def create_country():
    name = request.form['name']
    continent = request.form['continent']
    visited = "visited" in request.form.keys()
    want_to_visit = "want_to_visit" in request.form.keys()
    country = Country(name, continent, want_to_visit, visited)
    country_repository.save(country)
    return redirect('/countries')

#SHOW
#GET '/countries/<id>
@countries_blueprint.route("/countries/<id>")
def show_country(id):
    country = country_repository.select(id)
    cities = city_repository.select_by_country(country)
    return render_template('countries/show.html', title = "Country Info", country = country, cities = cities)

#EDIT
#GET '/countries/<id>/edit'
@countries_blueprint.route("/countries/<id>/edit")
def edit_country(id):
    all_countries = gc.get_countries_by_names()
    country = country_repository.select(id)
    return render_template('countries/edit.html', title = "Edit Country", country = country, all_countries = all_countries)


#UPDATE
#PUT '/countries/<id>'
@countries_blueprint.route("/countries/<id>", methods ={'POST'})
def update_country(id):
    name = request.form['name']
    continent = request.form['continent']
    visited = "visited" in request.form.keys()
    want_to_visit = "want_to_visit" in request.form.keys()
    country = Country(name, continent, want_to_visit, visited, id)
    country_repository.update(country)
    return redirect('/countries')

#DELETE
#DELETE '/countries/<id>
@countries_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/countries')