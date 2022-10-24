from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet


app_name = 'api'

router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router.register('groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]
