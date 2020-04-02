from rest_framework import serializers
from .models import Hero, Villain


class VillainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Villain
        fields = ('name', 'super_power')


class HeroSerializer(serializers.ModelSerializer):
    villains = VillainSerializer(many=True)

    class Meta:
        model = Hero
        fields = ('name', 'alias', 'villains')

