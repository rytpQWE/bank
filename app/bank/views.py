from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from bank.models import BankAccount
from bank.serializers import BankAccountSerializer


class AccountViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

    def get_queryset(self):
        """Get object for current user"""
        return self.queryset.filter(user=self.request.user)

