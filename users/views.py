from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .models import KefirUser
from .serializers import KefirUserSerializer


class CommonUserDetailView(RetrieveAPIView):
    queryset = KefirUser.objects.all()
    serializer_class = KefirUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.request.user.pk)
        self.check_object_permissions(self.request, obj)
        return obj
