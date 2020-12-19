from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(
    'posts', 
    PostViewSet, 
    basename='posts'
)

router.register(
    r'posts/(?P<post_id>\d+)/comments', 
    CommentViewSet,
    basename='comments'
    )



urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token)
]
