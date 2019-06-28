from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

# Create a router and register our viewset with it
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API urls re now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]