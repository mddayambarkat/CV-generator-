from . import views
from django.urls import path

app_name='pdf'


urlpatterns = [
    path('', views.accept,name='accept'),
    path('<int:id>/', views.resume,name='resume'),
    path("list/",views.list,name="list"),
]