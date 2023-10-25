from django.urls import path
from books import views

urlpatterns = [
	path('',views.login,name='login'),
	path('login',views.login,name='login'),
	path('logout',views.logout,name='logout'),
	path('register',views.register,name='register'),
	path('newuser',views.newuser,name='newuser'),
	path('checkusername',views.checkusername,name='checkusername'),
	path('main',views.main,name='main'),
	path('mylist',views.mylist,name='mylist'),
	path('addlist',views.addlist,name='addlist'),
	path('more/<int:isbn>',views.more,name='more'),
	
]
