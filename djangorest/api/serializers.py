from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') # Same as using a CharField(read_only=True)
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'id', 'owner', 'title', 'code', 'linenos', 'language', 'style')
        

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # We need to add snippets manually because it's created by the ForeignKey in the Snippet class, and not directly in the User model
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')