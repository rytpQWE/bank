from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class ApiTestCaseAuth(APITestCase):
    customer_url = reverse('customer')
    account_url = reverse('account-list')
    transaction_url = reverse('transaction-list')

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_customers_authenticated(self):
        response = self.client.get(self.customer_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_account_authenticated(self):
        response = self.client.get(self.account_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_transaction_authenticated(self):
        response = self.client.get(self.transaction_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
