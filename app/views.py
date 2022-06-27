from django.shortcuts import render
from django.shortcuts import HttpResponse
from app.models import Task

# Create your views here.
def home_view(request):
    context = {'success': False}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task (task=title,desc=desc)
        ins.save()
        context = {'success': True}
    return render(request, 'app/home.html', context)

def task_view(request):
    allTask = Task.objects.all()
    print(allTask)
    context = {'task': allTask}
    return render(request, 'app/task.html', context )