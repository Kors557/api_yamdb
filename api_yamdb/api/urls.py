from django.urls import include, path
from rest_framework import routers

from .views import CategoriesViewSet, GenresViewSet, TitlesViewSet
from users.views import UsersViewSet, RegisterUser, TakeToken

router = routers.DefaultRouter()
router.register('categories', CategoriesViewSet)
router.register('genres', GenresViewSet)
router.register('titles', TitlesViewSet)
router.register('users', UsersViewSet, basename='users'),

urlpatterns = [
    path('v1/auth/signup/', RegisterUser.as_view(), name='register_user'),
    path('v1/auth/token/', TakeToken.as_view(), name='take_token'),
    path('v1/', include(router.urls)),
]
