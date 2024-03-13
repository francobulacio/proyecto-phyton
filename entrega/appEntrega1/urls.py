from re import template
from django.urls import path
from appEntrega1 import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name="Index"),
    path('about', views.about, name="About"),
    path('contact', views.contact, name="Contact"),
    path('blogpost', views.blogpost, name="Blogpost"),
    path('addblogpost', views.addblogpost, name="AddBlogPost"),
    path('searchpost', views.searchpost, name="SearchPost"),
    path('searchpostsite', views.searchpostsite, name="SearchPostSite"),
    path('deletepost/<post_id>/', views.deletepost, name="DeletePost"),
    path('register', views.register, name="Register"),
    path('login', views.login_request, name="Login"),
    path('logout', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('profile', views.profile, name="Profile"),
    path('updateprofile', views.updateprofile, name="UpdateProfile"),
    path('updatepost/<post_id>/', views.updatepost, name="UpdatePost"),
]