### Create tasks folder

`mkdir tasks`

### Start Django project
`django-admin startproject config .`

### Start local server
`py manage.py runserver`

### Creating a new service named tasks

`py manage.py startapp tasks`

### Creating model Task
- id
- title
- description (optional)

### Make migration and migrate
`py manage.py makemigrations`
`py manage.py migrate`

##### Now database is ready


### It is time to write new data into database using Django Admin
1. First create a new superuser
   `py manage.py createsuperuser`
2. Enter to admin panel
   `http://127.0.0.1:8000/admin`
3. Enter your login and password


### Go to admin.py file inside service
1. Import Task model
2. Register model
`admin.site.register(Task)`