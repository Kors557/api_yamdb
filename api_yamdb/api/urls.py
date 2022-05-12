from django.urls import include, path
from rest_framework import routers

from .views import CategoriesViewSet, GenresViewSet, TitlesViewSet
from users.views import UsersViewSet

router = routers.DefaultRouter()
router.register('categories', CategoriesViewSet)
router.register('genres', GenresViewSet)
router.register('titles', TitlesViewSet)
router.register('users', UsersViewSet, basename='users'),

urlpatterns = [
    path('v1/', include(router.urls)),
]
