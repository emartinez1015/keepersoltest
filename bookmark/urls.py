from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookmarkViewSet, UserViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'api/bookmark', BookmarkViewSet, basename='bookmark')
router.register(r'api/user', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls))
]