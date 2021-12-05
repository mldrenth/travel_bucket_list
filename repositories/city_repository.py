from pdb import run
from db.run_sql import run_sql
from psycopg2 import sql as sql_test
from models.country import Country
from models.city import City
import repositories.country_repository as country_repository

# Create
def save(city):
    sql = "INSERT INTO cities (name, country_id, visited, want_to_visit) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [city.name, city.country.id, city.visited, city.want_to_visit]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

# SELECT ALL
def select_all():
    cities = []
    sql = "SELECT * from cities"
    results = run_sql(sql)
    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['want_to_visit'], row['visited'], row['id'])
        cities.append(city)
    return cities

# SELECT BY ID
def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select(result['country_id'])
        city = City(result['name'], country, result['want_to_visit'], result['visited'], result['id'])
    return city

# SELECT BY COUNTRY
def select_by_country(country):
    cities = []
    sql = "SELECT cities.* FROM cities WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['name'], country, row['want_to_visit'], row['visited'], row['id'])
        cities.append(city)
    return cities

# FILTER
def filter(option,state):
    cities = []
    boolean_state = state == "true"
    #Formating sql query string to pass in column via browser
    sql = sql_test.SQL("SELECT * FROM cities WHERE {column} = %s").format(column=sql_test.Identifier(option))
    values = [boolean_state]
    results = run_sql(sql,values)
    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['want_to_visit'], row['visited'], row['id'])
        cities.append(city)
    return cities

# UPDATE
def update(city):
    sql = "UPDATE cities SET (name, country_id, visited, want_to_visit) = (%s, %s, %s, %s) WHERE id = %s"
    values = [city.name, city.country.id, city.visited, city.want_to_visit, city.id]
    run_sql(sql, values)


# DELETE ALL
def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

#DELETE BY ID
def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql,values)