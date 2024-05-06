from django.urls import path
from.import views
app_name='userinterface'
urlpatterns = [

    path('home',views.userhome,name='home'),
    path('register',views.userregister,name='userregister'),
    path('login',views.userlogin,name='userlogin'),
    path('appdetail/<int:id>/',views.getappdetail,name='appdetail'),
    path('appdownload/<str:name>/<int:points>/',views.downloadapp,name='downloadapp'),
    path('points',views.getpoints,name='getpoints'),
    path('gettask',views.gettask,name='gettask'),
    path('getprofile',views.getprofile,name='getprofile'),

    
]