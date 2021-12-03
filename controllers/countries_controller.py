from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", title = "Countries", countries = countries)

#NEW
#GET '/countries/new'
@countries_blueprint.route("/countries/new")
def new_country():
    return render_template("countries/new.html", title = "Create New Country")

#POST '/countries'
@countries_blueprint.route("/countries", methods=['POST'])
def create_country():
    name = request.form['name']
    continent = request.form['continent']
    visited = False
    if "visited" in request.form.keys():
        visited = True
    want_to_visit = False
    if "want_to_visit" in request.form.keys():
        want_to_visit = True
    country = Country(name, continent, want_to_visit, visited)
    country_repository.save(country)
    return redirect('/countries')