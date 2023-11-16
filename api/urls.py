from django.urls import path
from .views import UserRegistrationView, UserLoginView, PostCreateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
]
