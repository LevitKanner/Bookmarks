from django.shortcuts import render
# from .forms import LoginForm
from django.contrib.auth import  authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm


# Create your views here.
# def user_login(request):
#     if request.method == 'POST':
#         login_form = LoginForm(request.POST)
        
#         if login_form.is_valid():
#             data = login_form.cleaned_data
#             user = authenticate(request,
#                                 username=data['username'],
#                                 password=data['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request,user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse("Invalid login")
#     else:
#         login_form = LoginForm()
#     return render(request, 'account/login.html', {'form': login_form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'register_form': form})
        
        
        
    