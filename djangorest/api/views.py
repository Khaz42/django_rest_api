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

# This ViewSet automatically provides the CRUD actions
# We are also adding a custom 'highlight' action
class SnippetViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all snippets.

    create:
    Create a new snippet instance

    read:
    Return the snippet corresponding to {id}

    update:
    Edit the existing snippet

    partial_update:
    Edit the existing snippet

    delete:
    Remove the snippet instance from database.

    highlight:
    Return the highlight of a given snippet.
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


# This ViewSet automatically provides 'user-list' and 'user-detail'
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:
    Return a list of all existing users.

    retrieve:
    Return the user corresponding to {id}.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer