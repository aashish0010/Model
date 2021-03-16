from .models import Home
from rest_framework import serializers


class HomeSerializers(serializers.ModelSerializer):
    # username = serializers.CharField(read_only=True)

    class Meta:
        model = Home
        fields = ['username', 'password', 'email', 'phone']
        # read_only_fields = ['name', 'email']

    def validate_password(self, value):
        if len(value) <= 8:
            raise serializers.ValidationError('Password must be larger then 8')
        return value