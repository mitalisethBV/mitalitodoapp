from django.shortcuts import redirect, render
from my_todolist.models import Task
from django.utils import timezone

# Create your views here.


def mytask(request):
    thank = False
    if request.method=="POST":
        title = request.POST.get("title","")
        
        current_date=timezone.localtime(timezone.now())
 

        data = Task(taskTitle =title,added_date=current_date)
        data.save()
        thank = True
        
    todo_items= Task.objects.all().order_by("added_date")
    context =  {"todo_items":todo_items}
    #todo_items stores all the items given by Todo.objects.all()
    #i.e all the items in database in order by added_date
    return render(request,'mytask.html',context)



def edit_task(request,pk):
    task = Task.objects.get(id=pk)
    context = {'title':task.taskTitle,'id':task.id}
    return render(request, "edit_task.html",context)
def update_task(request, pk):
    task = Task(id=pk)
    if request.method=="POST":
        task.taskTitle = request.POST.get("title","")
        task.added_date=timezone.localtime(timezone.now())
        
        task.save()
        context =  {"todo_items":Task.objects.all()}
        return render(request, "mytask.html",context)
    return render(request, "edit_task.html")
def delete_task(request, pk):
    if pk:
        task = Task.objects.get(id=pk)
        task.delete()
        context =  {"todo_items":Task.objects.all()}
        return redirect("/")

    return render(request,'mytask.html')
def edit_status(request, pk,status):
    if pk:
        task = Task.objects.get(id=pk)
        task.status = status
        task.save()
        context =  {"todo_items":Task.objects.all()}
        return render(request, 'mytask.html',context)
    return render(request,'mytask.html')