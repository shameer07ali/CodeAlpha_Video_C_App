# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .models import Blog

# Sign Up Form (with Profile Picture field)
class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    profile_picture = forms.ImageField(required=False)  # Add the profile picture field

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile_picture']  # Include profile picture

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            # Save profile picture
            Profile.objects.create(user=user, profile_picture=self.cleaned_data['profile_picture'])
        return user



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']  # Include profile_picture field
# blog/forms.py



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
