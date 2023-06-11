from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoListItem, ToDoTables


def todoappView(request):
    all_todo_items = ToDoListItem.objects.all()
    tables = ToDoTables.objects.all()
    return render(request, 'todo/index.html',
    {'all_items':all_todo_items,
    'tables':tables})

def addTodoView(request, table_id):
    x = request.POST['content']
    table = ToDoTables.objects.get(id= table_id)
    new_item = ToDoListItem(content=x, todo_tables=table)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request, i):
    y = ToDoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')

def addToDoTable(request):
    x = request.POST['new_table']
    new_item = ToDoTables(name_table = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteToDoTable(request, table):
    y = ToDoTables.objects.get(id= table)
    y.delete()
    return HttpResponseRedirect('/todoapp/')