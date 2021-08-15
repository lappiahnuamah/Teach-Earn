from django.urls import path
from .views import SignUpView, home

urlpatterns = [
  path('register/', SignUpView.as_view(), name='signup'),
  path('', home, name='home'),
]