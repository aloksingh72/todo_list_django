from django.urls import path
from .views  import *


urlpatterns= [
    path('',task_list,name='task_list'),
    path('delete/<int:task_id>',delete_task,name='delete_task'),
    path('complete/<int:task_id>',mark_completed,name="mark_complete"),
    

]
