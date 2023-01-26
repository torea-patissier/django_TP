from rest_framework import serializers
from myApp1.models import Artiste


class SerializerArtiste(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ['nom', 'style']