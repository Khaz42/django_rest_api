from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Snippet
from api.serializers import SnippetSerializer, UserSerializer
from api.permissions import IsOwnerOrReadOnly

# Create your views here.

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides the CRUD actions
    We are also adding a custom 'highlight' action
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            IsOwnerOrReadOnly,)
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This ViewSet automatically provides 'user-list' and 'user-detail'
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer