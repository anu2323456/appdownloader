from django.urls import path
from.import views
app_name='admininterface'
urlpatterns = [

    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('addapp',views.addapp,name='addapp'),
    path('adminlogout',views.adminlogout,name='adminlogout'),
    path('deleteapp/<int:id>',views.deleteapp,name='deleteapp'),
    path('editapp/<int:id>',views.editapp,name='editapp'),

]