from django.urls import path
from .views import register, index, about, login, forgotten

urlpatterns = [
  # path('register/', SignUpView.as_view(), name='signup'),
  path('register/', register, name='register'),
  path('about/', about, name='about'),
  path('login/', login, name='login'),
  path('forgotten_password/', forgotten, name='forgotten'),
  path('', index, name='index'),
]