# Create your views here.
from cleaners.models import Cleaner
from cleaners.serializers import CleanerSerializer

from rest_framework import viewsets


# Create your views here.
class CleanerViewSet(viewsets.ModelViewSet):
    queryset = Cleaner.objects.all()
    serializer_class = CleanerSerializer