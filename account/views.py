from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


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
            Profile.objects.create(user=new_user)  # creates an empty profile when a user signs up
            return render(request, 'account/register_done.html', {'user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'register_form': form})


@login_required
def edit(request):
    changed = False
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            changed = True
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form,
                                                 'profile_form': profile_form,
                                                 'changed': changed
                                                 })


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request, 'account/user/user_list.html', {'section': 'people', 'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'account/user/detail.html', {'section': 'people', 'user': user})
