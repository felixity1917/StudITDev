from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('', views.todo_list, name='todo_list'),
    path('home/', views.todo_list, name='todo_list'),
    # path('', views.home, name='home'),
    # path('todos/', views.todos, name='Todos')
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
]
