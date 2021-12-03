from pdb import run
from db.run_sql import run_sql

from models.country import Country
from models.city import City

# Create
def save(country):
    sql = "INSERT INTO countries (name, continent, visited, want_to_visit) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [country.name, country.continent, country.visited, country.want_to_visit]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

# SELECT ALL
def select_all():
    countries = []
    sql = "SELECT * from countries"
    results = run_sql(sql)
    for row in results:
        country = Country(row['name'], row['continent'], row['want_to_visit'], row['visited'], row['id'])
        countries.append(country)
    return countries


# DELETE ALL
def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)