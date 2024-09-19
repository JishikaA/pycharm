from django.shortcuts import render

from app.forms import TodoForm


# Create your views here.

# def test(request):
#     return render(request,'test.html')

def index(request):
    return render(request,'index.html')

def index_dashboard(request):
    return render(request,'index_dashboard.html')

def test(request):
    data=TodoForm()
    if request.method == "POST":
        todo = TodoForm(request.POST)
        if todo.is_valid():
            todo.save()
    return render(request,'test.html',{"forms":data})