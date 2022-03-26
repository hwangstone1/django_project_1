from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView


class AccountappLogin(Login)

class AccountAppCreate(CreateView):

      form_class = UserCreationForm
      template_name = 'forms.html'

class AccountAppDetail(DetailView):
    pass

class AccountAppUpdate(UpdateView):
    pass

class AccountAppDelete(DeleteView):
    pass

