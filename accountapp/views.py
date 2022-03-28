from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm


def hello_world(request):
    return render(request, 'accountapp/hello_world.html')


# 회원가입
class AccountAppCreate(CreateView):


   model = User
   form_class = UserCreationForm
   success_url = reverse_lazy('accountapp:test')
   template_name = 'accountapp/create.html'

# 개인 페이지
class AccountAppDetail(DetailView):

    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


class AccountAppUpdate(UpdateView):
    model = User
    form_class =  AccountUpdateForm
    success_url = reverse_lazy('accountapp:test')
    template_name = 'accountapp/update.html'


class AccountAppDelete(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

