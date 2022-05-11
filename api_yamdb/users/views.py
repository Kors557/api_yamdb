from rest_framework import viewsets, filters
from .models import User
from .serializers import UserSerializer
from .permissions import IsAdminUser, IsAdminOrReadOnly


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, IsAdminOrReadOnly)
    pagination_class = None
    filter_backends = (filters.SearchFilter,)
    lookup_value_regex = r'[\w\@\.\+\-]+'
    search_fields = ('username',)

