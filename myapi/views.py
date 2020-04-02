from rest_framework import viewsets
from .serializers import HeroSerializer, VillainSerializer
from .models import Hero, Villain


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


class VillainViewSet(viewsets.ModelViewSet):
    queryset = Villain.objects.all()
    serializer_class = VillainSerializer
