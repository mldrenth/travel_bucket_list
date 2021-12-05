from flask import Flask, render_template
import repositories.country_repository as country_repository
import geonamescache
from controllers.countries_controller import countries_blueprint
from controllers.cities_controller import cities_blueprint


app = Flask(__name__)

app.register_blueprint(countries_blueprint)
app.register_blueprint(cities_blueprint)

gc = geonamescache.GeonamesCache()


@app.route("/")
def home():
    all_countries = gc.get_countries_by_names()
    sum_of_all_countries = len(all_countries)
    all_countries_of_user_visited = country_repository.filter("visited", "true")
    sum_of_all_user_countries = len(all_countries_of_user_visited)
    percentage = (sum_of_all_user_countries * 100) // sum_of_all_countries
    return render_template(
        "index.html", title="Home", percentage = percentage
    )


if __name__ == "__main__":
    app.run(debug=True)
