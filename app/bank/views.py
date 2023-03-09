from rest_framework import generics, viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from bank.models import BankAccount, Customer, Transaction
from bank.serializers import BankAccountSerializer, CustomerSerializer, TransactionSerializer
from bank.services import make_trans


class AccountViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin, ):
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
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin, ):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            make_trans(**serializer.validated_data)
        except ValueError:
            content = {'error': 'ERROR BL9T'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        """Return object for current authenticated user only"""
        accounts = BankAccount.objects.filter(user=self.request.user)
        return self.queryset.filter(account_from__in=accounts)
