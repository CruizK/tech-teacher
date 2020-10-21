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