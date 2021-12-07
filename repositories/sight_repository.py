from pdb import run
from db.run_sql import run_sql
from psycopg2 import sql as sql_test
from models.country import Country
from models.city import City
from models.sight import Sight
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

# Create
def save(sight):
    sql = "INSERT INTO sights (name, category, city_id, visited, want_to_visit) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [sight.name,sight.category, sight.city.id, sight.visited, sight.want_to_visit]
    results = run_sql(sql, values)
    id = results[0]['id']
    sight.id = id
    return sight

# SELECT ALL
def select_all():
    sights = []
    sql = "SELECT * from sights"
    results = run_sql(sql)
    for row in results:  
        city = city_repository.select(row['city_id'])
        sight = Sight(row['name'],row['category'], city, row['visited'], row['want_to_visit'], row['id'])
        sights.append(sight)
    return sights

# SELECT BY ID
def select(id):
    sight = None
    sql = "SELECT * FROM sights WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city = city_repository.select(result['city_id'])
        sight = Sight(result['name'],result['category'], city, result['visited'], result['want_to_visit'], result['id'])
    return sight

# SELECT BY CITY
def select_by_city(city):
    sights = []
    sql = "SELECT sights.* FROM sights WHERE city_id = %s"
    values = [city.id]
    results = run_sql(sql, values)

    for row in results:
        sight = Sight(row['name'],row['category'], city, row['visited'], row['want_to_visit'], row['id'])
        sights.append(sight)
    return sights

# SELECT BY NAME
def select_by_name(sight_name):
    sights = []
    sql = "SELECT * FROM sights WHERE name = %s"
    values = [sight_name]
    results = run_sql(sql, values)
    for row in results: 
        city = city_repository.select(row['city_id'])
        sight = Sight(row['name'],row['category'], city, row['visited'], row['want_to_visit'], row['id'])
        sights.append(sight)
    return sights



# FILTER
def filter(option,state):
    sights = []
    boolean_state = state == "true"
    #Formating sql query string to pass in column via browser
    sql = sql_test.SQL("SELECT * FROM sights WHERE {column} = %s").format(column=sql_test.Identifier(option))
    values = [boolean_state]
    results = run_sql(sql,values)
    for row in results: 
        city = city_repository.select(row['city_id'])
        sight = Sight(row['name'],row['category'], city, row['visited'], row['want_to_visit'], row['id'])
        sights.append(sight)
    return sights

# UPDATE
def update(sight):
    sql = "UPDATE sights SET (name, category, city_id, visited, want_to_visit) = (%s,%s, %s, %s, %s) WHERE id = %s"
    values = [sight.name, sight.category, sight.city.id, sight.visited, sight.want_to_visit, sight.id]
    run_sql(sql, values)


# DELETE ALL
def delete_all():
    sql = "DELETE FROM sights"
    run_sql(sql)

#DELETE BY ID
def delete(id):
    sql = "DELETE FROM sights WHERE id = %s"
    values = [id]
    run_sql(sql,values)