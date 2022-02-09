from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .models import KefirUser
from .serializers import KefirUserSerializer, KefirUserListSerializer, KefirUserUpdateSerializer
from KefirService.pagination import KefirPaginator


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

    # def partial_update(self, request, *args, **kwargs):
    #     super(CommonUserUpdateView, self).partial_update(request, *args, **kwargs)
