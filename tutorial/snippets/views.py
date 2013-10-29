# Create your views here.
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
# who can see what import authentication
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly

from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


#created an endpoint for the root of the api
@api_view(('GET',))
def apit_root(request, format=None):
    return Response({
        'users':reverse('users-list',request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


# creating an endpoint for the highlighted snippets
class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # who can edit this view, or is it read only it unauth users
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # associates snippets with users
    def pre_save(self, obj):
        obj.owner = self.request.user


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # who can edit this view or is it read only
    # added custom permissions class here
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    # associates snippets with users
    def pre_save(self, obj):
        obj.owner = self.request.user


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

