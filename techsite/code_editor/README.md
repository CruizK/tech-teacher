# Our Main App Folder
This will hold most of our code currently, if the project grows too much in size we can split this code into many different apps that allow them to be decoupled.

# File Structure
- `migrates/` - This is a folder maintined by django that stores migrations, you will not need to worry about it for most uses.
- `temapltes/code_editor/` - This holds our "templates" which is just "HTML,CSS,JS, but we can inject data from our server before we render the page" Look below for more details about templates.
- `init.py` - Django file, ignore
- `admin.py` - For registering files to our admin dashboard, more about models and the admin dashboard below
- `apps.py` - This holds any APP specific configurations, not needed for most uses.
- `models.py` - This holds all of our models, more on models below
- `tests.py` - When our app is actually working, we can run tests so that when we change something we can make sure nothing else broke, which can happen a lot when working in teams.
- `urls.py` - This stores all of our APP routes, more on routes below
- `views.py` - This stores all of our views, this is the code that executes when someone goes to a route specified in `urls.py`

# Routes & Views
Let's take a look at the code in urls.py
```python
# URLS.PY
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index")
]
```

So we have urlpatterns which is a list of "routes", let's take a look at how a route is specified: `path('', views.index, name="index")`, So we provide 3 arguments. these 3 arguments are:
1. The Route - A string that specifies that if someone goes to "ourwebsite.com/" and then the route it will execute the code the view specifies
2. The View - This is the actual code that gets run when someone goes to the URL, it can be literally anything, but most of the time is an HTTP response with some text or HTML.
3. The Name - This is whatever you want to call the route, should be unique in the app, used in templates

In this example the route is: `''` which means that if the url is just "ourwebsite.com" or "ourwebsite.com/" it will execute the view.index code. Let's say our views.py file looks like this:
```python
# VIEWS.py
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World")
```

So we have a function(def) called index that takes in (request) and returns an HttpRespone in which we supply some text. So all this function does is return the text specified into it which is `Hello World`.