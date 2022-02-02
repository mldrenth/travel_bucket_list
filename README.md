# travel_bucket_list

This is a solo project done within 5 days as part of CodeClan's Professional Software Development course.

## Brief
Build an app to track someone's travel adventures.

### MVP:

 * The app should allow the user to track countries and cities they want to visit and those they have visited.
 * The user should be able to create and edit countries
 * Each country should have one or more cities to visit
 * The user should be able to create and delete entries for cities
 * The app should allow the user to mark destinations as visited or still to see

### Possible Extensions:

 * Have separate pages for destinations visited and those still to visit
 * Add sights to the destination cities
 * Search for destination by continent, city or country
 * Any other ideas you might come up with

## About the project
As an avid traveller myself, it was easy for me to choose this topic. With this project, I devolped my skills as a software engineer both from a frontend and a  backend point of view. Within the app, you can create and edit new countries, cities and sights you want to visit and have visited so far. It is interacting with a PostgreSQL database (full CRUD functionality) and is following RESTful conventions. It was built using only :
<ul>
<li>HTML / CSS</li>
<li>Python</li>
<li>Flask</li>
<li>PostgreSQL and psycopg2 </li>
<li> GeonamesCache to gain access to a list of country names </li> </ul>

## This is how it looks:
![App Screenshot](/static/images/app_screenshot.png?raw=true)

## Instructions
### Requirements
You will need the following installed:
- Git
- Python 3
- Flask
- Postgres
- Psycopg2

### How to run
- Create the database by typing "dropdb travel_bucket_list" and then "createdb travel_bucket_list" in the terminal
- In your terminal move to the downloaded folder and enter "psql -d travel_bucket_list -f travel_bucket_list.sql"
- Run console.py with Python 3 to populate the database with examples
- Type "flask run" to start the application and click on the link shown in the terminal
