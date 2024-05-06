from django.urls import path
from.import views
app_name='restapp'
urlpatterns = [

    path('api/adminlogin',views.admin_login,name='adminlogin'),
    path('api/addapp',views.addapp,name='addapp'),
    path('api/deleteapp/<int:id>/',views.addapp,name='addapp'),


]