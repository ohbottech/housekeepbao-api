# Create your views here.
from cleaners.models import Cleaner
from cleaners.serializers import CleanerSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class CleanerViewSet(viewsets.ModelViewSet):
    queryset = Cleaner.objects.all()
    serializer_class = CleanerSerializer
    permission_classes = (IsAuthenticated,)