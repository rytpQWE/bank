from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from bank.models import BankAccount, Customer, Transaction
from bank.serializers import BankAccountSerializer, CustomerSerializer, TransactionSerializer


class AccountViewSet(ReadOnlyModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

    def get_queryset(self):
        """Get object for current user"""
        return self.queryset.filter(user=self.request.user)


class CustomerCreateViewSet(generics.RetrieveUpdateAPIView):
    """GET, PUT, UPDATE """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    """Get pk object"""

    def get_object(self):
        return self.queryset.filter(user=self.request.user).first()


class TransactionViewSet(viewsets.GenericViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
