from django.shortcuts import render,redirect
from django.db.models import Q
from .models import TODOLIST,History

# Create your views here.
def home(request):
    temp = True
    if request.method == 'POST':
        task = request.POST.get('task')
        description = request.POST.get('description')
        
        a = TODOLIST.objects.create(task = task,description=description)
    return render(request,'home.html',{'temp':temp}) # no error



def display(request):
    search_bar = True
    todo_data = TODOLIST.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')
        todo_data = TODOLIST.objects.filter(Q(task__icontains = search))
    context = {'todo_data':todo_data,
               'search_bar':search_bar}
    return render(request,'display.html',context) #no error


def update(request,ud):
    temp = False
    todo_data = TODOLIST.objects.get(id = ud)
    context = {'todo_data':todo_data,
               'temp':temp}

    if request.method == 'POST':
        task = request.POST.get('task')
        description = request.POST.get('description')

        todo_data.task = task
        todo_data.description = description
        todo_data.save()
        return redirect('display')
    return render(request,'update.html',context)

def single(request,pk):
    todo_data = TODOLIST.objects.get(id = pk)
    context = {'todo_data':todo_data}
    return render(request,'single.html',context)


def complete(request,com):
    todo_data = TODOLIST.objects.get(id = com)
    History.objects.create(task = todo_data.task,description = todo_data.description)
    todo_data.delete()
    return redirect('display')


def history(request):
    history = History.objects.all().order_by('-id')
    context = {'history':history}
    return render(request,'history.html',context)


def delete(request,dl):
    history = History.objects.get(id = dl)
    history.delete()
    return redirect('history')


    