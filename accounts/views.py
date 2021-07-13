from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# Create your views here.
from .forms import LoginForm
from django.contrib.auth.decorators import login_required



# def login_user(request):
#     """
#     If the form is submitted, instantiate the login form with the data presented
#     if from is valid,check if details matches database. If true, log in user

#     """
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request,username=cd['username'],password=cd['password'])
#             user1 = user.username
#             print(user1)
#             print(user)
#             if user is not None:
#                 if user.is_active:

#                     login(request,user)
#                     return HttpResponse('/Authenticated Successfully')
#                 else:
#                     return HttpResponse('Disables Account')
#             return HttpResponse('Invalid login details')

#     else:

#         form = LoginForm()
#     context = {
        
#         'form':form,
#     }
#     return render(request,'accounts/login.html',context)

@login_required
def dashboard(request):
    context = {
        'section':'dashboard',
    }
    return render(request,'accounts/dashboard.html',context)
