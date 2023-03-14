from django.urls import path
from . import views



app_name = 'weather'

urlpatterns = [
    path('user/login/', views.login_view, name='login'),
    path('user/signin/', views.register_view, name='register'),
    path('user/create/', views.create_user, name="create"),
    path('user/logout/', views.logout_view, name='logout'),

    path('', views.home_view, name='home'),
    path('city/', views.get_info, name='get_city'),
    path('delete/city/<int:pk>', views.delete_view, name="delete")
]