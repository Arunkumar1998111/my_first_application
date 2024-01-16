
from django.urls import path
from app2.views import signup,user_login,signin,about,sign_out,homepage,user_list,delete_user,edit_user,update_user,insertdata,updatedata,deletedata

urlpatterns = [

    path('',homepage,name='homepage'),
    path('signup/',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('user_login/', user_login, name='user_login'),
    path('about/',about,name="about"),
    path('logout/',sign_out,name='logout'),
    path('user-list',user_list,name='user-list'),
    path('delete-user/<int:id>/',delete_user, name='delete-user'),
    path('edit-user/<int:id>',update_user,name='edit-user'),



    path('insert',insertdata,name='insertdata'),
    path('update/<id>',updatedata,name='updatedata'),
    path('delete/<id>',deletedata,name='deletedata'),
]
