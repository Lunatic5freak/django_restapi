from django.urls import include,path
from . import views

urlpatterns=[
    path('welcome',views.welcome),
    path('getlist',views.getlist),
    path('addemployee',views.addemployee),
]