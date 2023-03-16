from django.shortcuts import render
from .models import Todo
from django.http import HttpResponseRedirect

# Create your views here.

def str1(request):
    todo = Todo.objects.all
    context = {'todo':todo}
    return render(request, 'index.html',context)

def tudo1 (request):
    new_todo = Todo ()
    if request.method == 'POST':
        new_todo.title = request.POST.get('title')
        new_todo.description =request.POST.get('description')
        new_todo.created_at =request.POST.get('created_at')
        new_todo.save()
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')
        
def delete_record(request,id):                    
    todo = Todo.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect('/')

def update(request,id):
    todo=Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return HttpResponseRedirect('/')
    return render(request, 'update.html' , {'todo':todo})

