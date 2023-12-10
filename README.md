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