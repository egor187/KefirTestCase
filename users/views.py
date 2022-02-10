from rest_framework.generics import RetrieveAPIView, ListAPIView, ListCreateAPIView, UpdateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from users.models import KefirUser
from users.serializers import KefirUserSerializer, KefirUserListSerializer, KefirUserUpdateSerializer, KefirAdminUserListSerializer
from KefirService.pagination import KefirPaginator, KefirAdminPaginator


class CommonUserDetailView(RetrieveAPIView):
    queryset = KefirUser.objects.all()
    serializer_class = KefirUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.request.user.pk)
        self.check_object_permissions(self.request, obj)
        return obj


class CommonUserListView(ListAPIView):
    queryset = KefirUser.objects.all()
    serializer_class = KefirUserListSerializer
    pagination_class = KefirPaginator


class CommonUserUpdateView(UpdateAPIView):
    queryset = KefirUser.objects.all()
    serializer_class = KefirUserUpdateSerializer


class AdminUserListView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = KefirUser.objects.all()
    serializer_class = KefirAdminUserListSerializer
    pagination_class = KefirAdminPaginator
