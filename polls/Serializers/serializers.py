from rest_framework import serializers

from polls.Models.models import User


class BoatSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)

class UserSerializer(serializers.Serializer):
    forename = serializers.CharField(required=False, allow_blank=True, max_length=30)
    surname = serializers.CharField(required=False, allow_blank=True, max_length=30)
    email = serializers.EmailField(required=False, allow_blank=True, max_length=70)

    class Meta:
        model = User
        fields = ('id', 'forename', 'surname', 'email')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.forename = validated_data.get('forename', instance.forename)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance