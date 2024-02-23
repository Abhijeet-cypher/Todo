from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('logout', user_logout, name="logout"),
    path('signup/', user_signup, name="signup"),
    path('login/', user_login, name="login"),
    path('delete/<int:id>', delete, name="delete"),
    path('update/<int:id>', update, name="update"),
]