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

#Creating a function to select all countries in the database by continent, taking in a continent name as the parameter
#1. Create an empty list to store all countries in that match the search
#2. Write the SQL query string that returns all countries from my database where the continent 
# equals the chosen value
#3. Store the continent name outside of the string in a values variable
#4. Store the results of the run_sql function with the query string and values
#5. Loop over the results, creating a country object for each row
#6. Append the countries to the list created at the start of the function
#7. Return the list


#SELECT BY CONTINENT
def select_by_continent(continent):
    countries = []
    sql = "SELECT * FROM countries where continent = %s"
    values = [continent]
    results = run_sql(sql, values)
    for row in results:
        country = Country(row['name'], row['continent'], row['want_to_visit'], row['visited'], row['id'])
        countries.append(country)
    return countries

#SELECT BY NAME
def select_by_name(country_name):
    countries = []
    sql = "SELECT * FROM countries where name = %s"
    values = [country_name]
    results = run_sql(sql, values)
    for row in results:
        country = Country(row['name'], row['continent'], row['want_to_visit'], row['visited'], row['id'])
        countries.append(country)
    return countries

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