from django.urls import (
    include,
    path,
)
from rest_framework.routers import DefaultRouter

from profiles_api import views
from profiles_api.views import HelloViewSet


router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
