from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from bank.models import BankAccount, Customer, Transaction
from bank.serializers import BankAccountSerializer, CustomerSerializer, TransactionSerializer


class AccountViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

    def perform_create(self, serializer):
        """Create new bank account"""
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """Get object for current user"""
        return self.queryset.filter(user=self.request.user)


class CustomerCreateViewSet(generics.RetrieveUpdateAPIView):
    """GET, PUT, UPDATE"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    """Get pk object"""

    def get_object(self):
        return self.queryset.filter(user=self.request.user).first()


class TransactionViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin,):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        """Get object for current user"""
        account = BankAccount.objects.filter(user=self.request.user)
        return self.queryset.filter(account_from__in=account)
