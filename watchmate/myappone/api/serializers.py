from rest_framework import serializers
from myappone.models import Movie

# serializers are duplicate of models

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    #this function will validate the data
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)   #extracting**
    
    #old data is going to instance and new to valid_data
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance