from .models import Account
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]