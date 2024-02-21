from django.urls import include, path

from talent_app import views

urlpatterns = [

    path("",views.think,name='think')
]
