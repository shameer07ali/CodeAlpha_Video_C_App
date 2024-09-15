# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm
from .forms import ProfileUpdateForm
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/home.html', {'blogs': blogs})

# accounts/views.py
from django.contrib.auth.models import User
from django.contrib.auth import login
from blog.forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)  # Make sure to include `request.FILES` to handle file upload
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def about(request):
    return render(request, 'about.html')

# sign in views
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {'form': form})


# accounts/views.py

@login_required
def profile_view(request):
    profile = request.user.profile  # Fetch the user's profile
    return render(request, 'accounts/profile.html', {'profile': profile})

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form,
        'profile': request.user.profile  # Pass profile for the profile picture
    }
    return render(request, 'accounts/edit_profile.html', context)


# logout view 
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('signin')


# blog/views.py

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('home')  # Redirect to a page where blog posts are listed
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})

@login_required
def edit_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if blog.author != request.user:
        return redirect('home')  # Redirect if the user is not the author
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a page where blog posts are listed
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/edit_blog.html', {'form': form})
