from django.urls import path

from profiles_api import views

<<<<<<< HEAD
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
>>>>>>> 17327c535d5e3d4120fe74814adc3699f14f9291
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
<<<<<<< HEAD
router.register('profile', views.UserProfileViewSet)
=======
>>>>>>> Stashed changes
=======
=======
>>>>>>> d98eea2a42c8948a0709e607b6256b4139660220
>>>>>>> 17327c535d5e3d4120fe74814adc3699f14f9291

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]