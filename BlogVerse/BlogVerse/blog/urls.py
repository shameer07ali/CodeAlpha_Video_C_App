from django.urls import path, include 
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home' ),
    path('create/', views.create_blog, name='create_blog'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('edit/<int:pk>/', views.edit_blog, name='edit_blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)