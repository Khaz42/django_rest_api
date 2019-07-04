from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from api import views

# Create a router and register our viewset with it
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

schema_view = get_schema_view(title='Snippet API')

# The API urls re now determined automatically by the router
urlpatterns = [
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title='Snippet API', public=False)),
    path('', include(router.urls)),
]