from rest_framework import serializers
from cleaners.models import Cleaner


class CleanerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaner
        fields = '__all__'
        #fields = ('id', 'song', 'singer', 'last_modify_date', 'created')