from django.urls import path
from django.contrib.auth.views import LogoutView,PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views
from . views import MyLoginView,RegisterView,MyProfile
app_name='credentials'

urlpatterns = [
    # path('test/', views.home,name='home'),
    path('login/', MyLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='finalmovieapp:allMoviesCat'),name='logout'),
    path('register/', RegisterView.as_view(),name='register'),
    path('profile/', MyProfile.as_view(), name='profile'),

    ]