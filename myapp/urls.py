from django.urls import path
from . import views
app_name='myapp'

urlpatterns = [
	path('',views.index,name='index'),
	path('register/',views.register,name='register'),
	path('login/',views.login,name='login'),
	path('home/<int:id>',views.home,name='home'),
	path('logout/',views.logout,name='logout'),
	path('passwordchange/<int:id>',views.passwordchange,name='passwordchange'),
	path('viewprofile/<int:id>',views.viewprofile,name='viewprofile'),
	path('gallery/',views.gallery,name='gallery'),
	path('viewgallery/',views.viewgallery,name='viewgallery')
]