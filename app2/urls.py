
from django.urls import path
from app2.views import signup,user_login,signin,about,sign_out,homepage,user_list



urlpatterns = [

    path('',homepage,name='homepage'),
    path('signup/',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('user_login/', user_login, name='user_login'),
    path('about/',about,name="about"),
    path('logout/',sign_out,name='logout'),
    path('user-list',user_list,name='user-list'),
    


]
