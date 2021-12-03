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

# DELETE ALL
def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)