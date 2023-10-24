from django.urls import path
from puppies import views

urlpatterns = [
	path('',views.main,name='main'),
	path('main',views.main,name='main'),
	path('more/<int:isbn>',views.more,name='more'),
	
]
