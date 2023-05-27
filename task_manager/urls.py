from django.urls import path, include

from task_manager.views import index

urlpatterns = [
    path("index/", index, name="index"),

    path("", index, name="index")

]

app_name = "task_manager"
