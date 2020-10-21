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

# Models
Here I will talk about models, they are pretty simple if you understand the basics of either a database or just an excel spreadsheet. If you know databases, a model is literally just a table from SQL. Here's a basic example of a model based on something we might create:

```python

from django.db import models # First we import models

class CourseTutorial(models.Model):
  tutorial_title = models.CharField(max_length=200) # Make a field named tutorial_title and set it's possible value of characters, of max length 200
  tutorial_text = models.TextField() # Similar to tutorial_title, but made for long strings of text
  created_date = models.DateTimeField() # A date and time of when this was created, given the name "date created" instead of created_date
```
Let's break it down line by line

1. `from django.db import models` - We look through django, more specificly the db section and import into our code "models" which is needed to make any model
2. `class CourseTutorial(models.Model)` - We create a python class which INHERITS models.model. This is just a way of telling django "This is a model, give me special model functions"
3. `tutorial_title = models.CharField(max_length=200) ` - So every variable inside of our class counts as a "Field" similar to columns in SQL. In this case our field is named "tutorial_title" and it has to be characters, of max length 200
4. `tutorial_text = models.TextField()` - Similar to tutorial_text, but TextField is made for very long strings of text
5. `created_date = models.DateTimeField()` - This creates a created_date field that is a date and a time.

If you understand SQL this should be pretty familiar. If not then think of excel, but each sheet is a specific model and every COLUMN can only be entered by what we specify, whether it be a number, string of text, or a date.

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

So we have a function(def) called index that takes in (request) and returns an HttpResponse in which we supply some text. So all this function does is return the text specified into it which is `Hello World`.

Our views.py looks like this however
```python
from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'title': "This is some title",
    'items': [
      "This is item 1",
      "This is item 2",
      "This is item 3"
    ]
  }
  return render(request, 'code_editor/index.html', context)
```

Now most of it is similar: `def index(request):`. Context is just a map of some data, a title with a string "this is some title" and then a list of items numbered. The main difference is the last line `return render(request, 'code_editor/index.html', context)`. This allows us to use templates.

# Templates
Templates are where our HTML is stored, note not our CSS or JS is stored here, but we can do it inline for now as loading what are known as "static" assets are a little different in django.

To understand templates let's look at how we call one, like we did before

```python
return render(request, 'code_editor/index.html', context)
```

The arguments in order are
1. The request passed down to the function from django, will never change
2. Where the template is stored, without the root template folder, since django already knows that it is somewhere in there. So for this instance the actual file path is: `templates/code_editor/index.html` but we cut off `templates/` since django knows its a template
3. Finally the reason why templates are used over just plain HTML is context, or simply the data we pass into the template. This can be literally anything we want. In the view example its some static data, but most of the time it will be data we get from our models

First some template syntax: `{% something %}` curly braces with percent signs stands for "This is FUNCTIONALITY django will do for us". NOTE: You will also most of the time have to specify `{% endsomething %}` when doing something functional in the template. `{{ something }}` double curly braces stands for "This is DATA django will insert into the HTML"

So if you peek into the code_editor template folder you will see 2 files base.html and index.html. base.html is simply all the boilerplate HTML, with 2 django template `{% block something %}` tags. These allow us to "extend" this template and then just add stuff to the blocks instead of rewriting the whole HTML page every time we make a new file. You can literally think of a block as "Something will be put in here from another file most likely, BUT if they don't specify it then put what I have in here"

In the index.html we specify that we are extending "base.html" and then put two `{% block %}` tags override both the "title" to set it to what our context is and "content" so we can loop through our list and insert what we have in there, in the HTML.