# travel_bucket_list

This was done within 5 days as part of CodeClan's Professional Software Development course.
The brief can be found <a href="https://github.com/codeclan/g28_classnotes/blob/main/python_projects/project_briefs/Travel_Bucket_List.md"> here</a>.

As an avid traveller myself, it was easy for me to choose this topic. With this project, I devolped my skills as a software engineer both from a frontend and a  backend point of view. Within the app, you can create and edit new countries, cities and sights you want to visit and have visited so far. It is interacting with a PostgreSQL database (full CRUD functionality) and is following RESTful conventions. It was built using only :
<ul>
<li>HTML / CSS</li>
<li>Python</li>
<li>Flask</li>
<li>PostgreSQL and psycopg2 </li>
<li> GeonamesCache to gain access to a list of country names </li> </ul>

### This is how it looks:
![App Screenshot](/static/images/app_screenshot.png?raw=true)

### Instructions
<ol>
<li>Create a database called "travel_bucket_list"</li>
<li>In your terminal move to the downloaded folder and enter "psql -d travel_bucket_list -f travel_bucket_list.sql</li>
<li> Run console.py with Python 3 to populate the database with examples</li>
<li> Type "flask run" to start the application and click on the link shown in the terminal </li>
