# Main Folder
This folder serves as the root folder for all of our website data.

To do most things with django you will be using manage.py and running it with some sort of comand such as `python manage.py runserver` that we did earlier. Here is a list of a couple of useful ones and what they do

- `python manage.py runserver` run's the server, you can specify -p "PORT" for a certain port
- `python manage.py migrate` When you have a change that is made, but hasn't been synced with the db run this. If django says `You have x amount of unapplied migrations` when you use runserver then this is what you run to make it go away.
- `python manage.py makemigrations` Whenever you make a new Model (I'll explain them later) you will first run makemigrates which will generate the SQL and then `migrate` will sync it with the database

### Django Project Vs Apps
In django a project is a culmination of many apps. A project has a single settings.py and urls.py that everything has to through.

In our case our project is `techsite/` so everything must go through the settings.py and urls.py in that folder.

# Folder Structure
- `manage.py` - Django's command line utility that allows us to easily make migrations, apply migrations and run the local server, commands specified above are the main ones you will need to know
- `techsite/` - This is the PROJECT folder that contains our settings.py and urls.py. These apply for all APPS in our project, an example of an app would be `code_editor/`.
- `code_editor/` -  This is the APP folder, this contains views, urls, models, etc. ONLY FOR THIS APP. Since our current project is scoped small, we will hold most of our code here
