from django.urls import path
from . import views # . porque mira en el directorio en el que estamos (myapp)

urlpatterns = [
    path('', views.index, name='home'), #vacio para que sea desde la ip que estoy ejecutando? o del localhost // ruta principal y ejecuta funcion hello
    path('about/', views.about, name='about'), #para que visiten about, porque el de arriba es q nada mas entren al link q vean hola mundo
    #path('hello/<str:username>', views.hello),
    path('hello/<int:id>', views.hello, name='hello'), # AHORA ESPERA UN NUEMRO EN USERNAME DE VIEWS
    path('projects/', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='taskscompleted'),
    path('create_task/', views.create_task, name='createtask'),
    path('create_project/', views.create_project, name='createproject'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='signout'),
    path('login/', views.signin, name='signin'),
    path('tasks/<int:task_id>/', views.task_detail, name='taskdetail'),
    path('tasks/<int:task_id>/complete', views.task_complete, name='taskcomplete'),
    path('tasks/<int:task_id>/delete', views.task_delete, name='taskdelete'),
]
