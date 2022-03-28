from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world
from accountapp.views import AccountAppCreate, AccountAppDetail, AccountAppUpdate, AccountAppDelete

app_name = 'accountapp'



urlpatterns = [

    path('test/', hello_world, name='test'),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountAppCreate.as_view(), name='create'),
    path('detail/<int:pk>', AccountAppDetail.as_view(), name='detail'),
    path('update/<int:pk>', AccountAppUpdate.as_view(), name='update'),
    path('delete/<int:pk>', AccountAppDelete.as_view(), name='delete'),


]