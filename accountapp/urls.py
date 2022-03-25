from django.urls import path

from accountapp.views import AccountAppCreate, AccountAppDetail, AccountAppUpdate, AccountAppDelete

app_name = 'accountapp'

urlpatterns = [

    path('create/', AccountAppCreate.as_view(), name='create'),
    path('detail/', AccountAppDetail.as_view(), name='detail'),
    path('update/', AccountAppUpdate.as_view(), name='update'),
    path('delete/', AccountAppDelete.as_view(), name='delete'),


]