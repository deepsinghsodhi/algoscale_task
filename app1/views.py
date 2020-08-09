from django.shortcuts import render,redirect
from app1.forms import signupform
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import DeleteView
from django.urls import reverse_lazy

# Create your views here.
def loginpage(request):
    return redirect('/accounts/login')

def signup_form(request):
    form = signupform()
    if request.method == "POST":
        form = signupform(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'app1/signup.html',{'form':form})


def all_users(request):
    users = User.objects.all()
    return render(request,'app1/users.html',{'users':users})

class delete_user(DeleteView):
    model = User
    success_url = reverse_lazy('all_users')
