from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name="index"),
    path('filmsList' , views.filmsList , name="filmsList"),
    path('login', views.log_in , name="login"),
    path('logout', views.log_out, name="logout"),
    path('signup', views.signup, name="signup"),
    path('addWatchList', views.addWatchList, name="addWatchList"),
    path('addToList/<int:id>', views.addToList, name="addToList"),
    path('deleteUser', views.deleteUser, name="deleteUser"),
    path('delete/<str:user_name>', views.deleteExecution, name="deleteExecution")
]