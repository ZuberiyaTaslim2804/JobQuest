from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index),
    path('open_signup',views.open_signup,name="open_signup"),
    path('signup',views.signup,name="signup"),
]