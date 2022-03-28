from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm


has_ownership = [
   account_ownership_required,
   login_required
]


@login_required
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




@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountAppUpdate(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class =  AccountUpdateForm
    success_url = reverse_lazy('accountapp:test')
    template_name = 'accountapp/update.html'

    # 가독성이 떨어지는 코드  ==> 데코레이터로 대체
    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #
    # def post(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountAppDelete(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

