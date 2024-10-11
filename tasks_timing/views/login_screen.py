from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from ..forms import SignUpForm, UpdateDataProfileForm

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.warning(request, f'You Have Been Logged In!, Welcome @{request.user.username.lower()}')
                return redirect('home')
            else:
                messages.warning(request, f'There was an error loggin in. Try Again...')
                return redirect('login')
        else:
            return render(request, 'tasks_timing/login.html', {})



def logout_user(request):
    logout(request)
    messages.warning(request, 'You Have Been Logged Out. See you soon!')
    return redirect('login')



def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            #Log in User
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.warning(request, f'You have successfuly registered! Welcome @{user.username.lower()}')
            return redirect('home')
    return render(request, 'tasks_timing/register.html', {'form': form})



def update_user_data(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateDataProfileForm(request.POST or None, request.FILES or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.warning(request, f'@{request.user.username.lower()}, your profile has been updated!')
            return redirect('home')

        return render(request, 'tasks_timing/update_user_data.html', {
            'user_form': user_form,
        })
    else:
        messages.warning(request, 'You must be logged in to view that page!')
        return redirect('home')
