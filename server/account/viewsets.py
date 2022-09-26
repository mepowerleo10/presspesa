from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from server.account.models import Account

from server.account.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    http_method_names = [
        "get",
    ]
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["updated"]
    ordering = ["-updated"]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Account.objects.all()

    def get_object(self):
        lookup_field_value = self.kwargs(self.lookup_field)

        obj = Account.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj
