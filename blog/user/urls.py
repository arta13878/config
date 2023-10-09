from django.urls import path,include
from .views import userCreateView

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('signup',userCreateView.as_view(),name='signup')
]

