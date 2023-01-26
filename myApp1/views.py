from rest_framework.viewsets import ModelViewSet
from .models import Artiste
from .serializer import SerializerArtiste


class ArtisteViewSet(ModelViewSet):
    serializer_class = SerializerArtiste

    @staticmethod
    def get_queryset():
        return Artiste.objects.all()
