from django.urls import path

from profiles_api import views

<<<<<<< Updated upstream
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
=======
>>>>>>> Stashed changes

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]