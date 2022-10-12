from django.urls import path
from todolist.views import show_todolist, register_user, login_user, logout_user, create_task, delete_task, show_json

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('delete/<int:id>', delete_task, name="delete_task"),
    path('json/', show_json, name='show_json'),
]