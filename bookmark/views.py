from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Serializers
from .serializers import BookmarkSerializer, UserLoginSerializer, UserModelSerializer

# Models
from .models import Bookmark
from django.contrib.auth.models import User
from django.db.models import Q

class BookmarkViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]  
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        if user and user.is_authenticated:
            return Bookmark.objects.filter(Q(is_public=True) | Q(owner=user))
        return Bookmark.objects.filter(is_public=True)

class UserViewSet(viewsets.ModelViewSet):
    """
    User view set
    """
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
