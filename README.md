
<h1>For Final CS50W project Capstone</h1>

<h2>Requirements:</h2>
            <p>This project satisfied all requirements in Capstone. It is mobile-responsive, have 8 Django models, 
            have Javascript both inline and loaded js file from static.</p>

<ol>Technologies used in this project:
    <li>Django Framework</li>
    <li>Sqlite3</li>
    <li>Javascript</li>
    <li>Fetch Api</li>
    <li>Html</li>
    <li>CSS</li>
</ol>
<h2>Final Capstone Project</h2>
    <p>My final project for CS50W is Project Management SaaS. Users are able to register,create projects to track, each
    project can have many tasks inside and after all each task has been completed, it will update the percentage of
    overall project.</p>

<p>Create superuser with python manage.py createsuperuser. This is optional.</p>
<p>To migrate the server, type python manage.py makemigrations then
 python manage.py migrate
 </p>
<p>To Run the server, type python manage.py runserver  </p>
     
    .
    ├── db.sqlite3 - database
    ├── manage.py
    ├── Pmanage -Main Project Directory
    │   ├── admin.py -Registered models 
    │   ├── apps.py
    │   ├── forms.py
    │   ├── __init__.py
    │   ├── migrations
    │   │  
    │   │   └── __pycache__
    │   │       
    │   ├── models.py
    │   ├── __pycache__
    │   ├── static -Static files such as js and css
    │   │   └── Pmanage 
    │   │       ├── cat_icon_138789.ico
    │   │       ├── icon.ico
    │   │       ├── report.js - Used fetch to get /${id}/reports and show the each elements
    │   │       └── Tiger.jpg   //Picture of my cat
    │   ├── templates
    │   │   └── Pmanage
    │   │       ├── createplan.html 
    │   │       ├── index.html - Shows all created projects with days and teams.
    │   │       ├── layout.html - layout
    │   │       ├── login.html - Login form to login
    │   │       ├── logout.html - Logout
    │   │       ├── Plan.html - Shows a form to create a project
    │   │       ├── projectID.html -shows the task as well as can add new task
    │   │       ├── register.html - register users
    │   │       ├── Release.html - shows the list of released projects
    │   │       ├── Report.html - Can write report for released projects as well as show the prev: reports
    │   │       ├── task.html - can edit the task's percentage 
    │   │       └── Track.html - Shows all the project with percentages as well as can release the project
    │   ├── tests.py
    │   ├── urls.py - shows the routes
    │   └── views.py - contains all applications views 
    ├── projectmanagement
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── README.md
    
Project's video links-https://youtu.be/z3NFk1cT2L0
