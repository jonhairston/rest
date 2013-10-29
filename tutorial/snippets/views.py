# Create your views here.
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
# who can see what import authentication
from rest_framework import permissions

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
    permission_classes =  (permissions.IsAuthenticatedOrReadOnly,)

    # associates snippets with users
    def pre_save(self, obj):
        obj.owner = self.request.user


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

