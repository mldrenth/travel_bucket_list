from pdb import run
from db.run_sql import run_sql
from psycopg2 import sql as sql_test

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

# SELECT BY ID
def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result['name'], result['continent'], result['want_to_visit'], result['visited'], result['id'])
    return country

# FILTER
def filter(option,state):
    countries = []
    boolean_state = state == "true"
    #Formating sql query string to pass in column via browser
    sql = sql_test.SQL("SELECT * FROM countries WHERE {column} = %s").format(column=sql_test.Identifier(option))
    values = [boolean_state]
    results = run_sql(sql,values)
    for row in results:
        country = Country(row['name'], row['continent'], row['want_to_visit'], row['visited'], row['id'])
        countries.append(country)
    return countries

# UPDATE
def update(country):
    sql = "UPDATE countries SET (name, continent, visited, want_to_visit) = (%s, %s, %s, %s) WHERE id = %s"
    values = [country.name, country.continent, country.visited,country.want_to_visit, country.id]
    run_sql(sql, values)



# DELETE ALL
def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

#DELETE BY ID
def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql,values)