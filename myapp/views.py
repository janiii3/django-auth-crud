from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task, Task2 #UTILIZANDO ESTE MODELO PUEDO HACER CONSULTAS
from .forms import CreateNewTask, CreateNewProject, TaskForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone 
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    title = 'Django course!!'
    return render(request, 'index.html', {
        'title': title #con esto y poniendo doble llave en el index.html, mete el valor de aqui en la doble llave de alli 
        })

def hello(request, id): #request --> info que me manda el usuario cuando trate de ejecutar esta funcion
    print(id) #aqui puedo hacer lo que quiera con el id --> cualquier operacion matematica o lo que sea y gradarlo y que sea ese resultado lo q se imprima en la web
    return HttpResponse("<h1>Hola %s</h1>" % id)  # respuesta http --> devuelve al navegador este mensaje. Le puedo poner si es un header 
                                                #o no como en html para cambiar tamaño

def about(request):
    return render(request, 'about.html')

@login_required
def projects(request):
    #projects = list(Project.objects.values()) #lista de los proyectos que tengo --> pongo values en vez de all porque da error de algo de JSON
    #return JsonResponse(projects, safe=False) #porque es un query
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects 
    })

@login_required
def tasks(request):
    #task = Task.objects.get(id=id)
    #task = get_object_or_404(Task, title=name) # es lo mismo que arriba pero si no encuentra el task te da un 404 para que sepas que se ha caido el servidor?
    #return HttpResponse('task: %s' % task.title)
    #return render(request, 'tasks.html')
    tasks = Task2.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks 
    })

@login_required
def tasks_completed(request):
    tasks = Task2.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted') #las ordena de mas nuevo a viejo
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks 
    })

@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': TaskForm #CreateNewTask() 
        })
    else: 
        try:
            form = TaskForm(request.POST)
            form.save()
            #Task.objects.create(title=request.POST['title'], description=request.POST['description'], done=request.POST['done'], project_id=1)
            return redirect('/tasks/')#la primera barra para que sea desde la ruta inicial y no algo que añada a la ruta actual
        except:
            return render(request, 'tasks/create_task.html', {
                'form': TaskForm, #CreateNewTask()
                'error': '⚠️ Por favor provee un dato valido' 
            })
    
@login_required
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject() 
        })
    else: 
        Project.objects.create(name=request.POST['name'])
        return redirect('/projects/')
    
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
                'form': UserCreationForm
        })
    else: 
        if request.POST['password1'] == request.POST['password2']: #comporbamos que las contraseñas son iguales
            try: 
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError: # para que no caiga toda la aplicacion
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': '⚠️ El usuario ya existe'
                })
        return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': '⚠️ Las contraseñas no coinciden'
                })

@login_required   
def signout(request): #NO PONEMOS LOGOUT PORQUE HAY UNA FUNCION DE DJAGNO QUE SE LLAMA LOGOUT Y PARA QUE NO HAYA CONFUSIONES
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
                    'form': AuthenticationForm,
            })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                        'form': AuthenticationForm,
                        'error': '⚠️ Usuario o contraseña incorrectos'
                })
        else:
            login(request, user)
            return redirect('home')

@login_required        
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task2, pk=task_id, user=request.user) #en vez de task.objects.get() que si no existe el id se cae la red, ponemos get_objects_or_404
        form = TaskForm(instance=task)
        return render(request, 'tasks/task_detail.html',{
            'task': task,
            'form': form
        })
    else: 
        try:
            task = get_object_or_404(Task2, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('home')
        except ValueError:
            return render(request, 'tasks/task_detail.html',{
                'task': task,
                'form': form,
                'error': '⚠️ Error acualizando tarea'
            }) 

@login_required
def task_complete(request, task_id):
    task = get_object_or_404(Task2, pk=task_id, user=request.user) 
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

@login_required         
def task_delete(request, task_id):
    task = get_object_or_404(Task2, pk=task_id, user=request.user) 
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
          
            