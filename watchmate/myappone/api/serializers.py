from rest_framework import serializers
from myappone.models import Movie

# serializers are duplicate of models
    
class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'name', 'description', 'active']
        # fields = "__all__"
        # exclude = ['active']

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Title and Description must not have contain the same value!')
        else:
            return data

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short!')
        else:
            return value
        
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name is too short!')


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     #this function will validate the data
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)   #extracting**
    
#     #old data is going to instance and new to valid_data
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance