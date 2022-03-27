from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView


def hello_world(request):
    return render(request, 'accountapp/hello_world.html')


class AccountappLogin():
    pass


class AccountAppCreate(CreateView):

    pass

class AccountAppDetail(DetailView):
    pass


class AccountAppUpdate(UpdateView):
    pass


class AccountAppDelete(DeleteView):
    pass

