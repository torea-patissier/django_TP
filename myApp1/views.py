from rest_framework.viewsets import ModelViewSet
from .models import Artiste
from .serializer import SerializerArtiste


class ArtisteViewSet(ModelViewSet):
    serializer_class = SerializerArtiste

    def get_queryset(self):

        queryset = Artiste.objects.all()

        nomparam = self.request.GET.get('nom')
        styleparam = self.request.GET.get('style')

        if nomparam is not None:
            queryset = queryset.filter(nom=nomparam)

        if styleparam is not None:
            queryset = queryset.filter(style=styleparam)

        return queryset
